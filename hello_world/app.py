import json
import sys
import boto3
import os
import uuid
from urllib.parse import unquote_plus

import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import decode
import numpy as np
import cv2

import imageio
import imgaug as ia
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage

from PIL import Image

s3 = boto3.client('s3')
textract = boto3.client('textract')
DESTINATION_BUCKETNAME = os.environ['DESTINATION_BUCKETNAME']

def decode(im):
    print("Decoding image")
    decoded_objects = pyzbar.decode(im)
    print(decoded_objects)
    for obj in decoded_objects:
        print("Type: {}".format(str(obj.type)))
        print("Data: {}".format(str(obj.data)))
    return decoded_objects

def detect_boxes(image_path, resized_path):
    with Image.open(image_path) as image:
        image.save(resized_path)
    im = cv2.imread(image_path)
    decode(im)


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        S3 event notification

    context: object, required
        Lambda Context runtime methods and attributes
        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    Nothing

    """

    print("In lambda function")
    print(event)
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        tmpkey = key.replace('/', '')
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
        upload_path = '/tmp/resized-{}'.format(tmpkey)
        s3.download_file(bucket, key, download_path)
        detect_boxes(download_path, upload_path)
        s3.upload_file(upload_path, DESTINATION_BUCKETNAME, key)

    return
