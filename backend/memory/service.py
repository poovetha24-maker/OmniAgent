from sqlalchemy.orm import Session
from sqlalchemy import text

from backend.memory.model import Memory
from backend.memory.embedding import generate_embedding


def create_memory(db: Session, user_id: str, content: str):
    # Generate embedding from the memory content
    embedding = generate_embedding(content)

    # Convert Python list into CockroachDB vector format
    embedding_string = "[" + ",".join(map(str, embedding)) + "]"

    # Create memory
    memory = Memory(
        user_id=user_id,
        content=content
    )

    db.add(memory)

    try:
        # Get the generated ID without committing yet
        db.flush()

        # Store embedding in CockroachDB VECTOR column
        db.execute(
            text("""
                UPDATE memories
                SET embedding = CAST(:embedding AS VECTOR)
                WHERE id = :memory_id
            """),
            {
                "embedding": embedding_string,
                "memory_id": memory.id
            }
        )

        # Commit memory + embedding together
        db.commit()
        db.refresh(memory)

    except Exception:
        db.rollback()
        raise

    return memory


def get_memories(db: Session, user_id: str):
    return (
        db.query(Memory)
        .filter(Memory.user_id == user_id)
        .order_by(Memory.created_at.desc())
        .all()
    )


def search_memories(
    db: Session,
    user_id: str,
    query: str,
    limit: int = 3
):
    # Generate embedding for the user's query
    query_embedding = generate_embedding(query)

    # Convert embedding into CockroachDB VECTOR format
    query_vector = "[" + ",".join(map(str, query_embedding)) + "]"

    # Search using cosine distance
    results = db.execute(
        text("""
            SELECT
                id,
                user_id,
                content,
                created_at,
                1 - (embedding <=> CAST(:query_vector AS VECTOR)) AS similarity
            FROM memories
            WHERE user_id = :user_id
              AND embedding IS NOT NULL
            ORDER BY embedding <=> CAST(:query_vector AS VECTOR)
            LIMIT :limit
        """),
        {
            "query_vector": query_vector,
            "user_id": user_id,
            "limit": limit
        }
    ).fetchall()

    return results


def delete_memory(db: Session, memory_id: str):
    memory = (
        db.query(Memory)
        .filter(Memory.id == memory_id)
        .first()
    )

    if memory:
        db.delete(memory)
        db.commit()

    return memory