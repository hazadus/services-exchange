runserver:
	python src/manage.py runserver
format:
	ruff check . -n --select I --fix
css:
	npx tailwindcss -i ./src/static/src/input.css -o ./src/static/styles.css
prepare:
	make format
	make css
dev_up:
	docker compose -f docker-compose.dev.yml up
dev_down:
	docker compose -f docker-compose.dev.yml down