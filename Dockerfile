FROM python:3

RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt 

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
