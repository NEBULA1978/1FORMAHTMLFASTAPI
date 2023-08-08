# from fastapi import FastAPI

# Primera dorma

# app=FastAPI()

# @app.get("/")
# def root():
#     return "Hi,i am Fastapi"

# SEGUNDA FORMA

# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse

# app=FastAPI()

# @app.get("/",response_class=HTMLResponse)
# def root():
#     return """
#         <html>
#         <head>
#             <title>Web FastAPI</title>
#         </head>
#         <body>
#             <h1>Hi I a, a html file</h1>
#         </body>
#     </html>

#     """
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app=FastAPI()

app.mount("/static",StaticFiles(directory="./static"),name="static")

templates = Jinja2Templates(directory="./public/templates")


# Ruta para archivos html
@app.get("/",response_class=HTMLResponse)
def root():
    html_address = "./static/html/index.html"
    return FileResponse(html_address,status_code=200)

# Tercera forma:
# Ruta para Jinja2
@app.get("/template/{id}", response_class=HTMLResponse)
def template(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
