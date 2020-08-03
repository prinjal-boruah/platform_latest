FROM python:3.6-alpine

EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev

ADD . /me_platform_s3

WORKDIR /me_platform_s3

RUN pip install -r requirements.txt

RUN python django-dashboard-atlantis-dark/manage.py makemigrations

RUN python django-dashboard-atlantis-dark/manage.py migrate

CMD [ "python", "django-dashboard-atlantis-dark/manage.py", "runserver", "0.0.0.0:8000" ]