import boto3
import os
import urllib.parse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key'],
        encoding='utf-8'
    )

    if not key.startswith('uploads/') or key == 'uploads/':
        return

    filename = os.path.basename(key)
    extension = filename.split('.')[-1].lower()

    if extension in ['jpg', 'jpeg', 'png', 'gif', 'svg']:
        folder = 'images/'
    elif extension == 'pdf':
        folder = 'pdfs/'
    elif extension in ['doc', 'docx', 'txt', 'csv', 'xlsx']:
        folder = 'documents/'
    elif extension in ['mp4', 'mov', 'avi', 'mkv']:
        folder = 'videos/'
    else:
        folder = 'others/'

    destination_key = folder + filename

    try:
        s3.copy_object(
            Bucket=bucket,
            CopySource={'Bucket': bucket, 'Key': key},
            Key=destination_key
        )

        s3.delete_object(
            Bucket=bucket,
            Key=key
        )

        print(f"Moved {filename} to {folder}")

    except Exception as e:
        print(f"Error: {str(e)}")
        raise e