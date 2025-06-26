from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes_users import router as user_router
from .routes_providers import router as provider_router
from .routes_appointments import router as appointment_router

app = FastAPI(
    title="ConnectBook Booking API",
    description=(
        "API for user registration, authentication, appointment scheduling, "
        "and provider management."
    ),
    version="0.1.0",
    openapi_tags=[
        {"name": "User", "description": "User registration and authentication"},
        {"name": "Appointments", "description": "Appointment creation and retrieval"},
        {"name": "Service Providers", "description": "Register and list providers"},
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health"])
def health_check():
    """Health check endpoint."""
    return {"message": "Healthy"}


# Register routes
app.include_router(user_router)
app.include_router(provider_router)
app.include_router(appointment_router)
