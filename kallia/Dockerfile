FROM python:3.11-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./kallia /code/kallia
CMD ["fastapi", "run", "kallia/main.py", "--port", "80"]
