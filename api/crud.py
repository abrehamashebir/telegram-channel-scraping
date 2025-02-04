from sqlalchemy.orm import Session
from models import TelegramMessage
from schemas import TelegramMessageCreate

def create_message(db: Session, message: TelegramMessageCreate):
    db_message = TelegramMessage(**message.model_dump())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TelegramMessage).offset(skip).limit(limit).all()
