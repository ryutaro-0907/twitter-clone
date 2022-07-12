// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'
import { TweetBody } from '../../typings'

type Data = {
    message: string,
    body?: TweetBody,
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
    try {
        console.log('handler called')
        const data: TweetBody = JSON.parse(req.body)
        console.log('data', data)

        const mutations =  [{
            create: {
                _type: "tweet",
                text: data.text,
                username: data.username,
                blockTweet: false,
                profileImage: data.profileImage,
                image: data.image,
            }
          }]

        const apiEndpoint = `https://${process.env.NEXT_PUBLIC_SANITY_PROJECT_ID}.api.sanity.io/v2021-06-07/data/mutate/${process.env.NEXT_PUBLIC_SANITY_DATASET}`

        const result = await fetch(apiEndpoint, {
            method: 'post',
            headers: {
              'Content-type': 'application/json',
              Authorization: `Bearer ${process.env.SANITY_API_TOKEN}`
            },
            body: JSON.stringify({mutations})
        })

        const json = await result.json();
        console.log('post tweet', json)

        res.status(200).json({ message: 'added!' , body: json})

    } catch (err) {
        res.status(500).json({ message: 'error' + err})
    }

}
