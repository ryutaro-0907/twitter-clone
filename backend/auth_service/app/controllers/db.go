package controllers

import "auth_service/app/models"

func InitializeDb() {
	models.Initialize()
}

func CloseDb() {
	models.CloseDB()
}
