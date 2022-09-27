from pydantic import BaseModel


class Fields(BaseModel):
    key: str
    AWSAccessKeyId:str
    policy: str
    signature: str


class AwsPreSignedUrlResponse(BaseModel):
    url: str
    fields: Fields