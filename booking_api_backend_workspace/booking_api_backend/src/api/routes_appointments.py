from fastapi import APIRouter, Depends
from .models import AppointmentCreate, Appointment
from .dependencies import get_current_user
from typing import Dict, List


router = APIRouter(prefix="/appointments", tags=["Appointments"])


# In-memory appointment "db"
APPOINTMENTS: Dict[int, dict] = {}
APPOINTMENT_ID_SEQ = 1


# PUBLIC_INTERFACE
@router.post("/", response_model=Appointment, summary="Create an appointment")
def create_appointment(
    appointment_in: AppointmentCreate, user: dict = Depends(get_current_user)
):
    """Create an appointment for the current user with a service provider."""
    global APPOINTMENT_ID_SEQ
    appt_id = APPOINTMENT_ID_SEQ
    appointment = {
        "id": appt_id,
        "user_id": user["id"],
        "provider_id": appointment_in.provider_id,
        "time": appointment_in.time,
        "notes": appointment_in.notes,
    }
    APPOINTMENTS[appt_id] = appointment
    APPOINTMENT_ID_SEQ += 1
    return Appointment(**appointment)


# PUBLIC_INTERFACE
@router.get("/", response_model=List[Appointment], summary="Get my appointments")
def get_my_appointments(user: dict = Depends(get_current_user)):
    """List all appointments for the current user."""
    return [Appointment(**a) for a in APPOINTMENTS.values() if a["user_id"] == user["id"]]
