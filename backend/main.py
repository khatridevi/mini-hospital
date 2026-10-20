from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini Hospital Management API", version="1.0")

@app.post("/patients", response_model=schemas.PatientResponse)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db, patient)

@app.get("/patients", response_model=list[schemas.PatientResponse])
def list_patients(db: Session = Depends(get_db)):
    return crud.get_patients(db)

@app.post("/doctors", response_model=schemas.DoctorResponse)
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return crud.create_doctor(db, doctor)

@app.get("/doctors", response_model=list[schemas.DoctorResponse])
def list_doctors(db: Session = Depends(get_db)):
    return crud.get_doctors(db)

@app.post("/appointments", response_model=schemas.AppointmentResponse)
def create_appointment(appt: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    return crud.create_appointment(db, appt)

@app.get("/appointments", response_model=list[schemas.AppointmentResponse])
def list_appointments(db: Session = Depends(get_db)):
    return crud.get_appointments(db)

@app.delete("/appointments/{appt_id}")
def delete_appointment(appt_id: int, db: Session = Depends(get_db)):
    return crud.delete_appointment(db, appt_id)