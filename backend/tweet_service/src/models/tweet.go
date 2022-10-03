package models

import (
	"log"

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
	db *gorm.DB
}

func NewTweetHandler(db *gorm.DB) *TweetHandler {
	return &TweetHandler{db: db}
}

func (h *TweetHandler) CreateTweet(input *CreateTweet) (*Tweet, error) {
	log.Println("creating tweet with:", input)
	t := &Tweet{
		Username: input.Username,
		Body:     input.Body,
	}

	if res := h.db.Create(&t); res.Error != nil {
		return t, res.Error
	}

	log.Println("Tweet created successfully")
	return t, nil

}

func (h *TweetHandler) FetchAllTweets() ([]Tweet, error) {
	log.Println("fetching all tweets")
	var tweets []Tweet

	if res := h.db.Find(&tweets); res.Error != nil {
		return tweets, res.Error
	}

	return tweets, nil

}
