from datetime import timedelta

from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt 
)
from werkzeug.security import(
    generate_password_hash,
    check_password_hash,
)

from app import db
from models import User
from schemas import UserSchema

auth_bp = Blueprint('auth', __name__)#Registramos un Blueprint

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.authorization #Recibo la data del post
        if not data or not data.username or not data.password:
            return jsonify({"Mensaje": "Faltan credenciales o no se enviaron correctamente"}), 400
        
        username = data.username
        password = data.password
        
        usuario = User.query.filter_by(username=username).first()

        if usuario and check_password_hash(usuario.password_hash,password):
            access_token=create_access_token(#crea token
                identity=username,
                expires_delta=timedelta(minutes=10),
                additional_claims=dict(
                    is_admin=usuario.is_admin
                )
            )
            return jsonify({"Token": access_token}), 200
        return jsonify({"Mensaje": "La contraseña es incorrecta"}), 401
    return jsonify({"Mensaje": "Utiliza el método POST para autenticarte"}), 405


@auth_bp.route('/usuario', methods=['POST', 'GET'])
#Decoradores agregan funcionalidad a las funciones
@jwt_required()
def user():
    if request.method == 'POST':
        usuarios = User.query.all
        
        return UserSchema().dump(obj=usuarios)
        additional_data = get_jwt()
        administrador = additional_data.get('administrador')
        if administrador is True:
            data = request.get_json()
            username = data.get('nombre_usuario')
            password = data.get('password')

            password_hasheada = generate_password_hash(
                password=password,
                method='pbkdf2',
                salt_length=8,
            )
            try:
                nuevo_usuario = User(
                    username=username,
                    password_hash=password_hasheada
                )
                db.session.add(nuevo_usuario)
                db.session.commit()

                return jsonify({"Usuario Creado": username}), 201
            except:
                return jsonify({"Error": "Algo salio mal"})
        return jsonify(Mensaje="Ud no esta habilitado para crear un usuario")
    usuarios = User.query.all()
    usuario_list = []
    for usuario in usuarios:
        usuario_list.append(
            dict(
                username=usuario.username,
                is_admin=usuario.is_admin,
                id=usuario.id
            )
        )
    return jsonify(usuario_list)
