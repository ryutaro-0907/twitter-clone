export interface Tweet extends TweetBody {
    id: int
    created_at: string
    user_id: int
    updated_at?: string
    deleted_at?: string
    blocked?: bool
}

export type TweetBody = {
    text: string
    username?: string
    profile_image: string
    images?: string
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