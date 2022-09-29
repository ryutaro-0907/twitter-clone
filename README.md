# Twitter Clone with Go, React.js.



## Login Page


<img width="1440" alt="Screen Shot 2022-09-05 at 1 26 23 PM" src="https://user-images.githubusercontent.com/85374614/188360705-434dcd14-eb34-4bb4-a1eb-4e3b98ad8150.png">


## Home page 


<img width="1440" alt="Screen Shot 2022-09-05 at 1 30 56 PM" src="https://user-images.githubusercontent.com/85374614/188360816-a7e8e778-baad-4973-8b4e-0fb5b21c317e.png">

## Authentification Service Swagger


<img width="1440" alt="Screen Shot 2022-09-30 at 8 35 51 AM" src="https://user-images.githubusercontent.com/85374614/193160158-d8ed80c3-05d1-4e7e-ab7f-ddcafcbad3be.png">

## Tweet Service Swagger


<img width="1440" alt="Screen Shot 2022-09-30 at 8 35 07 AM" src="https://user-images.githubusercontent.com/85374614/193160096-f8c5963e-669e-4729-8f07-45e1a47977ed.png">


# Tecnologies

- Gin
- Next.js
- Typescript
- Tailwind.css
- Postgres
- Docker


# Getting Started


## Install direnv and set up .envrc file.


```.envrc
# Auth Service
export AUTH_DB_HOST=192.168.0.2
export AUTH_DB_DRIVER=postgres
export AUTH_DB_USER=root
export AUTH_DB_PASSWORD=root
export AUTH_DB_NAME=auth_service_db
export AUTH_DB_PORT=5432
export AUTH_DB_ENDPOINT=192.168.0.25:${AUTH_DB_PORT}

export AUTH_LOCAL_DATA_DIR=./backend/auth_service/data
export AUTH_LOGFILE_PATH=${AUTH_LOCAL_DATA_DIR}/logs/app.log

export AUTH_API_SECRET=ssss
export AUTH_TOKEN_HOUR_LIFESPAN=1


# Tweet Service
export TWEET_SERVICE_PORT=8082

export TWEET_DB_HOST=192.168.0.25
export TWEET_DB_DRIVER=postgres
export TWEET_DB_USER=root
export TWEET_DB_PASSWORD=root
export TWEET_DB_NAME=tweet_service_db
export TWEET_DB_PORT=5433
export TWEET_DB_ENDPOINT=192.168.0.25:${TWEET_DB_PORT}

export TWEET_LOCAL_DATA_DIR=./backend/tweet_service/data
export TWEET_LOGFILE_PATH=${TWEET_LOCAL_DATA_DIR}/logs/app.log

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



