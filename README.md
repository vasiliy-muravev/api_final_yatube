# Yatube API Final

Финальная версия проекта Yatube API предоставляет интерфейс для взаимодействия с моделями постов, комментариев, групп и подписчиков Yatube. Этот проект реализован с использованием Django и Django REST Framework. 

### Цепочка проектов Blogicum
[api_yatube](https://github.com/vasiliy-muravev/api_yatube "api_yatube")

**[api_final_yatube](https://github.com/vasiliy-muravev/api_final_yatube "api_final_yatube")** &#8592; вы тут

### Фреймворки и библиотеки

* **Django** : Высокоуровневый веб-фреймворк для быстрой разработки и чистого, прагматичного дизайна. Он предоставляет мощные инструменты и библиотеки для разработки веб-приложений.
* **Django REST Framework (DRF)** : Набор инструментов для построения веб-API на основе Django. DRF предоставляет мощные и гибкие инструменты для создания API, такие как сериализация данных, аутентификация и разрешения.

### Аутентификация

* **Django Rest Framework JWT Authentication**: В отличие от встроенной схемы TokenAuthentication, аутентификация JWT не требует использования базы данных для проверки токена. Пакет для аутентификации JWT — djangorestframework-simplejwt, который предоставляет некоторые функции, а также подключаемое приложение черного списка токенов.

### Инструкция по запуску проекта (Linux)
**1. Клонирование с Github.**

В локальную директорию клонируйте проект
```
git clone git@github.com:vasiliy-muravev/api_final_yatube.git
```
**2. Создание окружения.**

В корневой папке проекта создайте и активируйте виртуальное окружение
```
python3 -m venv venv
source venv/bin/activate
```

**3. Обновление pip и установка зависимостей.**
 
Находясь в корневой папке проекта, выполните команду
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Эндпоинты

* `POST /api/v1/jwt/create/`: Получить токен аутентификации. Отправьте свои `username` и `password`.
* `GET /api/v1/posts/`: Получить список всех постов.
* `POST /api/v1/posts/`: Создать новый пост.
* `GET /api/v1/posts/{post_id}/`: Получить подробную информацию о посте.
* `PUT /api/v1/posts/{post_id}/`: Полностью обновить пост.
* `PATCH /api/v1/posts/{post_id}/`: Частично обновить пост.
* `DELETE /api/v1/posts/{post_id}/`: Удалить пост.
* `GET /api/v1/groups/`: Получить список всех групп.
* `GET /api/v1/groups/{group_id}/`: Получить информацию о группе.
* `GET /api/v1/posts/{post_id}/comments/`: Получить список всех комментариев к посту.
* `POST /api/v1/posts/{post_id}/comments/`: Создать новый комментарий к посту.
* `GET /api/v1/posts/{post_id}/comments/{comment_id}/`: Получить информацию о комментарии.
* `PUT /api/v1/posts/{post_id}/comments/{comment_id}/`: Полностью обновить комментарий.
* `PATCH /api/v1/posts/{post_id}/comments/{comment_id}/`: Частично обновить комментарий.
* `DELETE /api/v1/posts/{post_id}/comments/{comment_id}/`: Удалить комментарий.
* `GET /api/v1/follow/`: Получить подписчиков текущего пользователя.
* `POST /api/v1/follow/`: Подписаться на пользователя.

### Как работать с коллекцией?
Прежде чем начать работу с коллекцией — подготовьте Django-проект:
* Проверьте, что виртуальное окружение развёрнуто и активировано, зависимости проекта установлены.
* Перейдите в директорию postman_collection и командой bash `set_up_data.sh` запустите bash-скрипт для создания необходимых для работы коллекции объектов в базе данных.