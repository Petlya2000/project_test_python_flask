# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine  # Исправленный импорт
from app.models import Base
from app.crud import *
from app.schemas import *

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}
    
@app.get("/questions/")
def read_questions(db: Session = Depends(get_db)):
    return get_questions(db)

@app.post("/questions/")
def create_new_question(question: QuestionCreate, db: Session = Depends(get_db)):
    return create_question(db, question)

@app.get("/questions/{id}")
def read_question(id: int, db: Session = Depends(get_db)):
    question = get_question(db, id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@app.delete("/questions/{id}")
def delete_question_endpoint(id: int, db: Session = Depends(get_db)):
    delete_question(db, id)
    return {"detail": "Question deleted"}

@app.post("/questions/{id}/answers/")
def create_new_answer(answer: AnswerCreate, db: Session = Depends(get_db)):
    question = get_question(db, answer.question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return create_answer(db, answer)

@app.get("/answers/{id}")
def read_answer(id: int, db: Session = Depends(get_db)):
    answer = get_answer(db, id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer

@app.delete("/answers/{id}")
def delete_answer_endpoint(id: int, db: Session = Depends(get_db)):
    delete_answer(db, id)
    return {"detail": "Answer deleted"}
