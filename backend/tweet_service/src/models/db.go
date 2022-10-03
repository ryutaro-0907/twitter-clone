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

func init() {
	db, err := OpenDB()
	if err != nil {
		return
	}
	db.LogMode(true)

	db.AutoMigrate(&Tweet{}) //Database migration
	db.Close()
	log.Println("Database initialzied successfully:")

}

func OpenDB() (*gorm.DB, error) {
	var (
		db  *gorm.DB
		err error
	)

	DbHost := os.Getenv("TWEET_DB_HOST")
	DbUser := os.Getenv("TWEET_DB_USER")
	DbPassword := os.Getenv("TWEET_DB_PASSWORD")
	DbName := os.Getenv("TWEET_DB_NAME")
	DbPort := os.Getenv("TWEET_DB_PORT")

	dsn := fmt.Sprint("host=", DbHost, " user=", DbUser, " password=", DbPassword, " dbname=", DbName, " port=", DbPort, " sslmode=disable TimeZone=Asia/Tokyo")

	db, err = gorm.Open("postgres", dsn)

	if err != nil {
		log.Println(err)
		return db, err
	}

	return db, nil

}
