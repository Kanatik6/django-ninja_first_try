FROM python:3.11-slim

WORKDIR /app

# Установить uv
RUN pip install uv

# Копировать зависимости
COPY requirements.txt .
RUN uv pip install --system -r requirements.txt

# Копировать проект
COPY . .

# Собрать статику
RUN python manage.py collectstatic --noinput || true

# Открыть порт
EXPOSE 8000

# Запустить сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]