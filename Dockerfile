FROM python:3.10

WORKDIR /app

# Скопировать весь проект в контейнер
COPY . .

# Установить зависимости из текущей среды
RUN pip install fastapi uvicorn sqlalchemy psycopg2 alembic

# Команда для запуска приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]