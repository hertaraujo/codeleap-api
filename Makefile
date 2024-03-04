.PHONY:install
install:
	poetry install;

.PHONY:run
run:
	poetry run python manage.py runserver

.PHONY:migrations
migrations:
	poetry run python manage.py makemigrations
	
.PHONY:migrate
migrate:
	poetry run python manage.py migrate
	
.PHONY:lint
lint:
	poetry run ruff check .; poetry run ruff format .
