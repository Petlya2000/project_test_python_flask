# schemas.py
from pydantic import BaseModel
from datetime import datetime

class QuestionBase(BaseModel):
    text: str

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class AnswerBase(BaseModel):
    text: str
    user_id: str

class AnswerCreate(AnswerBase):
    question_id: int

class Answer(AnswerBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
