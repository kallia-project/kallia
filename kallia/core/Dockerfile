FROM python:3.11-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./kallia_core /code/kallia_core
CMD ["fastapi", "run", "kallia_core/main.py", "--port", "80"]
