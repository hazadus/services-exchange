runserver:
	python src/manage.py runserver
format:
	ruff check . -n --select I --fix