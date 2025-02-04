from pydantic import BaseModel

class TelegramMessageBase(BaseModel):
    # channel: str
    message_text: str
    
class TelegramMessageCreate(TelegramMessageBase):
    pass

class TelegramMessage(TelegramMessageBase):
    id: int

    class Config:
        orm_mode = True
