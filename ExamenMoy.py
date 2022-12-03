#Moisés Moreno Maravilla, 17420582
from  Mongodb import PyMongo
from configur import  variables
def meteraMongo(Json):
    objPymongo = PyMongo(variables)
    tabla="PropductosExamen"
    for Pro in Json:
        objPymongo.conectar_MongoDB()
        objPymongo.insertar(tabla,Pro)
        objPymongo.desconectar_MongoBD()
elemento=[
    {
        "idProducto": 1850,
        "productoNombreLargo": "Whisky William Lawsons Std 750 ml",
        "productoNombreCorto": "William Lawsons Std",
        "productoDescripcion": "Es un whisky afrutado de cuerpo ligero, se caracteriza por su aroma a pastel de manzana y su sabor a cereal tostado y al tofee, con un final suave.",
        "productoTipo": 1,
        "productoPresentacion": "Botella",
        "productoCosto": 170.5,
        "productoGanancia": 15,
        "productoDescuento": 0,
        "productoExistencia": 1000,
        "productoImagen": "Whisky-1850.webp"
    },
    {
        "idProducto": 1450,
        "productoNombreCorto": "Outer Space",
        "productoNombreLargo": "Vodka Outer Space 750 ml",
        "productoDescripcion": "Es un vodka hecho con maíz 100% americano, sin gluten, el diseño de su botella es único y llamativo. Tiene aromas y sabores a frutos secos.",
        "productoTipo": 1,
        "productoPresentacion": "Botella",
        "productoCosto": 700.5,
        "productoGanancia": 15,
        "productoDescuento": 0,
        "productoExistencia": 1000,
        "productoImagen": "Vodka-1450.webp"
    },
    {
        "idProducto": 850,
        "productoNombreCorto": "Ron Antillano Blanco",
        "productoNombreLargo": "Ron Antillano Blanco C/Vaso/Macerador 1L",
        "productoDescripcion": "",
        "productoTipo": 1,
        "productoPresentacion": "Botella",
        "productoCosto": 150.5,
        "productoGanancia": 15,
        "productoDescuento": 0,
        "productoExistencia": 1000,
        "productoImagen": "Ron-850.webp"
    }

]

meteraMongo(elemento)