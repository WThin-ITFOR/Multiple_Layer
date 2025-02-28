import uuid
import boto3

def generate():
    return str(uuid.uuid4())

def get_s3(access_key, secret_key, region_name, bucket_name):
    s3 = boto3.client('s3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key ,
            region_name=region_name
    )

    response = s3.list_objects_v2(Bucket=bucket_name)
    objects = response.get('Contents', [])

    for obj in objects:
        print(f"- {obj['Key']}")
    else:
        print(f"{bucket_name} バケットにオブジェクトはありません。")
