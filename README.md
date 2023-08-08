# 1FORMAHTMLFASTAPI

3 maneras de mostar contenido html js y cs con FASTAPI:

Creamos entorno:

python3 -m venv venv
El la ruta:
/home/next/Vídeos/VIDEOS_PROYECTOS/3 Formas diferentes de devolver HTML con FASTAPI _ Construyendo SITIO WEB con FASTAPI
source venv/bin/activate

Para iniciar entorno virtual:
source /home/next/Escritorio/venv/bin/activate

Abro con vscode:
code venv/

Instalo FastAPI y uvicorn:
pip install uvicorn fastapi

Creo archivo raiz main.py:

from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return "Hi,i am Fastapi"

Para iniciar por consola:
Entro en carpeta venv(he movido el proyecto de carpeta):
uvicorn main:app --reload

Para ver en navegador:

http://localhost:8000/

"Hi,i am Fastapi"

Primera forma ver html en navegador:
main.py:
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()

@app.get("/",response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>Web FastAPI</title>
        </head>
        <body>
            <h1>Hi I a, a html file</h1>
        </body>
    </html>

    """

    Para ver pagina de fastapi:
 view-source:http://localhost:8000/docs

http://localhost:8000/docs#/default/root__get

Añado archivo main.py:

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles


app=FastAPI()

app.mount("/static",StaticFiles(directory="./static"),name="static")


# Ruta para archivos html
@app.get("/",response_class=HTMLResponse)
def root():
    html_address = "./static/html/index.html"
    return FileResponse(html_address,status_code=200)

PARA VER EN NAVEGADOR:

http://localhost:8000/
FUNCIONA

Archivo index.html dentro carpeta html:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web FastAPI</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <h1>Hi I a, a html file</h1>
    <script defer src="/static/js/script.js"></script>
</body>
</html>

(((((((((((((((((((((((((((((())))))))))))))))))))))))))))))
(((((((((((((((((((((((((((((())))))))))))))))))))))))))))))
