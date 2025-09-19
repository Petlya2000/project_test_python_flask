# crud.py
from sqlalchemy.orm import Session
from app.models import Question, Answer
from app.schemas import QuestionCreate, AnswerCreate

def get_questions(db: Session):
    return db.query(Question).all()

def create_question(db: Session, question: QuestionCreate):
    db_question = Question(text=question.text, created_at=datetime.utcnow())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_question(db: Session, question_id: int):
    return db.query(Question).filter(Question.id == question_id).first()

def delete_question(db: Session, question_id: int):
    db_question = get_question(db, question_id)
    if db_question:
        db.delete(db_question)
        db.commit()

def create_answer(db: Session, answer: AnswerCreate):
    db_answer = Answer(
        text=answer.text,
        user_id=answer.user_id,
        question_id=answer.question_id,
        created_at=datetime.utcnow()
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

def get_answer(db: Session, answer_id: int):
    return db.query(Answer).filter(Answer.id == answer_id).first()

def delete_answer(db: Session, answer_id: int):
    db_answer = get_answer(db, answer_id)
    if db_answer:
        db.delete(db_answer)
        db.commit()
