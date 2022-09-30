package controllers

import (
	"bytes"
	"encoding/json"
	"github.com/stretchr/testify/assert"
	"net/http"
	"net/http/httptest"
	"testing"

	"tweet_service/src/models"
	// "github.com/gin-gonic/gin"
)

// NOTE make sure to start up server before testing this.
// TODO Enable to use test db? or do it separately.
func TestFetchAllTweets(t *testing.T) {
	server := SetuptWebServer()

	w := httptest.NewRecorder()
	// TODO: Change url with env variable?
	req, _ := http.NewRequest("GET", "http://localhost:8082/api/v1/tweets", nil)
	server.ServeHTTP(w, req)

	assert.Equal(t, 200, w.Code)
}

func TestCreateTweet(t *testing.T) {
	server := SetuptWebServer()
	tweet := models.CreateTweet{
		Username: "user",
		Body:     "text",
	}

	w := httptest.NewRecorder()
	var buf bytes.Buffer
	err := json.NewEncoder(&buf).Encode(tweet)
	if err != nil {
		t.Fatal(err)
	}

	// FIXME
	// change url
	req, _ := http.NewRequest("POST", "http://localhost:8082/api/v1/tweets", &buf)
	server.ServeHTTP(w, req)

	assert.Equal(t, 200, w.Code)
}
