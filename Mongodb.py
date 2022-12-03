import pymongo
from configur import  variables
class PyMongo():
    def __init__(self,variables):
        self.MONGO_DATABASE=variables["db"]
        self.MONGO_URL = 'mongodb://' + variables["host"] + ':' + str(variables["port"])
        self.MONGO_CLIENT = None
        self.MONGO_RESPUESTA = None
        self.MONGO_TIMEOUT=variables["timeout"]
    def conectar_MongoDB(self):
        try:
            self.MONGO_CLIENT = pymongo.MongoClient(self.MONGO_URL, serverSelectionTimeoutMS=self.MONGO_TIMEOUT)
            #Mongo_Respuesta = Mongo_client[bd]["Producto"].find({})
            # for reg in Mongo_Respuesta:
            #     print(reg['nombre'])
        except Exception as error:
            print("Esto no jala: ", error)
        else:
            print("CONEXION Para servidor de MongoBD realizada")
            pass

    def desconectar_MongoBD(self):
        if self.MONGO_CLIENT:
            self.MONGO_CLIENT.close()
    def Eliminar(self,tabla, filtro):
        response={"startus":False}
        self.MONGO_RESPUESTA=self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].delete_one(filtro)
        if  self.MONGO_RESPUESTA:
            return self.MONGO_RESPUESTA
        else:
            return None
    def consulta_MongoBD(self,tabla,filtro,atributos={"_id":0}):
        response={"status":False,"resultado":[]}
        self.MONGO_RESPUESTA = self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].find(filtro,atributos)
        if self.MONGO_RESPUESTA:
            response["status"]=True
            for reg in self.MONGO_RESPUESTA:
                response["resultado"].append(reg)
        return  response
            # for reg in self.MONGO_RESPUESTA:
            #     print(reg['nombre'])

    # def Incertar_estudiante(self,est):
    #     self.Mongo_Respuesta = self.Mongo_client[self.MONGO_DATABASE]["Estudiante"].incertOne({est})
    #     if self.Mongo_Respuesta:
    #         return True
    #     else:
    #         return False

    def insertar(self, tabla, documento):
        self.MONGO_RESPUESTA = self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].insert_one(documento)
        if self.MONGO_RESPUESTA:
            return self.MONGO_RESPUESTA
        else:
            return None
    def actualizar(self,tabla,filtro,nuevos_valores):
        response={"status":False}
        self.MONGO_RESPUESTA=self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].update_many(filtro,nuevos_valores)
        if self.MONGO_RESPUESTA:
            response["status"]=True
            # return  self.MONGO_RESPUESTA
        # else:
        #     return None
        return  response
    def Octener_Promedio(self,tabla):
        response = {"status": False, "resultado": []}
        self.MONGO_RESPUESTA = self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].aggregate(
            [
              {
                "$group": {
                  "_id": '$control',
                  "promedio": {
                    "$avg":"$calificacion"
                  }
                }
              }
            ])
        if self.MONGO_RESPUESTA:
            response["status"] = True
            for reg in self.MONGO_RESPUESTA:
                response["resultado"].append(reg)
        return response
        # for reg in self.MONGO_RESPUESTA:
        #     print(reg['nombre'])
alumno={
    "control":200,
    "nombre":"Juan"
}


# actualizar documentos en la colecion


obj=PyMongo(variables)
obj.conectar_MongoDB()
obj.desconectar_MongoBD()