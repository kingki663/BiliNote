from faster_whisper import WhisperModel

def transcribe_audio(audio_path):
    model = WhisperModel("large-v3", device="cuda", compute_type="float16")
    print("开始转录...")
    segments, _ = model.transcribe(audio_path, log_progress=True, vad_filter=True)
    return " ".join(segment.text for segment in segments)

def save2txt(transcription, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(transcription)

def main():
    audio_path = "../resources/audio/【一席】只是一个人的命运，只是一个人的悲喜，只是一个人的上升和坠落 双雪涛：冬天的骨头.mp3"
    transcription = transcribe_audio(audio_path)
    print(transcription)

if __name__ == '__main__':
    main()