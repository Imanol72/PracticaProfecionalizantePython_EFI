from app import db

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50),nullable =True)
    
    def __str__(self):
        return self.nombre
    
class Tipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    
    def __str__(self):
        return f"Tipo {self.nombre}"
    
class Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50), nullable=False)
    anio_fabricacion = db.Column(db.Integer)
    precio = db.Column(db.Integer)
    
    #Pertenece a una marca y a un tipo 
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo.id'), nullable=False)
    
    #Relacion directa con otro objeto 
    marca = db.relationship("Marca", backref=db.backref("vehiculos", lazy=True))
    tipo = db.relationship("Tipo", backref=db.backref("vehiculos", lazy=True))
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable = False)
    password_hash = db.Column(db.String(256),nullable = False)   #contraseña hasheada
    is_admin = db.Column(db.Boolean, default=True)
    
    def __str__(self):
        return self.username