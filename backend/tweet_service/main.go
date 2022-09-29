package main

import (
	"log"

	"tweet_service/src/controllers"
	"tweet_service/src/utils"
)

func main() {

	utils.LoggingSettings("tweet_service.log")
	log.Println("starting tweet service...")

	// Initialize database (migrate Tweet model)
	controllers.InitDB()

	// Start Server
	controllers.StartWebServer()

}
