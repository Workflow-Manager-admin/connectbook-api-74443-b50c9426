from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# ---------- User Models ----------


class UserCreate(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., min_length=6, description="User password")


class User(BaseModel):
    id: int
    email: EmailStr


# ---------- Service Provider Models ----------


class ServiceProviderCreate(BaseModel):
    name: str = Field(..., description="Name of the service provider")
    category: str = Field(..., description="Category such as doctor, tutor, etc.")


class ServiceProvider(BaseModel):
    id: int
    name: str
    category: str


# ---------- Appointment Models ----------


class AppointmentCreate(BaseModel):
    provider_id: int = Field(..., description="ID of the service provider")
    time: datetime = Field(..., description="Scheduled datetime of the appointment")
    notes: Optional[str] = Field(None, description="Optional notes for the appointment")


class Appointment(BaseModel):
    id: int
    user_id: int
    provider_id: int
    time: datetime
    notes: Optional[str] = None


# ---------- Auth Token Models ----------


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    email: EmailStr
    password: str
