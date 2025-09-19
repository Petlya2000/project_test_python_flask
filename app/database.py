from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Получаем параметры подключения из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/test_db")

# Создаем движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# Создаем сессию для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()
