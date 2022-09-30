export interface Tweet extends TweetBody {
    id: number
    created_at: str
    username: str
    updated_at?: str
    deleted_at?: str
    blocked?: bool
}

export type TweetBody = {
    body: str
    username?: str
    profile_image?: str
    images?: str
}

export type CommentBody = {
    tweet_id: number
    user_id: number
    username: str
    profile_image: str

    comment: str
    images?: str

    blocked?: bool = false




}

export interface Comment extends CommentBody {
    id: number
    created_at: datetime
    updated_at: datetime = null
    deleted_at: datetime = null

    user_id: number
    tweet_id: number
    username: str
    profile_image: str

    comment: str
    images: str
    blocked?: bool = false


}