
# Convert Audio to Text with Whisper

### Steps to use
Instala las dependencias para correr el server

```bash
  pip install fastapi, uvicorn
```

Install the dependency to run the WHISPER model

```bash
  pip install -U openai-whisper
```

Install the ffmpeg audio driver

Use this command if you have Linux or a subsystem (recommended)
```bash
  sudo apt update && sudo apt install ffmpeg
```

Or install it on Windows using Chocolatey

```bash
  choco install ffmpeg
```

### Run the server using
```bash
  uvicorn main:app --reload 
```

## How to interact with the Endpoint

Go to the following link: http://localhost:8000/docs#
(this will open an interactive documentation to use the endpoint)

You will find the routes; since we only have one, it will only be the "/upload" route.

![image](https://github.com/DanteUrdaneta/whisper-endpoint-FASTAPI/blob/main/utils/ss1.png?raw=true)


Click on it, and a small dashboard will interact with the endpoint. Click the "try it out" button.

![image](https://github.com/DanteUrdaneta/whisper-endpoint-FASTAPI/assets/137725460/d8b23a44-2a42-46a2-b136-415a93966d70)


Then, click the "Choose file" button, select the audio file you want, and click "Execute" to process it.

![image](https://github.com/DanteUrdaneta/whisper-endpoint-FASTAPI/blob/main/utils/ss3.png?raw=true)


Finally, you will receive a response with the processed text.

![image](https://github.com/DanteUrdaneta/whisper-endpoint-FASTAPI/blob/main/utils/ss4.png?raw=true)






