FROM python:3.11-slim
RUN apt-get update && apt-get install -y \
    libgl1-mesa-dev \
    libglib2.0-0
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./kallia /code/kallia
CMD ["fastapi", "run", "kallia/main.py", "--port", "80"]
