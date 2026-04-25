FROM python:3.11-slim

WORKDIR /code

COPY ./dockerfile/fastapi/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./backend /code/backend


CMD ["uvicorn", "main:backend", "--host", "0.0.0.0", "--port", "10000"]