from flask import Flask, render_template, url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

#configuracion de SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/repaso_flask_primer_semestre"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)



from models import Marca, Pais, Caracteristica, Stock, Accesorio, Persona, Fabricante, Equipo, Modelo, Proveedor


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/equipos_list', methods=["POST","GET"])
def equipos():
    equipos = Equipo.query.all()
    modelos = Modelo.query.all()
    fabricantes = Fabricante.query.all()
    equipo_nuevo = None
    if request.method == 'POST':
        nombre = request.form["nombre"]
        categoria = request.form["categoria"]
        costo = request.form["costo"]
        modelo_id = request.form["modelos"]
        fabricante_id = request.form["fabricantes"]
        try:
            fabricante_id = int(fabricante_id)  # Asegurarse de que el ID del fabricante es un entero
            modelo_id = int(modelo_id)
            equipo_nuevo = Equipo(nombre = nombre, categoria = categoria, costo = costo, modelo_id = modelo_id, fabricante_id = fabricante_id)
            db.session.add(equipo_nuevo)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e), 500
        
        return redirect (url_for("equipos"))
    
    return render_template('equipos_list.html', equipos=equipos, modelos = modelos, fabricantes = fabricantes, equipo_nuevo = equipo_nuevo)

@app.route('/accesorio_list', methods=['POST', 'GET'])
def accesorios():
    equipos = Equipo.query.all()
    accesorios = Accesorio.query.all()

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        compatibilidad = request.form.get('compatibilidad') == 'true'
        equipo_id = request.form.get('Equipos')

        nuevo_accesorio = Accesorio(
            nombre=nombre,
            compatibilidad=compatibilidad,
            equipo_id=equipo_id
        )
        db.session.add(nuevo_accesorio)
        db.session.commit()

        return redirect(url_for('accesorios'))

    return render_template('accesorio_list.html', accesorios=accesorios, equipos=equipos)

@app.route('/caracteristica_list', methods=['POST', 'GET'])
def caracteristicas():
    equipos = Equipo.query.all()
    caracteristicas = Caracteristica.query.all()
    selected_equipo_id = None

    if request.method == 'POST':
        selected_equipo_id = request.form.get('equipo_id')
        caracteristicas = Caracteristica.query.filter_by(equipo_id=selected_equipo_id).all()
        
        if 'agregar_caracteristica' in request.form:
            nueva_caracteristica = request.form.get('nueva_caracteristica')
            descripcion = request.form.get('descripcion')
            nueva_caracteristica_entry = Caracteristica(
                equipo_id=selected_equipo_id,
                caracteristicas=nueva_caracteristica,
                descripcion=descripcion
            )
            db.session.add(nueva_caracteristica_entry)
            db.session.commit()
            caracteristicas = Caracteristica.query.filter_by(equipo_id=selected_equipo_id).all()

    return render_template('caracteristica_list.html', equipos=equipos, caracteristicas=caracteristicas, selected_equipo_id=selected_equipo_id)

@app.route('/fabricante_list', methods=['POST', 'GET'])
def fabricantes():
    fabricantes = Fabricante.query.all()
    paises = Pais.query.all()
    if request.method == 'POST':
        fabricante_nombre = request.form['nombre']
        pais_id = request.form['pais']
        if not fabricante_nombre or not pais_id:
            return "Datos incompletos", 400
        nuevo_fabricante = Fabricante(nombre=fabricante_nombre, pais_id=pais_id)
        db.session.add(nuevo_fabricante)
        db.session.commit()
        return redirect(url_for('fabricantes'))
    return render_template('fabricante_list.html', fabricantes=fabricantes, paises=paises)

@app.route('/marca_list', methods=["POST","GET"])
def marcas():
    marcas = Marca.query.all()
    fabricantes = Fabricante.query.all()
    if request.method=="POST":
        nombre = request.form["nombre"]
        categoria = request.form["categoria"]
        fabricante_id = request.form["fabricante_id"]
        if not nombre or not categoria or not fabricante_id:
            return "Datos incompletos", 400
        
        try:
            fabricante_id = int(fabricante_id)  # Asegurarse de que el ID del fabricante es un entero
            nueva_marca = Marca(nombre=nombre, categoria=categoria, fabricante_id=fabricante_id)
            db.session.add(nueva_marca)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e), 500
        return redirect(url_for("marcas"))
    return render_template('marca_list.html', marcas = marcas, fabricantes = fabricantes)

@app.route('/modelo_list', methods=["POST","GET"])
def modelos():
    modelos = Modelo.query.all()
    marcas = Marca.query.all()
    if request.method=="POST":
        nombre = request.form["nombre"]
        marca_id = request.form["marca_id"]

        print(f"Datos recibidos: nombre={nombre}, marca_id={marca_id}")

        if not nombre or not marca_id:
            return "Datos incompletos", 400
        try:
            marca_id = int(marca_id)
            marca = Marca.query.get(marca_id)
            if not marca:
                return "Marca no existe", 400
            
            modelo_nuevo = Modelo(
                nombre=nombre,
                marca_id=marca_id
            )
            db.session.add(modelo_nuevo)
            db.session.commit()
            return redirect(url_for("modelos"))

        except Exception as e:
            db.session.rollback()
            return f"Error al crear el modelo: {str(e)}", 400
    
    return render_template('modelo_list.html', modelos=modelos, marcas=marcas)
        

@app.route('/proveedor_list', methods=["POST","GET"])
def proveedor_list():
    proveedores = Proveedor.query.all()
    if request.method == 'POST':
            nueva_razon_social = request.form['razon_social']
            nuevo_telefono = request.form['telefono']
            nuevo_mail = request.form['mail']
            nuevo_cuit = request.form['cuit']
            nuevo_proveedor = Proveedor(
                razon_social=nueva_razon_social,
                telefono=nuevo_telefono,
                mail=nuevo_mail,
                cuit=nuevo_cuit,
            )
            db.session.add(nuevo_proveedor)
            db.session.commit()
            return redirect(url_for('proveedor_list'))
    return render_template('proveedor_list.html', proveedores=proveedores)

@app.route('/proveedor/editar/<int:id>', methods=['POST'])
def editar_proveedor(id):
    proveedor = Proveedor.query.get(id)
    if proveedor:
        proveedor.razon_social = request.form['razon_social']
        proveedor.telefono = request.form['telefono']
        proveedor.mail = request.form['mail']
        proveedor.cuit = request.form['cuit']
        db.session.commit()
    return redirect(url_for('proveedor_list'))

@app.route('/proveedor/eliminar/<int:id>', methods=['POST'])
def eliminar_proveedor(id):
    proveedor = Proveedor.query.get(id)
    if proveedor:
        db.session.delete(proveedor)
        db.session.commit()
    return redirect(url_for('proveedor_list'))

@app.route('/stock', methods=['GET', 'POST'])
def stock():
    equipos = Equipo.query.all()
    stocks = Stock.query.all()

    if request.method == 'POST':
        equipo_id = request.form.get('equipo_id')
        cantidad_disponible = request.form.get('cantidad_disponible')
        cantidad_minima = request.form.get('cantidad_minima')
        ubicacion_almacen = request.form.get('ubicacion_almacen')

        if equipo_id:
            equipo_id = int(equipo_id)
            # Aquí se pasa equipo_id al constructor de Stock
            nuevo_stock = Stock(
                equipo_id=equipo_id,
                cantidad_disponible=cantidad_disponible,
                cantidad_minima=cantidad_minima,
                ubicacion_almacen=ubicacion_almacen
            )
            db.session.add(nuevo_stock)
            db.session.commit()
        else:
            flash('Por favor selecciona un equipo válido.', 'error')

        return redirect(url_for('stock'))

    return render_template('stock.html', stocks=stocks, equipos=equipos)


