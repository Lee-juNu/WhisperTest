from fastapi import FastAPI, HTTPException, Query
from app.health import router as health_router
from app.transcriber import transcribe_audio

app = FastAPI()

app.include_router(health_router)

@app.get("/", tags=["Transcription"])
def read_root(
    file_name: str = Query(..., description="サウンドファイル名"),
    extension: str = Query(..., description="拡張子")
):
    file_path = f"app/audio/{file_name}.{extension}"
    try:
        result = transcribe_audio(file_path)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return result
