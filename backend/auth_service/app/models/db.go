package models

import (
	"fmt"
	"log"
	"os"

	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
)

var db *gorm.DB

func Initialize() {

	DbHost := os.Getenv("AUTH_DB_HOST")
	DbUser := os.Getenv("AUTH_DB_USER")
	DbPassword := os.Getenv("AUTH_DB_PASSWORD")
	DbName := os.Getenv("AUTH_DB_NAME")
	DbPort := os.Getenv("AUTH_DB_PORT")

	dsn := fmt.Sprint("host=", DbHost, " user=", DbUser, " password=", DbPassword, " dbname=", DbName, " port=", DbPort, " sslmode=disable TimeZone=Asia/Japan")

	conn, err := gorm.Open("postgres", dsn)

	if err != nil {
		log.Println(err)
	}

	db = conn

	db.LogMode(true)

	db.AutoMigrate(&User{}) //Database migration
	log.Println("Database started successfully:")
}

//returns a handle to the DB object
func GetDB() *gorm.DB {
	return db
}

func CloseDB() {
	db.Close()
}
