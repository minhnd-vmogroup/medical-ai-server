from flask import Flask
from flask import jsonify
from flask import request
import os
from minio import Minio
from minio.error import S3Error
import requests


def predict():
    url = "http://172.16.2.189:8000/preprocess_vid/"
    # url = "http://172.16.2.189:8000"
    headers = {
        "name_user": "2",
        "id_video": "a"
    }

    response = requests.post(url, headers=headers)
    # response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("response")
        # Process the data
        print(data)
    else:
        print("hekwejse ----------\n")
        print(f"GET failed: {response.status_code}")




if __name__ == '__main__':
    predict()