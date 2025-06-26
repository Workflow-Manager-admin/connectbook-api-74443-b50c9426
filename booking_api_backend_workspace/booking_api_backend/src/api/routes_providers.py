from fastapi import APIRouter
from .models import ServiceProviderCreate, ServiceProvider
from typing import Dict, List


router = APIRouter(prefix="/providers", tags=["Service Providers"])


# In-memory provider "db"
PROVIDERS: Dict[int, dict] = {}
PROVIDER_ID_SEQ = 1


# PUBLIC_INTERFACE
@router.post("/", response_model=ServiceProvider, summary="Register a new service provider")
def register_provider(provider_in: ServiceProviderCreate):
    """Register a new service provider (e.g. doctor, tutor)."""
    global PROVIDER_ID_SEQ
    provider_id = PROVIDER_ID_SEQ
    PROVIDERS[provider_id] = {
        "id": provider_id,
        "name": provider_in.name,
        "category": provider_in.category,
    }
    PROVIDER_ID_SEQ += 1
    return ServiceProvider(id=provider_id, name=provider_in.name, category=provider_in.category)


# PUBLIC_INTERFACE
@router.get("/", response_model=List[ServiceProvider], summary="List all service providers")
def list_providers():
    """List all registered service providers."""
    return [ServiceProvider(**info) for info in PROVIDERS.values()]
