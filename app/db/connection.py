from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Conexão com o banco
engine = create_engine("sqlite:///db/backend_test.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
