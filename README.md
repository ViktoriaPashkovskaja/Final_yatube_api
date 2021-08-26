#api_final_yatube
##Проект: api_yatube
***
##О проекте
API для проекта Yatube.

Авторизация по JWT токену

Сериализация данных для моделей проекта (Post, Comment, Group, Follow)

Обработка GET, POST, PATCH, PUT и DELETE запросов к базе данных проекта Yatube
***

###Для запуска проекта установите виртуальное окружение:
```
python -m venv venv

```
###Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/yandex-praktikum/kittygram.git
cd kittygram
```

###Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
###Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

###Выполнить миграции:
```
python3 manage.py migrate
```

###Запустить проект:
```
python3 manage.py runserver
```
***
##Примеры запросов к API

###Пример запроса

```
http://127.0.0.1:8000/api/v1/posts/
```
###Пример ответа
```
[
    {
        "id": 1,
        "author": "Sergey",
        "text": "Привет, мир!",
        "pub_date": "2020-08-24T14:15:22Z",
        "image": "photo.png",
        "group": 2
    }
]
```
###Пример запроса

```
http://127.0.0.1:8000/api/v1/follow/
```
###Пример ответа
```
[
    {
        "user": "Matvey",
        "following": "Sergey"
    }
]
```