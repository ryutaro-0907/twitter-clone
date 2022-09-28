import { NextApiRequest, NextApiResponse } from "next";
import S3 from "aws-sdk/clients/s3";



export const config = {
    api: {
        bodyParser: {
            sizeLimit: "800mb",
        },
    },
};