FROM python:3.7-slim
RUN mkdir /app
COPY requirements.txt /app
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt --no-cache-dir
WORKDIR /app/django_stripe
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py loaddata db.json
ENV STRIPE_PUBLIC_KEY pk_test_51M5uagFXiDYe7Pq77WqHHODnyzBF7RqpBOfD0URcReNMtC6GSNR50AzEmq2LeVdqUGbD2nPcveNv0ybbZL5ZzYuO000JobpvrJ
ENV STRIPE_SECRET_KEY sk_test_51M5uagFXiDYe7Pq7YMLy1yO1HS0Rt5AwxK2jtTUqyZh6YRJ1FTukYMwPDApSMJPka9PDC1qq6d2HO2OxIntTCukt00wOVIPLwO
CMD ["python3", "manage.py", "runserver", "0:8000"]
LABEL author='Iurij Nonikov' email='iurij.novickov2016@yandex.ru' version=1 data='22.11.2022'