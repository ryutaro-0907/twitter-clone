package controllers

import (
	"net/http"

	"tweet_service/src/models"

	"github.com/gin-gonic/gin"
)

// @BasePath /api/v1

// Create Tweet endpoint godoc
// @Summary Create Tweet Endpoint
// @Schemes
// @Description Create Tweet
// @Tags tweet
// @Accept json
// @Produce json
// @Param models.CreateTweet body models.CreateTweet true "Create Tweett"
// @Success 200 {string} tweets
// @Router /tweets [post]
func ApiCreateTweetHandler(c *gin.Context) {

	var input models.CreateTweet

	if err := c.ShouldBindJSON(&input); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	db, err := models.OpenDB()
	if err != nil {
		return
	}

	handler := models.NewTweetHandler(db)

	tweets, err := handler.CreateTweet(&input)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "could not create tweet."})
		return
	} else {
		c.JSON(http.StatusOK, gin.H{"body": tweets})
	}
}

// @BasePath /api/v1

// Fetch Tweets endpoint godoc
// @Summary Fetch Tweets Endpoint
// @Schemes
// @Description Fetch Tweets
// @Tags tweet
// @Accept json
// @Produce json
// @Success 200 {string} body
// @Router /tweets [get]
func ApiFetchAllTweetsHandler(c *gin.Context) {

	db, err := models.OpenDB()
	if err != nil {
		return
	}

	handler := models.NewTweetHandler(db)

	tweets, err := handler.FetchAllTweets()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "could not fetch tweets."})
		return
	} else {
		c.JSON(http.StatusOK, tweets)
	}
}
