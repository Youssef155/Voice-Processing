import youtube_dl

ydl_opt={"extract_flat":True,'quiet':True}
ydl = youtube_dl.YoutubeDL(ydl_opt)
ydl.add_default_info_extractors()
ydl1 = youtube_dl.YoutubeDL()

def get_video_infos(url):
    VIDEO_URL = url
    with ydl:
        result = ydl.extract_info(VIDEO_URL, download=False)
    if "entries" in result:
        return result["entries"][0]
    return result

def get_audio_url(video_info):
    for f in video_info["formats"]:
        print(f["ext"])

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=e-kSGNzu0hM"
    video_info = get_video_infos(url)
    audio_url = get_audio_url(video_info)
    print(audio_url)