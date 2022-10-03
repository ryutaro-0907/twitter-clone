package main

import (
	"auth_service/app/controllers"
	"auth_service/app/utils"
	"fmt"
	"os"
)

func main() {
	utils.LoggingSettings("auth_service.log")
	port := fmt.Sprint(":", os.Getenv("AUTH_SERVICE_PORT"), "")

	// Start Server
	server := controllers.SetuptWebServer()
	server.Run(port)

}
