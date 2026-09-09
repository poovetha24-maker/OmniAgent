from sqlalchemy import text

from backend.database.connection import engine
from backend.memory.model import Base


def init_db():
    # Create the memories table
    Base.metadata.create_all(bind=engine)

    # Add the embedding column if it does not already exist
    with engine.connect().execution_options(
        isolation_level="AUTOCOMMIT"
    ) as connection:

        connection.execute(
            text("""
                ALTER TABLE memories
                ADD COLUMN IF NOT EXISTS embedding VECTOR(384)
            """)
        )

    # Create the CockroachDB vector index if it does not already exist
    with engine.connect().execution_options(
        isolation_level="AUTOCOMMIT"
    ) as connection:

        connection.execute(
            text("""
                CREATE VECTOR INDEX IF NOT EXISTS memories_embedding_idx
                ON memories (user_id, embedding)
            """)
        )

    print("Memory table, embedding column, and vector index are ready!")


if __name__ == "__main__":
    init_db()