import { Tweet } from '../typings';

export const fetchTweets = async () => {
    const BaseUrl = '/server/getTweets'
    const result = await fetch(BaseUrl);
    const tweets:Tweet[] = await result.json();

    return tweets as Tweet[];

}
