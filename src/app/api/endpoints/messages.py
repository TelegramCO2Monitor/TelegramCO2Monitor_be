from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.app.depends import get_db
from src.models.Message import Message


router = APIRouter()


@router.get('/get_messages')
def get_messages(db: Session = Depends(get_db)):
    try:
        messages = db.query(Message).all()
        if not messages:
            raise HTTPException(status_code=404, detail="No messages found")
        return messages
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/get_user_messages')
def get_user_messages(user_id: int, db: Session = Depends(get_db)):
    return db.query(Message).filter(Message.user_id == user_id).all()

