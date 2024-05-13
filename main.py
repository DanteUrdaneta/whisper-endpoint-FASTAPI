from fastapi import FastAPI, UploadFile
from modules.functions import Whisper
import shutil

app = FastAPI()


@app.post("/upload")
async def upload(audio: UploadFile):
    # save file
    path = "uploads/" + audio.filename
    with open(path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    # transcribe
    result = Whisper().to_text(path, audio.filename)
    return result




