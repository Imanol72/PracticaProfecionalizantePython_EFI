from app import db

    
class Tipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def _str_(self):
        return self.nombre 

class Pais(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    
    def __str__(self) -> str:
        return f"Pais {self.nombre}"
    
class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)
    pais = db.relationship('Pais', backref=db.backref('fabricantes', lazy=True))

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey("fabricante.id"), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    costo = db.Column(db.Integer, nullable=False)
    modelo = db.relationship('Modelo', backref=db.backref('modelos', lazy=True))
    fabricante = db.relationship('Fabricante', backref=db.backref('fabricantes', lazy=True))
    caracteristicas = db.relationship('Caracteristica', backref='equipo', lazy=True)

class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    marca = db.relationship("Marca", backref=db.backref("modelos", lazy=True))
    
class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)
    fabricante = db.relationship("Fabricante", backref=db.backref("marcas", lazy=True))
    

class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    caracteristicas = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(150), nullable=False)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    cantidad_disponible = db.Column(db.Integer, nullable=False)
    cantidad_minima = db.Column(db.Integer, nullable=False)
    ubicacion_almacen = db.Column(db.String(100), nullable=False)
    equipo = db.relationship('Equipo', backref=db.backref('stocks', lazy=True))

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=True)
    razon_social = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    cuit = db.Column(db.String(20), nullable=False)
class condicion_iva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)
    
class producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)
    
class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    accesorio = db.Column(db.String(100), nullable=False)
    compatibilidad = db.Column(db.Boolean)
    equipo = db.relationship('Equipo', backref=db.backref('accesorios', lazy=True))

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    documento = db.Column(db.String(20), nullable=False)
    genero = db.Column(db.String(10), nullable=False)

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)