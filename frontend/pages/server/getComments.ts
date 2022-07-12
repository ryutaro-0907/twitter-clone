// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'
import { sanityClient } from '../../sanity';

import groq from 'groq';

const commentQuery = groq`
    *[_type=="comment" && references(*[_type== 'tweet' && _id == $tweetId]._id)] {
        _id,
        ...
    } | order(_cratedAt desc)
`

type CommentData = Comment[]

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<CommentData>
) {
    const { tweetId } = req.query;

    const comments: Comment[] = await sanityClient.fetch(commentQuery, {
        tweetId,
    })

    res.status(200).json(comments)
}
