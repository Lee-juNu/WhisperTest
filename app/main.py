from fastapi import FastAPI, HTTPException
from app.health import router as health_router
from app.transcriber import transcribe_audio

app = FastAPI()

app.include_router(health_router)

@app.get("/", tags=["Transcription"])
def read_root():
    file_path = "app/audio/kr.mp3"
    try:
        result = transcribe_audio(file_path)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return result
