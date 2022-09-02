# Twitter Clone with Python, Next.js and Nginx.

## Tecnologies
- FastApi
- Next.js
- Typescript
- Tailwind.css
- Postgres
- Docker
- Nginx

## Getting Started

### Install direnv and set up .envrc file.
``` .envrc
    <!-- For next auth  -->
    export GOOGLE_CLIENT_ID=
    export GOOGLE_CLIENT_SECRET=

    export NEXTAUTH_URL=http://0.0.0.0:3000/
    export NEXTAUTH_SECRET=codeforfun

    export NEXT_PUBLIC_BASE_URL=http://0.0.0.0:3000/

    <!-- For backend logging-->
    export LOGFILE_PATH=${LOCAL_DATA_DIR}/logs/app.log

    <!-- For db -->
    export LOCAL_DATA_DIR=./data

    export DB_TYPE=postgres
    export DB_USER=user  # to access the postgres database from backend
    export DB_PASS=pass  # to access the postgres database from backend
    export DB_ENDPOINT=192.168.0.16:5432 # to access the postgres database from backend

    <!-- For frontend -->
    # export BASE_URL=http://nginx:8080/api # for frontend to call backend api
```

``` bash
sh development.sh #to build docker environment.
```

Then run
``` bash
 docker-compose up
```

## Authors

ryutaro.furutani@gmail.com
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## NOTE for development.
### Frontend
if data is not fetching from backend, please reload backend code.

``` i.e.
Server Error
Error: Error serializing `.tweets` returned from `getServerSideProps` in "/".
Reason: `undefined` cannot be serialized as JSON. Please use `null` or omit this value.
```
### Backend
If backend not conncting to database, please wait and reload backend.

### Nginx

### Database

### Environment variables
=======
# twitter-colne

# Set up

# Install direnv and crate .envrc file in your root directory as follows
```
export GOOGLE_CLIENT_ID=
export GOOGLE_CLIENT_SECRET=

export NEXTAUTH_URL=http://localhost:3000/
<!-- any secret is fine. -->
export NEXTAUTH_SECRET=codeforfun

export NEXT_PUBLIC_SANITY_DATASET=production
export NEXT_PUBLIC_SANITY_PROJECT_ID=
export NEXT_PUBLIC_BASE_URL=http://localhost:3000/
export SANITY_API_TOKEN=
```

## Note:
You need to have an access to Sanity and google API to use some backend processes.

# After you set up
## Run for dev
```
npm install
npm run dev
```
