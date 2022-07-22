import boto3
from botocore.exceptions import ClientError
import os
import time
import requests

transcribe_client = boto3.client('transcribe', region_name = 'us-west-2')

def upload_file_to_bucket(path, file_name, bucket):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(path + file_name, bucket, file_name)
    except ClientError as e:
        print(e)
        return False
    return True



def transcribe_file(filename):

    file_uri = 's3://userstudyqueries/' + filename
    job_name = filename

    transcribe_client.start_transcription_job(
        TranscriptionJobName = job_name,
        Media = {
            'MediaFileUri': file_uri
        },
        MediaFormat = 'wav',
        LanguageCode = 'en-US'
    )

    max_tries = 60
    while max_tries > 0:
        max_tries -= 1
        job = transcribe_client.get_transcription_job(TranscriptionJobName = job_name)
        job_status = job['TranscriptionJob']['TranscriptionJobStatus']
        if job_status in ['COMPLETED', 'FAILED']:
            print(f"Job {job_name} is {job_status}.")
            if job_status == 'COMPLETED':
                print(
                    f"Download the transcript from\n"
                    f"\t{job['TranscriptionJob']['Transcript']['TranscriptFileUri']}.")
                transcription_json = requests.get(job['TranscriptionJob']['Transcript']['TranscriptFileUri']).json()
                transcript = transcription_json['results']['transcripts'][0]['transcript']
                return transcript
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(3)