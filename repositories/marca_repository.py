from app import db

from models import Marca

class MarcaRepository:
    
    def get_all(self):
        return Marca.query.all()
    
    def create(self, nombre):#Creamos un metodo que crea una marca en la base de datos -solo le pega a la base de datos-
        nueva_marca = Marca(nombre = nombre)
        db.session.add (nueva_marca)#Agrega archivos y los carga al stach (marcas que se agregan a la base de datos)
        db.session.commit ()#Agrega marcas a la base de datos
        return nueva_marca