FROM golang:1.19-alpine

RUN apk update && apk add --no-cache git

ENV GO111MODULE=on

WORKDIR /app
COPY go.mod .
COPY go.sum .

RUN go install github.com/pilu/fresh@latest
RUN go mod download

COPY . .

EXPOSE 8081

ENTRYPOINT ["fresh"]
