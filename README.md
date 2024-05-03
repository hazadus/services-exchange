# Биржа Услуг

Веб-сайт "Биржа Услуг" позволяет размещать зарегистрированным пользователям информацию о
предоставляемых ими услугах и выступать в качестве исполнителей, или заказывать услуги у других
пользователей. Заказчики могут размещать сведения о своих проектах, а исполнители – предлагать свои услуги для
их реализации.

## Используемые библиотеки и инструменты

- [Django](https://docs.djangoproject.com/)
    - [django-allauth](https://pypi.org/project/django-allauth/): Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
    - [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/): Best debugging tool for Django.
- [Celery](https://docs.celeryq.dev/en/stable/index.html): simple, flexible, and reliable distributed system to process vast amounts of messages, while providing operations with the tools required to maintain such a system.
- [redis-py](https://github.com/redis/redis-py): Redis Python client.
- Оформление:
  - [Tailwind CSS](https://tailwindcss.com/)
  - [crispy-tailwind](https://django-crispy-forms.github.io/crispy-tailwind/getting_started.html#installation)
- Прочее:
  - [environs](https://pypi.org/project/environs/): `environs` is a Python library for parsing environment variables. 


## Запуск приложения

Создать файл `src/.env` со следущими параметрами:

```bash
SECRET_KEY="long-random-string"
```

### Запуск в режиме разработки

```bash
make dev_up
# или
docker compose -f docker-compose.dev.yml up
# Применить миграции
docker exec -it web python -m manage migrate
# Создать суперпользователя
docker exec -it web python -m manage createsuperuser
# Загрузить фикстуры категорий
docker exec -it web python -m manage loaddata exchange/fixtures/categories.json
# Остановить
docker compose -f docker-compose.dev.yml down
```

Приложение будет доступно по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Запуск на сервере

```bash
docker compose up -d --build
# Применить миграции
docker exec -it web python -m manage migrate
# Создать суперпользователя
docker exec -it web python -m manage createsuperuser
# Загрузить фикстуры категорий
docker exec -it web python -m manage loaddata exchange/fixtures/categories.json
# Создать статические файлы
docker exec web python manage.py collectstatic --noinput
# Остановить
docker compose down
```
