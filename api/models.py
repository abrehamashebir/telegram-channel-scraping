from sqlalchemy import Column, Integer, String, Float
from database import Base

class TelegramMessage(Base):
    __tablename__ = 'telegram_messages'
    id = Column(Integer, primary_key=True, index=True)
    # channel = Column(String, index=True)
    message_text = Column(String)
    # timestamp = Column(String)

# class DetectionResult(Base):
#     __tablename__ = 'detection_results'
#     id = Column(Integer, primary_key=True, index=True)
#     image_path = Column(String)
#     bbox = Column(String)  # Store as JSON or comma-separated string
#     confidence = Column(Float)
#     label = Column(String)
