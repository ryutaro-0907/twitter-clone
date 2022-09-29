package controllers

import (
	docs "tweet_service/docs"

	"github.com/gin-gonic/gin"
	swaggerfiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"
)

func SetuptWebServer() *gin.Engine {
	server := gin.Default()
	server.GET("/", func(c *gin.Context) { c.String(200, "Welcome to Tweet Service API!!") })

	docs.SwaggerInfo.BasePath = "/api/v1"

	v1 := server.Group("/api/v1")
	{
		tweet := v1.Group("/tweets")
		{
			tweet.POST("", ApiCreateTweetHandler)
			tweet.GET("", ApiFetchAllTweetsHandler)
		}
	}
	server.GET("swagger/*any", ginSwagger.WrapHandler(swaggerfiles.Handler))
	return server
	// check http://localhost:8082/swagger/index.html
	// for swagger

}
