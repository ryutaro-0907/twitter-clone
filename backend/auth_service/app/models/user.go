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
		return err
	}

	log.Println("password verified successfully.")
	return err


}

func (handler *AuthHandler) LoginCheck(input *LoginInput) (string, error) {
	var (
		err error
		u   User
	)

	log.Println("logging in...")

	if result := handler.Db.Where("username = ?", input.Username).First(&u); result.Error != nil {
		return "", errors.New("user not found please register")
	}

	err = VerifyPassword(input.Password, u.Password)

	if err != nil && err == bcrypt.ErrMismatchedHashAndPassword {
		return "incorrect password.", err
	}

	token, err := utils.GenerateToken(u.ID)

	if err != nil {
		log.Println(err)
		return "", err
	}

	log.Println("user is valid, returning token")

	return token, nil

}

func (handler *AuthHandler) SaveUser(input *RegisterInput) (*User, error) {

	log.Println("saving user to database with username=", input.Username)

	var uExist User

	if result := handler.Db.Where("username = ?", input.Username).First(&uExist); result.Error == nil {
		return &uExist, errors.New("username already taken")
	}

	u := &User{
		Username: input.Username,
		Password: input.Password,
	}

	log.Println("creating user with username=", u.Username)

	if result := handler.Db.Create(&u); result.Error != nil {
		return u, result.Error
	}

	log.Println("user created.")
	return u, nil
}

func (u *User) BeforeSave() error {
	log.Println("hashing password...")
	//turn password into hash
	hashedPassword, err := bcrypt.GenerateFromPassword([]byte(u.Password), bcrypt.DefaultCost)
	if err != nil {
		return err
	}
	log.Println("hashed Password.")
	u.Password = string(hashedPassword)

	//remove spaces in username
	u.Username = html.EscapeString(strings.TrimSpace(u.Username))
	log.Println("space in Username removed.")

	return nil

}
