package models

import (
	"fmt"
	"log"
	"os"

	"github.com/jinzhu/gorm"
)

type CreateTweet struct {
	Username string `json:"username" binding:"required"`
	Body     string `json:"body" binding:"required"`
}
type Tweet struct {
	gorm.Model
	Username string `gorm:"size:255;not null" json:"username" binding:"required"`
	Body     string `gorm:"size:255;not null" json:"body" binding:"required"`
}

func NewTweet(input *CreateTweet) *Tweet {
	return &Tweet{
		Username: input.Username,
		Body:     input.Body,
	}
}

type TweetHandler struct {
	// db *gorm.DB
}

func NewTweetHandler() *TweetHandler {
	return &TweetHandler{}
}

// FIXME:
// USE GetDB in base.go
// This is only temporary as GetDB was throing error("can not keep up db connection")
func openDB() *gorm.DB {
	DbHost := os.Getenv("TWEET_DB_HOST")
	DbUser := os.Getenv("TWEET_DB_USER")
	DbPassword := os.Getenv("TWEET_DB_PASSWORD")
	DbName := os.Getenv("TWEET_DB_NAME")
	DbPort := os.Getenv("TWEET_DB_PORT")

	dsn := fmt.Sprint("host=", DbHost, " user=", DbUser, " password=", DbPassword, " dbname=", DbName, " port=", DbPort, " sslmode=disable")

	db, _ := gorm.Open("postgres", dsn)

	db.LogMode(true)

	return db
}

func (h *TweetHandler) CreateTweet(input *CreateTweet) (body *gorm.DB, err error) {
	log.Println("creating tweet with:", input)

	tweet := NewTweet(input)

	if err != nil {
		log.Println(err)
	}
	db := openDB()
	res := db.Create(tweet)

	// FIXME:
	// want to use this insted
	// res := h.db.Create(&Tweet{Username: "hlhlhlll", Body: "jljlfjldsaf"})

	// res := h.db.Create(&Tweet{Username: "test", Body: "test"})

	log.Println("Tweet created successfully")
	return res, nil

}

func (h *TweetHandler) FetchAllTweets() ([]Tweet, error) {
	log.Println("fetching all tweets")
	var tweets []Tweet

	db := openDB()
	db.Find(&tweets)
	// FIXME:
	// want to use this insted
	// h.db.Find(&tweets)

	// FIXME
	// do error handling here
	return tweets, nil

}
