from minio import Minio
import os

client = Minio("172.16.2.189:9000", "minioadmin", "minioadmin", secure=False)
print('-----------------------------------------------')

a = os.listdir('/Volumes/OSX_Externa/VMO/Temp')

# if client.bucket_exists("medicaldata"):
#     print("my-bucket exists")
# else:
#     print("my-bucket does not exist")  

count = 0

for i in a:
    count += 1
    client.fput_object("medicaldata", f"vid/{i}",os.path.join('/Volumes/OSX_Externa/VMO/Temp',i))
    print(count)

