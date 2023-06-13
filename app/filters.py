from sqlalchemy.orm import Session
from db.models import Patients, Pharmacies, Transactions
from sqlalchemy import func
from fastapi import HTTPException
import re

# Filtros para pacientes

class Patients_filters:
    def __init__(self, db: Session):
        self.db = db
    
    def filter_patients_by_name(self, patient_name: str):
        sanitized_patient_first_name = re.sub(r"[^\w\s]", "", patient_name)
        return self.db.query(Patients).filter(func.lower(Patients.patient_first_name).ilike(f"%{sanitized_patient_first_name.lower()}%")).all()


    def filter_patients_by_last_name(self, patient_last_name: str):
        sanitized_patient_last_name = re.sub(r"[^\w\s]", "", patient_last_name)
        return self.db.query(Patients).filter(func.lower(Patients.patient_last_name).ilike(f"%{sanitized_patient_last_name.lower()}%")).all()

    def filter_patients_by_id(self, patient_id: str):
        sanitized_patient_id = re.sub(r"[^\w\s]", "", patient_id)
        return self.db.query(Patients).filter(Patients.patient_id == sanitized_patient_id).all()

    def get_patients(self, patient_name: str, patient_last_name: str, patient_id: str):
        if patient_id:
            patients = self.filter_patients_by_id(patient_id)
        elif patient_name:
            patients = self.filter_patients_by_name(patient_name)
        elif patient_last_name:
            patients = self.filter_patients_by_last_name(patient_last_name)
        else:
            patients = self.db.query(Patients).all()
        if not patients:
            raise HTTPException(status_code=404, detail="Nenhum paciente encontrado.")

        patient_list = [patient.serialize() for patient in patients]
        return {"patients": patient_list}

# Filtros para farmácias

class Pharmacies_filters:
    def __init__(self, db: Session):
        self.db = db
    
    def filter_pharmacies_by_name(self, pharmacy_name: str):
        sanitized_pharmacy_name = re.sub(r"[^\w\s]", "", pharmacy_name)
        return self.db.query(Pharmacies).filter(func.lower(Pharmacies.pharmacy_name).ilike(f"%{sanitized_pharmacy_name.lower()}%")).all()

    def filter_pharmacies_by_id(self, pharmacy_id: str):
        sanitized_pharmacy_id = re.sub(r"[^\w\s]", "", pharmacy_id)
        return self.db.query(Pharmacies).filter(Pharmacies.pharmacy_id == sanitized_pharmacy_id).all()

    def filter_pharmacies_by_city(self, pharmacy_city: str):
        sanitized_pharmacy_city = re.sub(r"[^\w\s]", "", pharmacy_city)
        return self.db.query(Pharmacies).filter(func.lower(Pharmacies.pharmacy_city).ilike(f"%{sanitized_pharmacy_city.lower()}%")).all()

    def get_pharmacies(self, pharmacy_name: str, pharmacy_id: str, pharmacy_city: str):
        if pharmacy_id:
            pharmacies = self.filter_pharmacies_by_id(pharmacy_id)
        elif pharmacy_name:
            pharmacies = self.filter_pharmacies_by_name(pharmacy_name)
        elif pharmacy_city:
            pharmacies = self.filter_pharmacies_by_city(pharmacy_city)
        else:
            pharmacies = self.db.query(Pharmacies).all()

        pharmacy_list = [pharmacy.serialize() for pharmacy in pharmacies]
        return {"pharmacies": pharmacy_list}


# Filtros para transações

class Transactions_filters:
    def __init__(self, db: Session):
        self.db = db
    
    def filter_transactions_by_id(self, transaction_id: str):
        sanitized_transaction_id = re.sub(r"[^\w\s]", "", transaction_id)
        return self.db.query(Transactions).filter(Transactions.transaction_id == sanitized_transaction_id)

    def filter_transactions_by_patient_name(self, patient_name: str):
        sanitized_patient_name = re.sub(r"[^\w\s]", "", patient_name)
        return self.db.query(Transactions).filter(Transactions.rel_patients.has(Patients.patient_first_name.ilike(f"%{sanitized_patient_name}%"))).all()

    def filter_transactions_by_patient_id(self, patient_id: str):
        sanitized_patient_id = re.sub(r"[^\w\s]", "", patient_id)
        return self.db.query(Transactions).filter(Transactions.rel_patients.has(Patients.patient_id == sanitized_patient_id))

    def get_transactions(self, transaction_id: str, patient_name: str, patient_id: str):
        query = self.db.query(Transactions)
        
        if transaction_id:
            transactions = self.filter_transactions_by_id(transaction_id)
        elif patient_name:
            transactions = self.filter_transactions_by_patient_name(patient_name)
        elif patient_id:
            transactions = self.filter_transactions_by_patient_id(patient_id)
        else:
            transactions = query.all()

        transaction_list = [transaction.serialize() for transaction in transactions]
        return {"transactions": transaction_list}
