import yt_dlp
from dotenv import load_dotenv
import os, re

def download_audio(url, output_path="./resources/audio/"):
    outtmpl = f"{output_path}%(title)s.%(ext)s"
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "ffmpeg_location": os.getenv("FFMPEG_PATH"),
        "outtmpl": outtmpl,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            # 获取视频信息
            info_dict = ydl.extract_info(url, download=True)
            # 解析后的实际路径
            actual_path = ydl.prepare_filename(info_dict)
            final_path = re.sub(r"\.[^.]*$", ".mp3", actual_path)
            print("下载成功！")
            print(f"音频已保存到: {final_path}")
            return final_path
    except Exception as e:
        print(f"下载失败: {e}")

def main():
    load_dotenv("./.env")
    video_url = "https://www.bilibili.com/video/BV1Yx411m7Fw"
    download_audio(video_url)

if __name__ == '__main__':
    main()
