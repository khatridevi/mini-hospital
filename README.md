📊 Mini Hospital Management System
📌 Slide 1: Title Slide
● Title: Mini Hospital Management System
● Subtitle: A Full-Stack Web Application for Managing Patients,
Doctors, and Appointments
● Tech Stack: FastAPI | Streamlit | SQLite / MSSQL | SQLAlchemy
● Presented by: [Your Name / Team Name]
📌 Slide 2: Project Overview & Problem
Statement
● Overview:
○ A lightweight, efficient, and user-friendly management system
designed to streamline daily administrative tasks in a hospital or
clinic.
● Problem Statement:
○ Maintaining manual registers or multiple spreadsheets in small
hospitals/clinics is difficult, error-prone, and time-consuming.
● Solution:
○ A centralized system that manages patient registrations, doctor
records, and appointment scheduling all in one place.
📌 Slide 3: Key Features
● 👤 Patient Management:
○ Add new patients (Name, Age, Gender, Contact, Address).
○ View a list of all saved patients in the system.
● 󰞯 Doctor Management:
○ Create doctor profiles with their specialization and contact
details.
○ Track available doctors.
● 📅 Appointment Scheduling:
○ Book appointments between patients and doctors.
○ Cancel or manage existing appointments.
📌 Slide 4: System Architecture & Folder
Structure
● Architecture: Client-Server Architecture (RESTful API Design).
● Project Folder Structure:
● Plaintext
mini-hospital/
├── backend/ # FastAPI REST API (Business Logic & DB
Connection)
├── frontend/ # Streamlit Web UI (Interactive Interface)
├── .env # Environment Configuration & DB URL
├── requirements.txt# Project Dependencies
└── run.bat # Batch Script to start both servers simultaneously
●
●
📌 Slide 5: Technical Stack (Backend &
Frontend)
● Backend (FastAPI):
○ Asynchronous, high-performance Python framework for building
REST APIs.
○ Dynamic Swagger Docs generation
([http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)).
● ORM & Database (SQLAlchemy + SQLite):
○ Object-Relational Mapping (ORM) to handle database queries
securely.
○ Relational Database (SQLite/MSSQL) for storing structured
records.
● Frontend (Streamlit):
○ Python-based interactive web framework for rapid UI
development and prototyping.
📌 Slide 6: Database Design (Data Models)
● Table Structures:
○ Patients Table: id, name, age, gender, contact, address,
created_at
○ Doctors Table: id, name, specialization, contact
○ Appointments Table: id, patient_id (FK), doctor_id (FK),
appointment_date, status
● Relationships:
○ One-to-Many: One patient can book multiple appointments.
○ One-to-Many: One doctor can have multiple appointments.
📌 Slide 7: API Endpoints Breakdown
Module HTTP
Method
Endpoint Path Functionality
Patients POST /
GET
/patients Add Patient / List
all Patients
Doctors POST /
GET
/doctors Add Doctor / List all
Doctors
Appointmen
ts
POST /
GET
/appointments Book Appointment /
List all
Appointmen
ts
DELETE /appointments/{
id}
Cancel/Remove
Appointment
📌 Slide 8: Execution & Deployment Strategy
● Setup & Running Steps:
1. Virtual Environment Setup: python -m venv .venv
2. Install Dependencies: pip install -r requirements.txt
3. Single-click Execution via run.bat script:
■ Starts FastAPI Backend Server (uvicorn main:app --reload)
■ Starts Streamlit Frontend UI (streamlit run app.py)