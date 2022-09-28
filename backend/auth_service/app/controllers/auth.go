package controllers

import (
	"log"

	"auth_service/app/models"
	"auth_service/app/utils"
	"net/http"

	"github.com/gin-gonic/gin"
)

func CurrentUser(c *gin.Context) {

	user_id, err := utils.ExtractTokenID(c)

	if err != nil {
		log.Println(err)
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	handler := models.AuthHandler{
		models.GetDB(),
	}
	u, err := handler.GetUserByID(user_id)

	if err != nil {
		log.Fatal(err)
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": "success", "data": u})
}

// @BasePath /api/v1

// Login endpoint godoc
// @Summary User Login Endpoint
// @Schemes
// @Description login user
// @Tags auth
// @Accept json
// @Produce json
// @Param loginInput body LoginInput true "Add Login input"
// @Success 200 {string} token
// @Router /auth/login [post]
func Login(c *gin.Context) {

	var input models.LoginInput

	if err := c.ShouldBindJSON(&input); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	u := models.User{}

	if input.Username == "" {
		log.Println("input username is required")
		c.JSON(http.StatusBadRequest, gin.H{"error": "input username is empty"})
	}

	if input.Password == "" {
		log.Println("input password is required")
		c.JSON(http.StatusBadRequest, gin.H{"error": "input password is empty"})
	}

	u.Username = input.Username
	u.Password = input.Password

	handler := models.AuthHandler{
		Db: models.GetDB(),
	}

	token, err := handler.LoginCheck(input.Username, input.Password)

	if err != nil {
		log.Println(err)
		c.JSON(http.StatusBadRequest, gin.H{"error": "username or password is incorrect."})
		return
	} else {
		log.Println(gin.H{"status": http.StatusOK, "message": "token successfully generated."})
		c.JSON(http.StatusOK, gin.H{"token": token})
	}
}

// @BasePath /api/v1
// Register endpoint godoc
// @Summary User Register Endpoint
// @Schemes
// @Description register user
// @Tags auth
// @Accept json
// @Produce json
// @Param registerInput  body RegisterInput true "Add register input"
// @Success 200 {map} message
// @Router /auth/register [post]
func Register(c *gin.Context) {
	log.Println("registering user")

	var input models.RegisterInput
	log.Println("define input")

	if err := c.ShouldBindJSON(&input); err != nil {
		log.Println(err)
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	log.Println("insert value to User model")

	log.Println("saving user")

	handler := models.AuthHandler{
		Db: models.GetDB(),
	}

	_, err := handler.SaveUser(&input)

	if err != nil {
		log.Println(err)
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	log.Println("user saved")

	c.JSON(http.StatusOK, gin.H{"message": "registration success"})

}
