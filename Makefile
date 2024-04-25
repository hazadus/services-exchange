runserver:
	python src/manage.py runserver
format:
	ruff check . -n --select I --fix
dev_up:
	docker compose -f docker-compose.dev.yml up
dev_down:
	docker compose -f docker-compose.dev.yml down