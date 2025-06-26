from fastapi import APIRouter, HTTPException
from .models import UserCreate, User, Token, LoginRequest
from .dependencies import FAKE_TOKENS
from typing import Dict


router = APIRouter(tags=["User"])


# In-memory user "db"
USERS: Dict[int, dict] = {}
USER_EMAIL_INDEX: Dict[str, int] = {}
USER_ID_SEQ = 1


# PUBLIC_INTERFACE
@router.post("/register", response_model=User, summary="Register a new user")
def register(user_in: UserCreate):
    """Register a new user. No duplicate emails allowed."""
    global USER_ID_SEQ
    if user_in.email in USER_EMAIL_INDEX:
        raise HTTPException(status_code=400, detail="Email already registered")
    user_id = USER_ID_SEQ
    USERS[user_id] = {
        "id": user_id,
        "email": user_in.email,
        "password": user_in.password,  # NOTE: Don't store plaintext passwords in prod!
    }
    USER_EMAIL_INDEX[user_in.email] = user_id
    USER_ID_SEQ += 1
    return User(id=user_id, email=user_in.email)


# PUBLIC_INTERFACE
@router.post("/login", response_model=Token, summary="Authenticate user and get token")
def login(login_req: LoginRequest):
    """Login a user and return a fake JWT token (stub implementation)."""
    user_id = USER_EMAIL_INDEX.get(login_req.email)
    if not user_id or USERS[user_id]["password"] != login_req.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # Fake JWT generation (use real JWT in production)
    token = f"fake-token-{user_id}"
    FAKE_TOKENS[token] = USERS[user_id]
    return Token(access_token=token)
