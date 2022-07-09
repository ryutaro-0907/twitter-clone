docker-compose build
docker-compose run --rm --entrypoint "poetry install" backend
docker-compose up