import boto3, uuid, os
from django.utils.timezone import now

'1'
#image 객체 통째로 받아오는 로직
s3 = boto3.resource('s3',
                    aws_access_key_id=AWS_S3_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_S3_SECRET_ACCESS_KEY,)
                
bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)
object = bucket.Object('//image url//')
response = object.get()
download_image = response['Body']

'2'
#s3 image delete
s3_resource = boto3.client(
                    's3',
                    aws_access_key_id=AWS_S3_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_S3_SECRET_ACCESS_KEY,
                )

image_url = '//image_url//'

s3_resource.delete_object(Bucket=AWS_STORAGE_BUCKET_NAME, Key=str(image_url))

'3'
#serializer data 저장시 image upload code (in models.py )
def upload_image_to_image(instance, filename):
    name = str(uuid.uuid4())
    filename_base, filename_ext = os.path.splitext(filename)
    return 'image/%s/%s' % (
        now().strftime("%Y%m%d"),
        name
    )
#해당 image field는 아래와 같이 option추가하면 됨^^
profile_image = models.ImageField(upload_to=upload_image_to_image)