# Биржа Услуг

Веб-сайт "Биржа Услуг" позволяет размещать зарегистрированным пользователям информацию о
предоставляемых ими услугах и выступать в качестве исполнителей, или заказывать услуги у других
пользователей. Заказчики могут размещать сведения о своих проектах, а исполнители – предлагать свои услуги для
их реализации.

## Используемые библиотеки и инструменты

- [Django](https://docs.djangoproject.com/)
    - [django-allauth](https://pypi.org/project/django-allauth/): Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
    - [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/): Best debugging tool for Django.
- Оформление:
  - [Tailwind CSS](https://tailwindcss.com/)
  - [crispy-tailwind](https://django-crispy-forms.github.io/crispy-tailwind/getting_started.html#installation)
- Прочее:
  - [environs](https://pypi.org/project/environs/): `environs` is a Python library for parsing environment variables. 


## Запуск приложения

### В режиме разработки

Создать файл `src/.env` со следущими параметрами:

```bash
SECRET_KEY="long-random-string"
DEBUG=True
```

#### Запуск в докере

```bash
make dev_up
# или
docker compose -f docker-compose.dev.yml up
# Применить миграции
docker exec -it web python -m manage migrate
# Создать суперпользователя
docker exec -it web python -m manage createsuperuser
# Остановить
docker compose -f docker-compose.dev.yml down
```

Приложение будет доступно по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
