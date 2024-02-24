# Project Steps
# Upload the file to AssemblyAI 
# Transcript the file 
# Keep polling AssemblyAI API to see transcription when done
# Save transcript file


import requests
from config import API_KEY_ASSEMBLYAI
import time
import json


# Upload local file
upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
headers = {"authorization" : API_KEY_ASSEMBLYAI}


def Upload(filename):
    def read_file(filename, chunk_size=5242880): #assemblyai requires data to be in chunks of 5MB size
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint, headers=headers, data=read_file(filename))
    audio_url = upload_response.json()['upload_url']
    return audio_url

# Transcript the file
def transcribe(audio_url, sentiment_analysis):
    transcript_request = {"audio_url" : audio_url,
                          "sentiment_analysis" : sentiment_analysis}
    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    job_id = transcript_response.json()['id']
    return job_id


# Poll
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    poll_response = requests.get(polling_endpoint, headers=headers)
    return poll_response.json()

def get_transcription_result_url(audio_url, sentiment_analysis):
    transcript_id = transcribe(audio_url, sentiment_analysis)
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
            print(data)
            return data, None
        elif data['status'] == 'error':
            return data, data['error']    

        print("waiting 30 seconds...")
        time.sleep(30)

# Saving transcription
def save_transcript(audio_url, filename, sentiment_analysis=False):
    data, error = get_transcription_result_url(audio_url, sentiment_analysis)

    if data:
        txt_file = filename + '.txt'
        with open(txt_file, 'w') as txtf:
            txtf.write(data['text'])
        if sentiment_analysis:
            filename = filename + "_sentiment.json"
            with open(filename, 'w') as f:
                sentiments = data["sentiment_analysis_results"]
                json.dump(sentiments, f, indent=4)

        print("Transcription saved!!")
    elif error:
        print("Error!!", error)

