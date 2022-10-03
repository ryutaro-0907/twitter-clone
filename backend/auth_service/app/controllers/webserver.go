package controllers

import (
	"log"

	"auth_service/app/utils"
	docs "auth_service/docs"

	"github.com/gin-gonic/gin"
	swaggerfiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"
)

func SetuptWebServer() *gin.Engine {
	log.Println("starting auth service...")

	server := gin.Default()
	server.Use(utils.CORSMiddleware())

	docs.SwaggerInfo.BasePath = "/api/v1"
	v1 := server.Group("/api/v1")
	{
		auth := v1.Group("/auth")
		{
			auth.POST("/register", Register)
			auth.POST("/login", Login)
		}
	}
	protected := server.Group("/api/admin")
	protected.Use(utils.JwtAuthMiddleware())
	protected.GET("/user", CurrentUser)

	server.GET("/swagger/*any", ginSwagger.WrapHandler(swaggerfiles.Handler))
	// http://localhost:8081/swagger/index.html

	return server
}
