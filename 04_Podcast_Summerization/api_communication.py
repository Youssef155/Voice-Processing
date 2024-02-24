import requests
from config import API_KEY_ASSEMBLYAI, API_KEY_LISTENNOTES
import time
import pprint
import json


# Upload local file

transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
assemblyai_headers = {"authorization" : API_KEY_ASSEMBLYAI}

listennotes_endpoint = "https://listen-api.listennotes.com/api/v2/episodes"
listennotes_headers = {"X-ListenAPI-Key" : API_KEY_LISTENNOTES}

def get_episodes_sudio_url(episodes_Id):
    url = listennotes_endpoint + '/' + episodes_Id
    response = requests.request('GET', url, headers=listennotes_headers)
    data = response.json()

    audio_url = data['audio']
    episode_thumbnail = data['thumbnail']
    podcast_title = data['podcast']['title']
    episode_title = data['title']

    return audio_url, episode_thumbnail, podcast_title, episode_title

# Transcript the file
def transcribe(audio_url, auto_chapters):
    transcript_request = {"audio_url" : audio_url,
                          "auto_chapters": auto_chapters}
    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=assemblyai_headers)
    job_id = transcript_response.json()['id']
    return job_id


# Poll
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    poll_response = requests.get(polling_endpoint, headers=assemblyai_headers)
    return poll_response.json()

def get_transcription_result_url(audio_url, auto_chapters):
    transcript_id = transcribe(audio_url, auto_chapters)
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']    

        print("waiting 60 seconds...")
        time.sleep(60)

# Saving transcription
def save_transcript(episodes_Id):
    audio_url, episode_thumbnail, podcast_title, episode_title = get_episodes_sudio_url(episodes_Id)
    data, error = get_transcription_result_url(audio_url, auto_chapters=True)

    pprint.pprint(data)

    if data:
        txt_file = episodes_Id + '.txt'
        with open(txt_file, 'w') as txtf:
            txtf.write(data['text'])

        chapters_filename = episodes_Id + "_Chapters.json"
        with open(chapters_filename, 'w') as f:
            chapters = data['chapters']
            episode_data = {'chapters':chapters}

            episode_data['episode_thumbnail'] = episode_thumbnail
            episode_data['podcast_title'] = podcast_title
            episode_data['episode_title'] = episode_title

            json.dump(episode_data, f)
            print("Transcription saved!!")
            return True
    elif error:
        print("Error!!", error)

