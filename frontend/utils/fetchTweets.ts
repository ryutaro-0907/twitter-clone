import { Tweet } from '../typings';

export const fetchTweets = async () => {
    const BaseUrl = `${process.env.NEXT_PUBLIC_BASE_URL}/api/getTweets`;
    const result = await fetch(BaseUrl);

    const data = await result.json();

    const tweets:Tweet[] = data.tweets;

    return tweets;

}