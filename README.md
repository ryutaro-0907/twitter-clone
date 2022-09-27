# Twitter Clone with Python, Next.js and Nginx.



## Login Page


<img width="1440" alt="Screen Shot 2022-09-05 at 1 26 23 PM" src="https://user-images.githubusercontent.com/85374614/188360705-434dcd14-eb34-4bb4-a1eb-4e3b98ad8150.png">


## Home page 


<img width="1440" alt="Screen Shot 2022-09-05 at 1 30 56 PM" src="https://user-images.githubusercontent.com/85374614/188360816-a7e8e778-baad-4973-8b4e-0fb5b21c317e.png">


# Tecnologies

- FastApi
- Next.js
- Typescript
- Tailwind.css
- Postgres
- Docker
- Nginx


# Getting Started


## Install direnv and set up .envrc file.


```.envrc
# For google auth api
export GOOGLE_CLIENT_ID=
export GOOGLE_CLIENT_SECRET=

# For backend log 
export LOGFILE_PATH=${LOCAL_DATA_DIR}/logs/app.log
export LOCAL_DATA_DIR=./data

# DB
export DB_TYPE=postgres
export DB_USER=user  # to access the postgres database from backend
export DB_PASS=pass  # to access the postgres database from backend
export DB_ENDPOINT=192.168.0.25:5432 # to access the postgres database from backend

# for frontend to call backend api
export BASE_URL=http://nginx:8080/api 

# aws s3
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_S3_BUCKET_NAME=pythons3tutorialbucket2022
export AWS_REGION_NAME=us-east-1

```

## Run development.sh file to set up docker enviroment.


```bash
sh development.sh #to build docker environment.
```


## Then run


```bash
 docker-compose up
```


## Authors


[Email] ryutaro.furutani@gmail.com
[Twitter] @ryulovepython
[Blog] https://ryutaro.hashnode.dev/


## License


This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


# NOTE for development.


## Trabule Shooting


### Frontend Trabule Shooting


if data is not fetching from backend, please reload backend code.

```i.e.
Server Error
Error: Error serializing `.tweets` returned from `getServerSideProps` in "/".
Reason: `undefined` cannot be serialized as JSON. Please use `null` or omit this value.
```


### Backend Trabule Shooting


If backend not conncting to database, please wait and reload backend.



### Nginx Trabule Shooting


### Database Trabule Shooting


### Environment variables Trabule Shooting


# Important tips For Development


## Backend test 


```bash
docker exec -it backend sh -c "poetry run pytest"
```


## Code Formatting For Backend (PEP8)


```bash
poetry run autopep8 .
```


## Sort imports in Backend


```bash
isort --atomic .
```
