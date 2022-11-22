FROM python:3.7-slim
RUN mkdir /app
COPY requirements.txt /app
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY . /app
WORKDIR /app
CMD ["python3", "django_stripe/manage.py", "runserver", "0:8000"]
LABEL author='Iurij Nonikov' email='iurij.novickov2016@yandex.ru' version=1 data='22.11.2022'