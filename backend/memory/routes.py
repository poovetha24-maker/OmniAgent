from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from backend.database.connection import get_db
from backend.memory.service import (
    create_memory,
    get_memories,
    search_memories,
    delete_memory
)

router = APIRouter(
    prefix="/memory",
    tags=["Memory"]
)


class MemoryCreate(BaseModel):
    user_id: str
    content: str = Field(min_length=1)


class MemorySearch(BaseModel):
    user_id: str
    query: str = Field(min_length=1)
    limit: int = Field(default=3, ge=1, le=20)


@router.post("/")
def add_memory(
    memory: MemoryCreate,
    db: Session = Depends(get_db)
):
    new_memory = create_memory(
        db,
        memory.user_id,
        memory.content
    )

    return {
        "message": "Memory saved successfully",
        "memory": {
            "id": new_memory.id,
            "user_id": new_memory.user_id,
            "content": new_memory.content,
            "created_at": new_memory.created_at
        }
    }


@router.post("/search")
def semantic_search(
    search: MemorySearch,
    db: Session = Depends(get_db)
):
    results = search_memories(
        db,
        search.user_id,
        search.query,
        search.limit
    )

    return {
        "user_id": search.user_id,
        "query": search.query,
        "results": [
            {
                "id": row.id,
                "content": row.content,
                "created_at": row.created_at,
                "similarity": float(row.similarity)
            }
            for row in results
        ]
    }


@router.get("/{user_id}")
def fetch_memories(
    user_id: str,
    db: Session = Depends(get_db)
):
    memories = get_memories(db, user_id)

    return {
        "user_id": user_id,
        "memories": [
            {
                "id": memory.id,
                "content": memory.content,
                "created_at": memory.created_at
            }
            for memory in memories
        ]
    }


@router.delete("/{memory_id}")
def remove_memory(
    memory_id: str,
    db: Session = Depends(get_db)
):
    memory = delete_memory(db, memory_id)

    if not memory:
        raise HTTPException(
            status_code=404,
            detail="Memory not found"
        )

    return {
        "message": "Memory deleted successfully",
        "memory_id": memory_id
    }