from fastapi import FastAPI 
from routers import users, products#Importamos la ruta users de la carpeta routers
from fastapi.staticfiles import StaticFiles
#Iniciamos el servidor con "python3 -m uvicorn main:app --reload" en windows y "uvicorn main:app --reload" en linux o en venv en la terminal
#FastAPI genera documentacion en Swagger http://127.0.0.1:8000/docs o en Redocly http://127.0.0.1:8000/redoc

app = FastAPI()

#Routers

app.include_router(users.router) #Incluimos la ruta users en main
app.include_router(products.router)
app.mount("/static", StaticFiles(directory='static'), name='static') #Así importamos recursos estaticos, desde la carpeta static. Accedemos a ellos en http://127.0.0.1:8000/static/images/python.png

@app.get("/")
async def root(): #Siempre que llamamos a un servidor las funciones deben ser asincronas (para cuando aparece el simbolo de loading en una pantalla cargando)
    return "Hola FastAPI"

@app.get("/url")
async def url():
    return { "url_mari":"https://github.com/LittleMari"} #La forma en la que se comunican las APIs es con formato json

