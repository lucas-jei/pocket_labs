from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import create_access_token
from app.db.session import get_async_session
from app.crud.user import authenticate_user, create_user, get_user_by_email
from app.schemas.auth import Token
from app.schemas.user import UserCreate, UserOut

router = APIRouter()

@router.post("/register", response_model=UserOut, status_code=201)
async def register(user_in: UserCreate, session: AsyncSession = Depends(get_async_session)):
    existing = await get_user_by_email(session, email=str(user_in.email))
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = await create_user(session, user_in=user_in)
    return user

@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_async_session),
):
    user = await authenticate_user(session, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    token = create_access_token(subject=user.email)
    return Token(access_token=token)
