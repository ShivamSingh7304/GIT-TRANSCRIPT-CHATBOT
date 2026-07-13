from youtube_transcript_api import YouTubeTranscriptApi , TranscriptsDisabled



video_id = '7ARBJQn6QkM'

def load_yt():
    yt_trancript = YouTubeTranscriptApi()

    try:    
        transcript_list = yt_trancript.fetch(video_id , languages=["en"])
        transcript = " ".join(chunk.text for chunk in transcript_list)
        return transcript
    except TranscriptsDisabled:
        print("no transcript available for the vedio")
        return None

if __name__ =="__main__":
    transcript=load_yt()
    
    if transcript:
        print(transcript[:200])