# project_test_python_flask

Основные технологии, используемые в проекте:
- Python, Django, Flask
- PostgreSQL
- Docker]

## Структура проекта

- `app/` — исходный код приложения.
- `docker-compose.yml` — файл конфигурации Docker Compose для запуска проекта.
- `README.md` — документация проекта.
- `test/` — папка с тестами.

## Требования

Для запуска проекта вам потребуется:
- Установленный Docker (https://www.docker.com/)
- Установленный Docker Compose (обычно идет в комплекте с Docker)

## Установка и запуск

Следуйте этим шагам, чтобы запустить проект:

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/username/project-name.git
   cd project-name
2. Запустите проект с помощью Docker Compose:

docker-compose up
Docker Compose автоматически создаст и запустит все необходимые контейнеры.

3. Доступ к приложению: 
После успешного запуска приложение будет доступно по адресу:

http://localhost:8000

Страница работы с вопросами 

http://localhost:8000/docs


4. Остановка проекта

Чтобы остановить проект, выполните команду:


docker-compose down

5. Проверка

Для проверки работы контейнеров используйте следующие команды.

docker-compose logs app

docker-compose logs db

6. Тестирование

Для выполнения тестов выполните команду для их запуска:

pytest tests/
