
postgres: 
	docker run --name recipes-postgres  -p 5432:5432  -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=secret -d postgres:12-alpine 

db: 
	docker exec -it recipes-postgres psql -U postgres -c "CREATE DATABASE recipes"

env:
	source env/bin/activate

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

test:
	python manage.py test

server: 
	python manage.py runserver

.PHONY: postgres db env migrations migrate test server migrate_zero