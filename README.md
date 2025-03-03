# BiliNote
一个实用的Bilibili视频笔记工具，支持音频转录为文字，并利用deepseek完成内容总结


## QuickStart
### Env
1. 在本机安装CUDA和CUDNN
2. 在本机安装FFmpeg
3. 在conda环境中安装[PyTorch](https://pytorch.org/)
4. `pip install faster-whisper openai dotenv yt-dlp`

### Usage
`python main.py --url <video_url>` 