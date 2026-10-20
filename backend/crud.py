from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas

# Patients CRUD
def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patients(db: Session):
    return db.query(models.Patient).all()

# Doctors CRUD
def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def get_doctors(db: Session):
    return db.query(models.Doctor).all()

# Appointments CRUD
def create_appointment(db: Session, appt: schemas.AppointmentCreate):
    patient = db.query(models.Patient).filter(models.Patient.id == appt.patient_id).first()
    doctor = db.query(models.Doctor).filter(models.Doctor.id == appt.doctor_id).first()
    if not patient or not doctor:
        raise HTTPException(status_code=404, detail="Patient or Doctor not found")
    
    db_appt = models.Appointment(**appt.dict())
    db.add(db_appt)
    db.commit()
    db.refresh(db_appt)
    return db_appt

def get_appointments(db: Session):
    return db.query(models.Appointment).all()

def delete_appointment(db: Session, appt_id: int):
    appt = db.query(models.Appointment).filter(models.Appointment.id == appt_id).first()
    if not appt:
        raise HTTPException(status_code=404, detail="Appointment not found")
    db.delete(appt)
    db.commit()
    return {"message": "Appointment cancelled successfully"}