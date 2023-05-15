from flask import Flask
from flask import jsonify
from flask import request
import os
from minio import Minio
from minio.error import S3Error
import requests
import time

app = Flask(__name__)

@app.route('/')
def index():
    app.logger.info('User connected to root URL')
    return 'Hello, world!'

def upload_minio(video_data):
    client = Minio("172.16.2.189:9000", "minhnd", "minhnd99", secure=False)
    print('-----------------------------------------------')
    poc_bucket = "poc"

    if client.bucket_exists(poc_bucket):
        print("my-bucket exists")
    else:
        print("my-bucket does not exist")  

    try:
        # Replace 'my-bucket' with your bucket name and 'my-video.mp4' with your file name
        # video_len = len(video_data.read())  # Replace with your video data in bytes format
        response = client.fput_object(poc_bucket, "nguyen_2.mp4", video_data)
        print(f"Video data object uploaded successfully. {response}")
    except S3Error as e:
        print(f"Error: {e}")


    url = "heheh"
    return url

def predict():
    url = "http://172.16.2.189:8500/preprocess_vid/"
    # url = "http://172.16.2.189:8000"
    headers = {
        "name_user": "2",
        "id_video": "a"
    }
    print("start predict")
    response = requests.post(url, json = { "name_user": "nguyen", "id_video": "2"})
    # time.sleep(10)
    # response = requests.get(url)
    print("After response")
    if response.status_code == 200:
        data = response.json()
        print("htttlll")
        # Process the data
        print(data)
    else:
        print(f"GET failed: {response.status_code}")
    return data

@app.route('/upload-video', methods=['POST'])
def upload_video():
    # Get the video file from the request
    app.logger.info('User connected to root URL')
    # print(request.get_json())
    print("skdfklsdfkasklf")
    video = request.files.get('video')
    print("fsdfsdf")
    # Get any additional parameters from the request
    param1 = request.form.get('param1')
    param2 = request.form.get('param2')
    # Save the video file to disk
    path = os.path.join('/Volumes/OSX_Externa/VMO/VideoData/', video.filename)
    video.save(path)
    # push to minio
    minio_url = upload_minio(path)
    print("upload minio")
    print(minio_url)
    data  = predict()
    
    # Handle the parameters or perform any other required processing here
    
    # Return a response to the client
    response_data = data
    app.logger.info('\nVideo upload successfull!!!')
    return jsonify(response_data), 200



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")