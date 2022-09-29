package controllers

import (
	"fmt"
	"log"
	"net/http"
	"os"

	docs "tweet_service/docs"
	"tweet_service/src/models"

	"github.com/gin-gonic/gin"
	swaggerfiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"
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
// @Success 200 {string} body
// @Router /tweets [post]
func ApiCreateTweetHandler(c *gin.Context) {

	var input models.CreateTweet

	if err := c.ShouldBindJSON(&input); err != nil {
		log.Println(err)
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	handler := models.NewTweetHandler()

	body, err := handler.CreateTweet(&input)

	if err != nil {
		log.Println("error crateing tweet: ", err)
		c.JSON(http.StatusBadRequest, gin.H{"error": "could not create tweet."})
		return
	} else {
		log.Println(gin.H{"status": http.StatusOK, "message": "tweet successfully created."})
		c.JSON(http.StatusOK, gin.H{"body": body})
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

	handler := models.NewTweetHandler()

	tweets, err := handler.FetchAllTweets()

	if err != nil {
		log.Println("error fetching tweet: ", err)
		c.JSON(http.StatusBadRequest, gin.H{"error": "could not fetch tweets."})
		return
	} else {
		c.JSON(http.StatusOK, gin.H{"message": "tweet successfully fetched.", "tweets": tweets})
	}
}

func StartWebServer() error {
	server := gin.Default()
	server.GET("/", func(c *gin.Context) { c.String(200, "Welcome to Tweet Service API!!") })

	docs.SwaggerInfo.BasePath = "/api/v1"

	port := fmt.Sprint(":", os.Getenv("TWEET_SERVICE_PORT"), "")

	v1 := server.Group("/api/v1")
	{
		tweet := v1.Group("/tweets")
		{
			tweet.POST("", ApiCreateTweetHandler)
			tweet.GET("", ApiFetchAllTweetsHandler)
		}
	}
	server.GET("swagger/*any", ginSwagger.WrapHandler(swaggerfiles.Handler))
	return server.Run(port)
	// check http://localhost:8082/swagger/index.html
	// for swagger

}
