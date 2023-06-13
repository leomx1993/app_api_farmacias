from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Numeric
from datetime import datetime

Base = declarative_base()

class Patients(Base):
    __tablename__ = "PATIENTS"

    patient_id = Column("UUID", String(11), primary_key=True, index=True)
    patient_first_name = Column("FIRST_NAME", String(20))
    patient_last_name = Column("LAST_NAME", String(20))
    patient_date_of_birth = Column("DATE_OF_BIRTH", DateTime)

    def serialize(self):
        return {
            "patient_id": self.patient_id,
            "patient_first_name": self.patient_first_name,
            "patient_last_name": self.patient_last_name,
            "patient_date_of_birth": self.patient_date_of_birth
        }
    
class Pharmacies(Base):
    __tablename__ = "PHARMACIES"

    pharmacy_id = Column("UUID", String(9), primary_key=True, index=True)
    pharmacy_name = Column("NAME", String(20))
    pharmacy_city = Column("CITY", String(20))

    def serialize(self):
        return {
            "pharmacy_id": self.pharmacy_id,
            "pharmacy_name": self.pharmacy_name,
            "pharmacy_city": self.pharmacy_city
        }

class Transactions(Base):
    __tablename__ = "TRANSACTIONS"

    transaction_id = Column("UUID", String(8), primary_key=True, index=True)
    patient_id = Column("PATIENT_UUID", String(11), ForeignKey("PATIENTS.UUID"))
    pharmacy_id = Column("PHARMACY_UUID", String(9), ForeignKey("PHARMACIES.UUID"))
    transaction_amount = Column("AMOUNT", Numeric(precision=10, scale=2))
    transaction_timestamp = Column("TIMESTAMP", DateTime)
    
    # Atributos para referenciar as colunas desejadas
    rel_patients = relationship("Patients", foreign_keys=[patient_id])
    rel_pharamcies = relationship("Pharmacies", foreign_keys=[pharmacy_id])


    def serialize(self):
        return {
            "patient_id": self.patient_id,
            "patient_name": self.rel_patients.patient_first_name,
            "patient_last_name": self.rel_patients.patient_last_name,
            "patient_date_of_birth": self.rel_patients.patient_date_of_birth.date().isoformat(),
            "pharmacy_id": self.pharmacy_id,
            "pharmacy_name": self.rel_pharamcies.pharmacy_name,
            "pharmacy_city": self.rel_pharamcies.pharmacy_city,
            "transaction_id": self.transaction_id,
            "transation_amount": self.transaction_amount,
            "transaction_date": self.transaction_timestamp.date().isoformat()
            
        }

