package models

import (
	"log"
	"regexp"
	"testing"

	"github.com/DATA-DOG/go-sqlmock"
	"github.com/jinzhu/gorm"
)

func NewDbMock() (*gorm.DB, sqlmock.Sqlmock, error) {
	sqlDB, mock, err := sqlmock.New()
	mockDB, err := gorm.Open("postgres", sqlDB)
	return mockDB, mock, err
}

func DummyHandler(db *gorm.DB) *AuthHandler {
	handler := NewAuthHandler(db)
	return handler
}

func TestSaveUser(t *testing.T) {
	mockDB, mock, err := NewDbMock()
	if err != nil {
		t.Error("Failed to initialize mock DB:", err)
	}
	defer mockDB.Close()

	u := &RegisterInput{
		Username: "Tom Hanks",
		Password: "tom1111@gmail.com",
	}

	// set expexted result
	rows := sqlmock.NewRows([]string{"ID"}).AddRow(1)

	mock.ExpectBegin()
	mock.ExpectQuery(regexp.QuoteMeta(
		`INSERT INTO "users" ("created_at","updated_at","deleted_at","username","password") VALUES ($1,$2,$3,$4,$5)`)).
		WillReturnRows(rows)
	mock.ExpectCommit()

	handler := DummyHandler(mockDB)
	user, err := handler.SaveUser(u)
	log.Printf("%T, %v", user, user)
	if err != nil {
		t.Fatal(err)
	}

	if err := mock.ExpectationsWereMet(); err != nil {
		t.Errorf("Test Create User: %v", err)
	}
}
