from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_async_session

router = APIRouter()

@router.get("/db-check")
async def db_check(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(text("SELECT 1"))
    return {"db": "connected", "result": result.scalar()}