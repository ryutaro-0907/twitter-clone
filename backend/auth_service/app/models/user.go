package models

import (
	"errors"
	"html"
	"log"
	"strings"

	"auth_service/app/utils"

	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
	"golang.org/x/crypto/bcrypt"
)

type LoginInput struct {
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
}

type RegisterInput struct {
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
}

type User struct {
	gorm.Model
	Username string `gorm:"size:255;not null;unique" json:"username"`
	Password string `gorm:"size:255;not null;" json:"password"`
}

type AuthHandler struct {
	Db *gorm.DB
}

func NewAuthHandler(db *gorm.DB) *AuthHandler {
	return &AuthHandler{Db: db}
}

func (handler *AuthHandler) GetUserByID(uid uint) (User, error) {
	var u User

	if err := handler.Db.First(&u, uid).Error; err != nil {
		log.Println(err)
		err := errors.New("User not found.")
		return u, err
	}

	PrepareGive(&u)

	return u, nil

}

func PrepareGive(u *User) {
	u.Password = ""
}

func VerifyPassword(password, hashedPassword string) error {
	log.Println("verifying password...")
	err := bcrypt.CompareHashAndPassword([]byte(hashedPassword), []byte(password))
	if err != nil {
		log.Println("verifying password failed", err)
	}
	return err
}

func (handler *AuthHandler) LoginCheck(username string, password string) (string, error) {
	var err error

	u := User{}
	log.Println("logging in...")

	user := handler.Db.Where("name = ?", username).First(&u)
	log.Println("user found in db")

	if user == nil {
		log.Println("could not find user", err)
		return "", err
	}

	err = VerifyPassword(password, u.Password)

	if err != nil && err == bcrypt.ErrMismatchedHashAndPassword {
		log.Println(err)
		return "", err
	}

	token, err := utils.GenerateToken(u.ID)

	if err != nil {
		log.Println(err)
		return "", err
	}

	log.Println("user is valid")

	return token, nil

}

func (handler *AuthHandler) SaveUser(input *RegisterInput) (*User, error) {

	log.Println("saving user to database")

	user := &User{
		Username: input.Username,
		Password: input.Password,
	}

	handler.Db.Create(&user)
	// FIXME
	// WANT TO DO
	// err := handler.Db.Create(&input).Error
	// err != nil {...}

	// BUT handler.Db.Create(&input).Error & handler.Db.Create(&input).Error()
	// do not return error unlike we see in official documentation.

	log.Println("user saved.")
	return user, nil
}

func (u *User) BeforeSave() error {
	log.Println("BeforeSave")
	//turn password into hash
	hashedPassword, err := bcrypt.GenerateFromPassword([]byte(u.Password), bcrypt.DefaultCost)
	if err != nil {
		log.Println(err)
		return err
	}
	log.Println("Hashed Password")
	u.Password = string(hashedPassword)

	//remove spaces in username
	u.Username = html.EscapeString(strings.TrimSpace(u.Username))
	log.Println("Values in User model cleaned.")

	return nil

}
