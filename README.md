### Django + Stripe API бэкенд со следующим функционалом:

-   Django Модель Item с полями (name, description, price, image)
    
API с двумя методами:
    

-   GET  /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe выполняет запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
    
-   GET  /item/{id}, c помощью которого можно получить HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy происходит запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

Решение опубликовано чтобы его можно было быстро и легко протестировать.

https://xboxer3003.pythonanywhere.com/


Реализованы следующие бонусные задачи:

-   Запуск используя Docker
    
-   Использование environment variables
    
-   Просмотр Django Моделей в Django Admin панели


### Запуск Docker-контейнера

1. Выполнить команду:
```docker run --name dsp -it -p 8000:8000 iurij/dgango_stripe_project:v1.0```


2. Перейти по адресу:
```http://localhost:8000/```

### Запуск локально
1. Клонировать репозиторий
```git clone https://github.com/iurij-n/django_stripe.git```

2. Создать и запустить виртуальное окружение
```python -m venv venv```
```source venv/Scripts/activate```

3. Установить зависимости
```pip install -r requirements.txt```

4. Перейти в папку 'django_stripe' и выполнить миграции
```python manage.py migrate```

5. Загрузить данные в базу данных
```python manage.py loaddata db.json```

6. Создать файл .env по шаблону .env.template и добавить в него публичный и секретные ключи Stripe-API

7. Запустить сервер
```python manage.py runserver```

8. Перейти по адресу:
```http://localhost:8000/```