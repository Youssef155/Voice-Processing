from pydub import AudioSegment

audio = AudioSegment.from_wav("Youssef.wav")

# Increase the volume by 6dB
audio = audio + 6

# Repeat the audio one more time
audio = audio * 2

# Make audio fade in ofter specific time
audio = audio.fade_in(2000)

# Export mp3 file
audio.export("NotWave.mp3", format="mp3")

# Load mp3 file
audio2 = AudioSegment.from_mp3("NotWave.mp3")
print("done!")