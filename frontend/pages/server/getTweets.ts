// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'
import { Tweet } from '../../typings';
// import { client } from '../../api/axios';

export type Data = {
  tweets: Tweet[]
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
    console.log('getting tweets')

    const tweets: any = await fetch('http://localhost:8080/api/tweets')
    console.log(tweets)
    res.status(200).json({ tweets })

  }
