package models

import (
	"fmt"
	"log"
	"os"

	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
)

var (
	Db  *gorm.DB
	err error
)

func InitDB() {
	DbHost := os.Getenv("TWEET_DB_HOST")
	DbUser := os.Getenv("TWEET_DB_USER")
	DbPassword := os.Getenv("TWEET_DB_PASSWORD")
	DbName := os.Getenv("TWEET_DB_NAME")
	DbPort := os.Getenv("TWEET_DB_PORT")

	dsn := fmt.Sprint("host=", DbHost, " user=", DbUser, " password=", DbPassword, " dbname=", DbName, " port=", DbPort, " sslmode=disable TimeZone=Asia/Japan")

	Db, err = gorm.Open("postgres", dsn)

	if err != nil {
		log.Println(err)
	}

	Db.LogMode(true)

	Db.AutoMigrate(&Tweet{}) //Database migration
	log.Println("Migration is processed successfully:")

	log.Println("Database started successfully:")
}

func GetDB() *gorm.DB {
	return Db
}

func Close() {
	if err := Db.Close(); err != nil {
		panic(err)
	}
}
