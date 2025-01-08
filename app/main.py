import whisper
import torch

# GPU 사용 가능 여부 확인
if torch.cuda.is_available():
    device = "cuda"
    print("GPU is available. Using CUDA.")
else:
    device = "cpu"
    print("GPU is not available. Using CPU.")

# Whisper 모델 로드
model = whisper.load_model("tiny", device=device)

# 처리할 파일 경로
file = "app/audio/test.m4a"

# 파일 변환 및 텍스트 추출
try:
    result = model.transcribe(file)
    print("Transcription result:", result["text"])
except Exception as e:
    print("Error during transcription:", str(e))