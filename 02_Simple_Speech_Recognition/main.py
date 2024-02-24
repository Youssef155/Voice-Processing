#@  To run this file use cmd with comand : "python main.py output3.wav"  @#


import sys
from api_communication import *


filename = sys.argv[1]

audio_url = Upload(filename)
save_transcript(audio_url, filename)