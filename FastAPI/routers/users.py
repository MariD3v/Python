from fastapi import APIRouter, HTTPException #APIRouter nos indica que esta es una ruta del API main
from pydantic import BaseModel # Para definir clases y objetos

'''
Distintos métodos HTTP
POST = Para crear datos
GET = Para leer datos
PUT = Para actualizar datos
DELETE = Para eliminar datos
'''
#HTTP Status Codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

router = APIRouter(prefix="/user",
                   tags=["Users"])

# Así obtenemos los usuarios en formato json sin usar clases u objetos
@router.get("/usersjson") 
async def usersjson(): 
    return [{"name":"Mari", "age":23, "branch":"developer"},
            {"name":"Miki", "age":25, "branch":"cybersecurity"}
            ]

# Así obtenemos los usuarios en formato json usando clases u objetos

# Definimos una clase Usuario
class User(BaseModel): # Con BaseModel no es necesario definir un constructor
    id : int
    name : str
    age : int
    branch : str

# Hacemos una lista simulando que es una base de datos

users_list = [User(id = 1, name="Mari", age=23, branch="developer"),
         User(id = 2, name="Miki", age=25, branch="cybersecurity")]

# Definimos una función que muestre los datos de la base de datos 

@router.get("/users")
async def users():
    return users_list # Nos devuelve un json


# Accedemos al usuario por su id

# Path
# Pasamos el párametro id al poner la ruta http://127.0.0.1:8000/user/1
@router.get("/{id}", response_model=User) #response_model nos indica que devuelve el método si va bien
async def user(id : int):
    return search_user(id)

# Query 
# Pasamos el parámetro id al poner la ruta http://127.0.0.1:8000/user/?id=1
@router.get("/", response_model=User)
async def user(id: int):
    return search_user(id)

@router.post("/", response_model=User, status_code=201) #Code 201 = "Created"
async def newUser(user : User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail = "El usuario ya existe") #Code 404 = "Not Found" 
        #Raise se usa como return pero para devolver code status
    else:
        users_list.append(user)
        return user

@router.put("/", response_model=User, status_code=202) #Code 202= "Accepted"
async def updateUser(user : User):
    found = False

    for index, user_saved in enumerate(users_list): #enumerate() nos obtiene un index para saber en que posición se encuentra
        if user_saved.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        raise HTTPException(status_code=404, detail = "Usuario no encontrado") #Code 404 = "Not Found" 
    else:
        return user
    
@router.delete("/{id}")
async def deleteUser(id : int):
    found = False

    if type(search_user(id)) == User:
        users_list.remove(search_user(id))
        found = True

    if not found:
        raise HTTPException(status_code=404, detail = "Usuario no encontrado") #Code 404 = "Not Found" 
    
def search_user(id: int):
    users = list(filter(lambda user: user.id == id, users_list)) #Uso de filter: Metemos en primer lugar 1 parámetro que será siempre una función, y en segundo lugar, una lista que queramos filtrar en funcion de la función anterior. Después se pasa a una lista el resultado
    try:
        return users[0]
    except:
        return {"error" : "No se ha encontrado el usuario"}