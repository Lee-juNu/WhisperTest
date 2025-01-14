import whisper
import torch

# GPU 使用可能かどうか
if torch.cuda.is_available():
    device = "cuda"
    print("GPU is available. Using CUDA.")
else:
    device = "cpu"
    print("GPU is not available. Using CPU.")

# Whisper モデルロード(tiny, base, small, medium, large, turbo)
model = whisper.load_model("tiny", device=device)

# mp3 ファイルのパス
file = "app/audio/kr.mp3"

# 文字お越し実行
try:
    result = model.transcribe(file)
    print("Transcription result:", result["text"])
except Exception as e:
    print("Error during transcription:", str(e))
