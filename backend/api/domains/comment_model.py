from pydantic import BaseModel

class Comment(BaseModel):
    id: str
    created_at: str
    updated_at: str
    
    blocked: bool
    comment: str
    tweet_id: str
    user_id: str

    images: str or None = None
    deleted_at: str or None =None
