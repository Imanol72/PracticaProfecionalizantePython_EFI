from flask import Blueprint, request

from models import Marca, Tipo, Vehiculo

from schemas import MarcaSchema, TipoSchema, VehiculoSchema

from app import db

vehiculos_bp = Blueprint('vehiculos', __name__)

@vehiculos_bp.route('/marcas', methods=['GET'])
def marcas():
    marcas=Marca.query.all()
    return MarcaSchema().dump(marcas, many=True)

@vehiculos_bp.route('/tipos', methods=['GET'])
def tipos():
    tipos=Tipo.query.all()
    return TipoSchema().dump(tipos, many=True)

@vehiculos_bp.route('/vehiculos', methods=['GET'])
def vehiculos():
    if request.method == "POST":
        data = request.get.json()
        errors = VehiculoSchema().validate(data)
        if errors:
            raise make_response(jsonfy(errors))
        
        nuevo_vehiculo = Vehiculo(
        modelo = data.get ('modelo'),
        anio_fabricacion = data.get ('anio_fabricacion'),
        precio = data.get ('precio'),
        marca_id = data.get ('marca_id'),
        tipo_id = data.get ('tipo_id')            
        )
        db.session.add(nuevo_vehiculo)
        db.session.commit()
        
    vehiculos=Vehiculo.query.all()
    return VehiculoSchema().dump(vehiculos, Vehiculoy=True)