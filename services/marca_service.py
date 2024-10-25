from repositories.marca_repository import MarcaRepository

class MarcaService:
    def __init__(self, marca_repository: MarcaRepository):#inicializa el servicio (inicialmente tiene esto)
        self._marca_repository = marca_repository
    
    def get_all(self):
        return self._marca_repository.get_all()
    
    def create(self, nombre):#Metodo recibe nombre
        return self._marca_repository.create(nombre)