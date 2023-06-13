from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from db.connection import get_db
from token_verification import generate_token, get_current_user
from filters import Patients_filters, Pharmacies_filters, Transactions_filters

app = FastAPI()

# Endpoint de autenticação com token

@app.post("/auth")
def login():
    return generate_token()

# Endpoints da API

@app.get("/patients")
def get_patients(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    patient_name: str = Query(None),
    patient_last_name: str = Query(None),
    patient_id: str = Query(None)
):
    filters = Patients_filters(db)
    return filters.get_patients(patient_name, patient_last_name, patient_id)


@app.get("/pharmacies")
def get_pharmacies(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    pharmacy_name: str = Query(None),
    pharmacy_id: str = Query(None),
    pharmacy_city: str = Query(None)
):
    filters = Pharmacies_filters(db)
    return filters.get_pharmacies(pharmacy_name, pharmacy_id, pharmacy_city)


@app.get("/transactions")
def get_transactions(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
    transaction_id: str = Query(None),
    patient_name: str = Query(None),
    transaction_time: str = Query(None)
):
    filters = Transactions_filters(db)
    return filters.get_transactions(transaction_id, patient_name, transaction_time)
