import { Tweet, TweetBody } from '../typings';
import { client } from './axios';

export const fetchTweets = async () => {
    try {
      const data = await fetch('http://nginx:8080/server/tweets')
      const tweets: Tweet[] = await data.json()
      console.log('tweets fetched succesfully;')
      return tweets
    } catch (err) {
      console.error(err) //
  }}

export const postTweet = async (tweetBody:TweetBody) => {
    try {
      const endpoint = 'http://nginx:8080/server/tweets'

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
