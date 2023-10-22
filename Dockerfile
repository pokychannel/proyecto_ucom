FROM python:3.8-alpine

ENV DEBUG=True
ENV SECRET_KEY="django-insecure-8uo7!9n^t3pq=zw2&2w)90u(fuvk-3tl(am+^u0w=v3yiiz(!y"
ENV DATABASE="Hospital-django"
ENV USER_DB="postgres"
ENV PASS_DB=12345
ENV HOST_DB="localhost"
ENV PORT_DB="5423"

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install pipenv
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev
RUN pip install -r requirements.txt

WORKDIR /app

COPY . .

EXPOSE 8088

ENTRYPOINT python manage.py runserver 0.0.0.0:8088