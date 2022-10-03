package main

import (
	"fmt"
	"log"
	"os"

	"tweet_service/src/controllers"
	"tweet_service/src/utils"
)

func main() {

	utils.LoggingSettings("tweet_service.log")
	log.Println("starting tweet service...")

	port := fmt.Sprint(":", os.Getenv("TWEET_SERVICE_PORT"), "")

	// Start Server
	server := controllers.SetuptWebServer()
	server.Run(port)

}
