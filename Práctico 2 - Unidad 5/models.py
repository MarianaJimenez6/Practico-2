from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
class Asistencia(db.Model):
    __tablename__ = 'asistencia'
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.String(80), nullable = False)
    codigoClase = db.Column(db.String(80), nullable = False)
    asistio = db.Column(db.String(80), nullable = False)
    justificacion = db.Column(db.String(80), nullable = True)
    idestudiante = db.Column(db.String(80), nullable = False)

class Curso(db.Model):
    __tablename__ = 'curso'
    id = db.Column(db.Integer, primary_key = True)
    #identificador = db.Column(db.String(80), nullable = False)
    anio = db.Column(db.String(80), nullable = False)
    division = db.Column(db.String(80), nullable = False)
    idpreceptor = db.Column(db.Integer, nullable = False)

class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(80), nullable = False)
    apellido = db.Column(db.String(80), nullable = False)
    dni =db.Column(db.String(80), nullable = False)
    idcurso = db.Column(db.Integer, nullable = False)

class Preceptor(db.Model):
    __tablename__ = 'preceptor'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(80), nullable = False)
    apellido = db.Column(db.String(80), nullable = False)
    correo = db.Column(db.String(80), unique = True, nullable = False)
    clave = db.Column(db.String(80), nullable = False) 

