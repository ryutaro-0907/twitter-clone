export interface Tweet extends TweetBody {
    _id: string
    _createdAt: string
    updatedAt: string
    _rev: string
    _type: 'tweet'
    blockTweet: boolean
}

export type TweetBody = {
    text: string
    username: string
    profileImage: string
    image?: string
}

export type CommentBody = {
    comment: string
    tweetId: string
    profileImage: string
    username: string
}

export interface Comment extends CommentBody {
    _id: string
    _createdAt: string
    updatedAt: string
    _rev: string
    _type: 'comment'
    tweet: {
        _ref: string
        _type: 'reference'
    }
}