from sqlalchemy import Column, Integer, String, DateTime, Numeric, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class CreditRequestsLog(Base):
    __tablename__ = "creditrequestslog"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(String(50), index=True)
    request_type = Column(Integer, index=True)
    sender = Column(String(50), index=True)
    receiver = Column(String(50), index=True)
    credits = Column(Integer)
    amount = Column(Numeric(10, 2))
    created_at = Column(DateTime, default=datetime.utcnow)