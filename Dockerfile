FROM python:3

ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
CMD python django_backend/manage.py runserver 0.0.0.0:8046
