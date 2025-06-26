from fastapi import HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


# Placeholder in-memory token store (for demo purposes)
FAKE_TOKENS = {}

security = HTTPBearer()


# PUBLIC_INTERFACE
def get_current_user(
    credentials: HTTPAuthorizationCredentials = security,
) -> dict:
    """Dependency to get the current user from a fake token."""
    token = credentials.credentials
    user = FAKE_TOKENS.get(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing authentication token.",
        )
    return user
