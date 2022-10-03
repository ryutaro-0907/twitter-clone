package controllers

import (
	"auth_service/app/models"
	"auth_service/app/utils"
	"net/http"

	"github.com/gin-gonic/gin"
)

func CurrentUser(c *gin.Context) {

	user_id, err := utils.ExtractTokenID(c)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	db, err := models.OpenDB()
	if err != nil {
		return
	}

	handler := models.AuthHandler{
		db,
	}
	u, err := handler.GetUserByID(user_id)

	if err != nil {
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
		c.JSON(http.StatusBadRequest, gin.H{"error": "input username is empty"})
	}

	if input.Password == "" {
		c.JSON(http.StatusBadRequest, gin.H{"error": "input password is empty"})
	}

	u.Username = input.Username
	u.Password = input.Password

	db, err := models.OpenDB()
	if err != nil {
		return
	}
	defer db.Close()

	handler := models.AuthHandler{
		Db: db,
	}

	token, err := handler.LoginCheck(&input)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "username or password is incorrect."})
		return
	} else {
		c.JSON(http.StatusOK, gin.H{"token": token, "username": u.Username})
		return
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
	var input models.RegisterInput

	if err := c.ShouldBindJSON(&input); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	db, err := models.OpenDB()
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	defer db.Close()

	handler := models.NewAuthHandler(db)
	_, err = handler.SaveUser(&input)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": "registration success"})

}
