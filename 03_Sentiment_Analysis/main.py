import json
from api_communication import save_transcript, Upload
import sys

filename = sys.argv[1]

audio_url = Upload(filename)

save_transcript(audio_url, filename, sentiment_analysis=True)