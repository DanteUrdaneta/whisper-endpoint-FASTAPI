from fastapi import FastAPI, UploadFile
from modules.functions import Whisper
from modules.functions import Process
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
    return result.text


@app.post("/process")
async def process(text: str):
    q1 = Process()
    query = q1.select_query(text)
    result = q1.execute_query(query)

    result = result[0][0]
    return result
