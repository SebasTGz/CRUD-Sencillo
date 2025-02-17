'''El modelo Define la estructura de la base de datos, permitiendo que Flask maneje los datos de los usuarios 
como objetos de Python, modelo de datos tipo ORM usado en Flask
'''
from flask_sqlalchemy import SQLAlchemy

'''Aquí se crea la instancia SQLAlchemy para manejar la DB y creamos la conexion'''
dbase = SQLAlchemy()

'''Definimos la clase usuario, la cual se convertirá en una tabla de DB'''
class Usuario(dbase.Model):
    id = dbase.Column(dbase.Integer, primary_key=True)
    nombre = dbase.Column(dbase.String(100), nullable=False)
    edad = dbase.Column(dbase.Integer, nullable=False)
    telefono = dbase.Column(dbase.String(10), nullable=False)
    email = dbase.Column(dbase.String(120), unique=True)
    descripcion = dbase.Column(dbase.Text) 

'''Una instancia es un objeto que se crea a partir de una clase.'''
#Pequeño cambio GH