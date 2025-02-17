'''App controlador quién maneja la lógica, las rutas del CRUD, las peticiones del usuario,
se conecta y comunica con la DB en model.py gestionando las operaciones con SQLAlchemy y renderiza 
las plantillas HTML.'''

from flask import Flask, render_template, request, redirect, url_for
from model import dbase, Usuario

app = Flask(__name__) # crea la aplicación Flask

'''Configurar la DB SQLite'''
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usuarios.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
dbase.init_app(app) # Inicia SQLAlchemy y conecta la DB con FLask

# Crear la base de datos
with app.app_context(): 
    dbase.create_all() # Al ejecutar se crea la Tabla (usuario) juntos con sus campos


'''Ruta principal donde está la lista de los usuarios'''
@app.route("/") # Leer
def index(): # Funcion index
    usuarios = Usuario.query.all() # Obtiene todos los usuarios
    return render_template("index.html", usuarios=usuarios)


# @app.route es un decorador 
@app.route("/crear", methods=["GET", "POST"]) # Recibe solicitudes (Mostrar y Procesar)
def crear():  # Crear usuario

    if request.method == "POST":   
        nombre = request.form["nombre"] # Captura el dato enviado desde el formulario
        edad = request.form["edad"]
        telefono = request.form["telefono"]
        email = request.form["email"]
        descripcion = request.form["descripcion"]
        nuevo_usuario = Usuario(nombre=nombre, edad=int(edad), telefono=telefono, email=email, descripcion=descripcion)  # type: ignore (ignorar error en parametros)
        dbase.session.add(nuevo_usuario)
        dbase.session.commit() # Para guardar datos en la DB de forma permanente
        return redirect(url_for("index"))
    
    return render_template("formulario.html")


@app.route("/editar/<int:id>", methods=["GET", "POST"]) # Actualizar usuario
def editar(id):
    usuario = Usuario.query.get(id) # Obtiene un Usuario por determinado id

    if usuario is None:
        return "Usuario no encontrado", 404  # Devuelve un error si no existe

    if request.method == "POST": # Detectar si el usuario envió un formulario 
        usuario.nombre = request.form["nombre"]
        usuario.edad = int(request.form["edad"])
        usuario.telefono = request.form["telefono"]
        usuario.email = request.form["email"]
        usuario.descripcion = request.form["descripcion"]
        dbase.session.commit()
        return redirect(url_for("index"))  
        # Redirige a la función index ya que genera una URL de la ruta usando el nombre de la función,
        # en vez de escribir manualmente la URL.
    
    return render_template("formulario.html", usuario=usuario)


@app.route("/eliminar/<int:id>") # Borrar usuario por id
def eliminar(id):
    usuario = Usuario.query.get(id)
    dbase.session.delete(usuario)
    dbase.session.commit()
    return redirect(url_for("index"))

# Mensaje de confirmación
print("📦 Base de datos creada con éxito.")

# Inicia la aplicación
if __name__ == "__main__":
    app.run(debug=True)

'''sqlite3 usuarios.db
sqlite> .tables
sqlite> SELECT * FROM usuario;  
para la terminal si esta sqlite instalado'''