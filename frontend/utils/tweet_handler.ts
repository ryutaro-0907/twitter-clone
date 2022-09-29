import { Tweet, TweetBody } from '../typings';
import { client } from './axios';

export const fetchTweets = async () => {
    try {
      const data = await fetch('http://localhost:8082/api/v1/tweets', {
        method: 'GET',
        headers: {
         'accept': 'application/json'
        }
      })
      console.log("tweets", data)
      const tweets: Tweet[] = await data.json()
      console.log('tweets fetched succesfully;')
      return tweets
    } catch (err) {
      console.error(err) //
      return null;
  }}

export const postTweet = async (tweetBody:TweetBody) => {
    try {
      const endpoint = 'http://localhost:8082/api/v1/tweets'

      const result = await fetch(endpoint, {
        method: 'post',
        headers: {
          'Content-type': 'application/json',
        },
        body: JSON.stringify({tweetBody})
      })
      return result
    } catch (err) {
      console.error(err) //
  }}
