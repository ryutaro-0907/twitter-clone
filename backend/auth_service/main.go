package main

import (
	"log"

	"auth_service/app/controllers"
	"auth_service/app/utils"
	docs "auth_service/docs"

	"github.com/gin-gonic/gin"
	swaggerfiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"
)

func main() {
	utils.LoggingSettings("auth_service.log")
	log.Println("starting auth service...")

	controllers.InitializeDb()

	r := gin.Default()
	docs.SwaggerInfo.BasePath = "/api/v1"
	v1 := r.Group("/api/v1")
	{
		auth := v1.Group("/auth")
		{
			auth.POST("/register", controllers.Register)
			auth.POST("/login", controllers.Login)
		}
	}
	protected := r.Group("/api/admin")
	protected.Use(utils.JwtAuthMiddleware())
	protected.GET("/user", controllers.CurrentUser)

	r.GET("/swagger/*any", ginSwagger.WrapHandler(swaggerfiles.Handler))
	// http://localhost:8081/swagger/index.html

	r.Run(":8081")

}
