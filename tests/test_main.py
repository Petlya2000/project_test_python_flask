import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal
import sys
import os

# Добавляем текущую директорию в пути импорта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
# Создаем тестовый клиент FastAPI
client = TestClient(app)

# Фикстура для тестовой базы данных
@pytest.fixture(scope="function")
def db_session():
    # Создаем таблицы перед каждым тестом
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        # Удаляем таблицы после каждого теста
        Base.metadata.drop_all(bind=engine)


# Тесты для вопросов (Questions)

def test_create_question():
    response = client.post("/questions/", json={"text": "What is Python?"})
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "What is Python?"
    assert "id" in data
    assert "created_at" in data


def test_get_questions():
    # Создаем тестовый вопрос
    client.post("/questions/", json={"text": "What is Python?"})

    # Проверяем список вопросов
    response = client.get("/questions/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["text"] == "What is Python?"


def test_get_question_by_id():
    # Создаем тестовый вопрос
    response = client.post("/questions/", json={"text": "What is Python?"})
    question_id = response.json()["id"]

    # Получаем вопрос по ID
    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == question_id
    assert data["text"] == "What is Python?"


def test_delete_question():
    # Создаем тестовый вопрос
    response = client.post("/questions/", json={"text": "What is Python?"})
    question_id = response.json()["id"]

    # Удаляем вопрос
    response = client.delete(f"/questions/{question_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Question deleted"}

    # Проверяем, что вопрос удален
    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 404


# Тесты для ответов (Answers)

def test_create_answer():
    # Создаем тестовый вопрос
    response = client.post("/questions/", json={"text": "What is Python?"})
    question_id = response.json()["id"]

    # Создаем ответ на вопрос
    response = client.post(f"/questions/{question_id}/answers/", json={
        "text": "Python is a programming language.",
        "user_id": "user123",
        "question_id": question_id
    })
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Python is a programming language."
    assert data["user_id"] == "user123"
    assert data["question_id"] == question_id


def test_create_answer_for_nonexistent_question():
    response = client.post("/questions/999/answers/", json={
        "text": "This should fail.",
        "user_id": "user123",
        "question_id": 999
    })
    assert response.status_code == 404
    assert response.json() == {"detail": "Question not found"}


def test_get_answer_by_id():
    # Создаем тестовый вопрос
    response = client.post("/questions/", json={"text": "What is Python?"})
    question_id = response.json()["id"]

    # Создаем ответ
    response = client.post(f"/questions/{question_id}/answers/", json={
        "text": "Python is a programming language.",
        "user_id": "user123",
        "question_id": question_id
    })
    answer_id = response.json()["id"]

    # Получаем ответ по ID
    response = client.get(f"/answers/{answer_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == answer_id
    assert data["text"] == "Python is a programming language."


def test_delete_answer():
    # Создаем тестовый вопрос
    response = client.post("/questions/", json={"text": "What is Python?"})
    question_id = response.json()["id"]

    # Создаем ответ
    response = client.post(f"/questions/{question_id}/answers/", json={
        "text": "Python is a programming language.",
        "user_id": "user123",
        "question_id": question_id
    })
    answer_id = response.json()["id"]

    # Удаляем ответ
    response = client.delete(f"/answers/{answer_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Answer deleted"}

    # Проверяем, что ответ удален
    response = client.get(f"/answers/{answer_id}")
    assert response.status_code == 404
