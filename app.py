from sqlalchemy.orm import Session

from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from db.database import engine, Base, SessionLocal
from models.models import CreditRequestsLog

from sqlalchemy import inspect

from sqlalchemy import or_


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update with the URL of your React app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/add_tables")
def add_tables(db: Session = Depends(get_db)):
    inspector = inspect(db.bind)
    if not inspector.has_table("creditrequestslog"):
        CreditRequestsLog.metadata.create_all(bind=engine)
        return "Created!"
    return "Table already exists"

@app.get("/register_log", response_model=None)
def register_log(address, request_type, sender, credits, amount, receiver=0, db: Session = Depends(get_db)):
    db_log = CreditRequestsLog(
        company_id = address, 
        request_type = request_type,
        sender = sender,
        receiver = receiver,
        credits = credits,
        amount = amount
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return "Done!"

@app.get("/get_transactions", response_model=None)
def get_transactions(address, db: Session = Depends(get_db)):
    logs = db.query(CreditRequestsLog) \
            .filter(or_(CreditRequestsLog.sender == address, CreditRequestsLog.receiver == address)) \
            .order_by(CreditRequestsLog.id) \
            .all()
    return logs