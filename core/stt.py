from faster_whisper import WhisperModel

def transcribe_audio(audio_path):
    model = WhisperModel("large-v3", device="cuda", compute_type="float16")
    segments, _ = model.transcribe(audio_path)
    return " ".join(segment.text for segment in segments)

def main():
    audio_path = "../resources/16k16bit.mp3"
    transcription = transcribe_audio(audio_path)
    print(transcription)

if __name__ == '__main__':
    main()