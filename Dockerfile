FROM python:3.10-slim-bullseye
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
WORKDIR /backend

# install dependecies for postgres
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

COPY requirements.txt /backend/
RUN pip install -r requirements.txt

EXPOSE 8000

COPY . /backend/
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
