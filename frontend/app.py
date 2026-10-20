import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Mini Hospital App", page_icon="🏥", layout="wide")
st.title("🏥 Mini Hospital Management System")

menu = ["Patients", "Doctors", "Appointments"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Patients":
    st.subheader("Manage Patients")
    
    with st.form("patient_form"):
        name = st.text_input("Patient Name")
        age = st.number_input("Age", min_value=0, max_value=120, value=25)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        contact = st.text_input("Contact Number")
        address = st.text_area("Address")
        submitted = st.form_submit_button("Add Patient")
        
        if submitted:
            res = requests.post(f"{API_URL}/patients", json={"name": name, "age": age, "gender": gender, "contact": contact, "address": address})
            if res.status_code == 200:
                st.success("Patient added successfully!")
            else:
                st.error("Failed to add patient.")

    st.markdown("### Patient Records")
    res = requests.get(f"{API_URL}/patients")
    if res.status_code == 200 and res.json():
        st.dataframe(res.json())
    else:
        st.info("No patients found.")

elif choice == "Doctors":
    st.subheader("Manage Doctors")
    
    with st.form("doctor_form"):
        name = st.text_input("Doctor Name")
        specialization = st.text_input("Specialization (e.g. Cardiologist)")
        contact = st.text_input("Contact Number")
        submitted = st.form_submit_button("Add Doctor")
        
        if submitted:
            res = requests.post(f"{API_URL}/doctors", json={"name": name, "specialization": specialization, "contact": contact})
            if res.status_code == 200:
                st.success("Doctor added successfully!")
            else:
                st.error("Failed to add doctor.")

    st.markdown("### Doctor Records")
    res = requests.get(f"{API_URL}/doctors")
    if res.status_code == 200 and res.json():
        st.dataframe(res.json())
    else:
        st.info("No doctors found.")

elif choice == "Appointments":
    st.subheader("Manage Appointments")
    
    # Fetch patients and doctors for selection
    patients_res = requests.get(f"{API_URL}/patients").json()
    doctors_res = requests.get(f"{API_URL}/doctors").json()
    
    patient_dict = {p["name"] + f" (ID: {p['id']})": p["id"] for p in patients_res} if patients_res else {}
    doctor_dict = {d["name"] + f" - {d['specialization']} (ID: {d['id']})": d["id"] for d in doctors_res} if doctors_res else {}

    with st.form("appointment_form"):
        selected_patient = st.selectbox("Select Patient", options=list(patient_dict.keys()))
        selected_doctor = st.selectbox("Select Doctor", options=list(doctor_dict.keys()))
        appt_date = st.text_input("Appointment Date & Time (e.g., 2026-10-20 10:30 AM)")
        submitted = st.form_submit_button("Book Appointment")
        
        if submitted and selected_patient and selected_doctor:
            payload = {
                "patient_id": patient_dict[selected_patient],
                "doctor_id": doctor_dict[selected_doctor],
                "appointment_date": appt_date
            }
            res = requests.post(f"{API_URL}/appointments", json=payload)
            if res.status_code == 200:
                st.success("Appointment booked successfully!")
            else:
                st.error("Failed to book appointment.")

    st.markdown("### Current Appointments")
    res = requests.get(f"{API_URL}/appointments")
    if res.status_code == 200 and res.json():
        st.dataframe(res.json())
    else:
        st.info("No appointments found.")