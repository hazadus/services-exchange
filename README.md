# Биржа Услуг

Веб-сайт "Биржа Услуг" позволяет размещать зарегистрированным пользователям информацию о
предоставляемых ими услугах и выступать в качестве исполнителей, или заказывать услуги у других
пользователей. Заказчики могут размещать сведения о своих проектах, а исполнители – предлагать свои услуги для
их реализации.

Сайт запущен для демонстрации на [http://exchange.amgold.ru/](http://exchange.amgold.ru/).

![Screen1](images/screen1.png)

## Реализованные фичи

- Регистрация, аутентификация пользователей.
- Пользователи могут указывать о себе дополнительные сведения – имя, изображение профиля, специальность, навыки, подробности об опыте, и др.
- В публичном профиле пользователя видна вся информация о нём, а также список его услуг и проектов.
- Создание, редактирование, удаление услуг пользователей.
- Просмотр списка услуг, с разбивкой по категориям, поиск по услугам.
- Создание, редактирование, удаление проектов пользователей.
- Просмотр списка услуг, с разбивкой по категориям, поиск по проектам.
- Страницы со списком услуг, проектов, заказов пользователя.
- Пользователи могут предлагать свои услуги по выполнению проекта, а заказчик может отклонить или принять предложения.
- Желающие могут создать заказ на представленную в каталоге услугу. Исполнитель может отклонить заказ, или взяться за его выполнение. С баланса заказчика снимается стоимость работы, которая при подтверждении выполнения заказчиком начисляется исполнителю.
- Пользователи могут отправлять друг другу сообщения на странице каждого заказа, при желании – прикреплять к сообщениям файлы.
- Пополнение баланса пользователя при помощи Celery Task.
- Аккуратная верстка с Tailwind CSS позволяет легко преобразить оформление страниц.
- Конечно же, прекрасная админ-панель Django на месте!
- Подключен Sentry.
- Настроен CI/CD на GitHub.

## Используемые библиотеки и инструменты

- [Django](https://docs.djangoproject.com/)
    - [django-allauth](https://pypi.org/project/django-allauth/): Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
    - [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/): Best debugging tool for Django.
- [Celery](https://docs.celeryq.dev/en/stable/index.html): simple, flexible, and reliable distributed system to process vast amounts of messages, while providing operations with the tools required to maintain such a system.
- [redis-py](https://github.com/redis/redis-py): Redis Python client.
- Тесты
  - [factory-boy](https://factoryboy.readthedocs.io/en/stable/recipes.html)
  - [Faker](https://faker.readthedocs.io/en/master/)
- Оформление:
  - [Tailwind CSS](https://tailwindcss.com/)
  - [crispy-tailwind](https://django-crispy-forms.github.io/crispy-tailwind/getting_started.html#installation)
- Прочее:
  - [environs](https://pypi.org/project/environs/): `environs` is a Python library for parsing environment variables. 


## Запуск приложения

Создать файл `src/.env` со следущими параметрами:

```bash
SECRET_KEY="long-random-string"
# Опционально для запуска на сервере – Sentry DSN:
SENTRY_DSN="sentry-dsn-..."
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
