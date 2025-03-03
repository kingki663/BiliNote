import argparse, os
from core.bilibili_downloader import download_audio
from core.stt import transcribe_audio, save2txt
from core.summarizer import summarize_content
from dotenv import load_dotenv

def run(url, audio_output_path, transcription_output_path, summary_output_path):
    try:
        # 下载音频
        # BUG 同一个音频会下载两次
        audio_path = download_audio(url, audio_output_path)
        
        # 转录音频
        transcription = transcribe_audio(audio_path)
        
        # 提取文件名（去掉扩展名）只取文件名
        filename_with_extension = os.path.basename(audio_path)  # 获取文件名（包含扩展名）
        filename = filename_with_extension[:-4]  # 去除扩展名 (.mp3)
        print(f"filename: {filename}")
        
        # 保存转录文本
        transcription_file = f"{transcription_output_path}/{filename}.txt"
        save2txt(transcription, transcription_file)
        
        # 生成摘要并保存
        summary = summarize_content(transcription)
        summary_file = f"{summary_output_path}/{filename}_summary.txt"
        save2txt(summary, summary_file)
        
        print(f"音频已保存到: {audio_path}")
        print(f"转录文本已保存到: {transcription_file}")
        print(f"摘要已保存到: {summary_file}")
        
    except Exception as e:
        print(f"发生错误: {e}")

def main():
    load_dotenv(dotenv_path="./.env")
    # 设置命令行参数
    parser = argparse.ArgumentParser(description="下载B站视频音频并生成转录文本和摘要")
    parser.add_argument("--url", type=str, help="B站视频URL")
    parser.add_argument(
        "--audio_output", 
        type=str, 
        default="./resources/audio/", 
        help="音频文件输出路径（默认: ./resources/audio/）"
    )
    parser.add_argument(
        "--transcription_output", 
        type=str, 
        default="./resources/txt/", 
        help="转录文本输出路径（默认: ./resources/txt/）"
    )
    parser.add_argument(
        "--summary_output", 
        type=str, 
        default="./resources/summary/", 
        help="摘要文本输出路径（默认: ./resources/summary/）"
    )
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 调用主逻辑
    run(args.url, args.audio_output, args.transcription_output, args.summary_output)

if __name__ == '__main__':
    main()