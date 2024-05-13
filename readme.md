
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

![SCREENSHOT1](utils\ss1.png)

Le das click y te desplegara una pequeña dashboard para interactuar con el endpoint, le damos al boton "try it out"
![SCREENSHOT2](utils\ss2.png)

Luego, le daremos al boton que dice "choose file", escojemos el archivo de audio que queramos, y le damos a "Execute" para procesarlo
![SCREENSHOT3](utils\ss3.png)

Finalmente, nos retornara una respuesta donde tendremos el texto procesado.
![SCREENSHOT4](utils\ss4.png)






