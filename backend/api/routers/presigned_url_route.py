import logging
from urllib import response

from fastapi import APIRouter, HTTPException

from ..domains.presigned_url_model import AwsPreSignedUrlResponse
from ..infra.aws.s3_file_uploader import AwsBucketApi

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/aws-s3-pre-signed-url", response_model=AwsPreSignedUrlResponse)
def gen_pre_signed_url(file_name: str):
    try:
        aws_api = AwsBucketApi()

        res = aws_api.create_presigned_post(object_name=file_name)
        if res is not None:
            logger.info("generated presigned url")
            return res
        else:
            HTTPException(404, "Couldn't generate presigned url", res)
    except Exception as e:
        return HTTPException(500, "Couldn't create AwsBucketApi", e)
