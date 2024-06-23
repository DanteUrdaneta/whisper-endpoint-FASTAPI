from fastapi import FastAPI, UploadFile
from modules.functions import Whisper
from modules.functions import Process
import shutil
from fastapi.middleware.cors import CORSMiddleware
from modules.functions import convert_text_to_audio
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()


# Paso 1: Definir el modelo Pydantic
class TextoEntrada(BaseModel):
    texto: str


origins = [
    "http://localhost:5500",  # Permitir solicitudes desde este origen
    "http://127.0.0.1:5500",  # También puedes añadir otros orígenes si es necesario
    "http://127.0.0.1:5000",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload")
async def upload(audio: UploadFile):
    # save file
    path = "uploads/" + audio.filename
    with open(path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    # transcribe
    result = Whisper().to_text(path, audio.filename)
    return result


@app.post("/convert")
async def convert(texto_entrada: TextoEntrada):
    # Paso 3: Usar el modelo en la función
    path = convert_text_to_audio(texto_entrada.texto)
    return FileResponse(path, media_type="audio/mp3", filename=path)


@app.post("/process")
async def process(text: str):
    q1 = Process()
    query = q1.select_query(text)
    result = q1.execute_query(query)

    result = result[0][0]
    return result
