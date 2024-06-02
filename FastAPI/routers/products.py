from fastapi import APIRouter

router = APIRouter(prefix="/products", # Prefix nos indica que todas las rutas de este router comenzaran por /products
                   tags=["Products"]) # Tags es para especificar mejor la documentación


product_list = ["producto 1", "producto 2", "producto 3"]

@router.get("/")
async def products():
    return  product_list

@router.get("/{id}")
async def products(id: int):
    return  product_list[id]
