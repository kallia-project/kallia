FROM python:3.11-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./kallia-playground /code/kallia-playground
CMD ["chainlit", "run", "kallia-playground/main.py", "--host", "0.0.0.0", "--port", "80"]
