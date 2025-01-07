import whisper
import torch

model = whisper.load_model("tiny")
file = "app/audio/kr.mp3" # mp3파일 경로를 넣어준다.
result = model.transcribe(file)
print(result["text"])