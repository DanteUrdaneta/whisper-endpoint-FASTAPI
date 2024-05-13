
# Pasar de audio a texto con whisper

### Pasos para usar

Instala las dependencias para correr el server

```bash
  pip install fastapi, uvicorn
```

Instala la dependencia para correr el modelo WHISPER

```bash
  pip install -U openai-whisper
```

Instala el driver de audio ffmpeg

usa este comando si tienes linux o un subsistema (recomendable)
```bash
  sudo apt update && sudo apt install ffmpeg
```

O instalalo en windows utilizando chocolatey

```bash
  choco install ffmpeg
```

### corre el server usando
```bash
  uvicorn main:app --reload 
```

## Como interactuar con el endpoint

ve al siguiente link: http://localhost:8000/docs#
(esto abrira una documentación interactuable para utilizar el endpoint)

Te encontraras con las rutas, como solo tenemos una sera la ruta "/upload" unicamente

![image](https://github.com/DanteUrdaneta/whisper-endpoint-FASTAPI/blob/main/utils/ss1.png?raw=true)


Le das click y te desplegara una pequeña dashboard para interactuar con el endpoint, le damos al boton "try it out"

![image](https://github.com/DanteUrdaneta/whisper-endpoint-FASTAPI/assets/137725460/d8b23a44-2a42-46a2-b136-415a93966d70)


Luego, le daremos al boton que dice "choose file", escojemos el archivo de audio que queramos, y le damos a "Execute" para procesarlo

![image](https://github.com/DanteUrdaneta/whisper-endpoint-FASTAPI/blob/main/utils/ss3.png?raw=true)


Finalmente, nos retornara una respuesta donde tendremos el texto procesado.

![image](https://github.com/DanteUrdaneta/whisper-endpoint-FASTAPI/blob/main/utils/ss4.png?raw=true)






