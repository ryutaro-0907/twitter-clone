docker-compose build
docker-compose run --rm --entrypoint "poetry install" backend
docker-compose run --rm --entrypoint "npm install" frontend

# docker-compose up