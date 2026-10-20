from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    contact: str
    address: Optional[str] = None

class PatientResponse(PatientCreate):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

class DoctorCreate(BaseModel):
    name: str
    specialization: str
    contact: str

class DoctorResponse(DoctorCreate):
    id: int
    class Config:
        orm_mode = True

class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: str

class AppointmentResponse(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    appointment_date: str
    status: str
    class Config:
        orm_mode = True