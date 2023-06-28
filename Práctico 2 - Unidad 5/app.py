from flask import Flask, render_template,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
import hashlib
import json
from werkzeug.security import generate_password_hash,check_password_hash
from pprint import pprint

app = Flask(__name__)
# app.secret_key = 'GDtfDCFYjD'
app.config.from_pyfile('config.py')

from models import db, Asistencia as asistencia, Curso as curso, Estudiante as estudiante, Preceptor as preceptor

@app.route('/')
def entrar():
  return render_template('ingresaralSistema.html')

@app.route('/inicio/') 
def inicio(): 
  if not session.get("correo"):
    return redirect ("/")
  else:
    return render_template('inicio.html') 

@app.route('/LogIn/', methods=["POST", "GET"]) 
def registrar(): 
  if request.method == "POST":
    session["correo"] = request.form.get("correo")
    correo = request.form.get("correo")
    contraseña = request.form['clave']
    clave = hashlib.md5(bytes(contraseña, encoding='utf-8'))
    prec = preceptor.query.filter(preceptor.correo == session["correo"]).first()
    session['nombre'] = prec.nombre
    session['apellido'] = prec.apellido
    session['idpreceptor'] = prec.id
    return redirect ('/inicio/')
  else:
    return render_template('ingresaralSistema.html')

@app.route('/RegistrarAsistencia/')
def registrarAsistencia():
  if not session.get("correo"):
    return redirect ("/")
  else:
    cursos = curso.query.filter(curso.idpreceptor == session.get("idpreceptor")).all()
    return render_template('cursos.html', cursos = cursos)

@app.route('/RegistroAsistencia/', methods=["POST", "GET"])
def registrarAsistencia2():
  if not session.get("correo"):
    return redirect ("/")
  else:
    curso = request.form['curso']
    fecha = request.form['fecha']
    codigoclase = request.form['codigoclase']
    
    estudiantes = estudiante.query.filter(estudiante.idcurso == curso).order_by(estudiante.apellido).all()
    return render_template ('registrarAsistencia.html', estudiantes = estudiantes, curso = curso, fecha = fecha, codigoclase = codigoclase)
  
@app.route("/RegistrarAsistencia3/", methods=["POST", "GET"])
def registrar3():
  if not session.get("correo"):
    return redirect ("/")
  else:
    justificacion = request.form.getlist('justificacion[]')
    asistio = request.form.getlist('asistio[]')
    idestudiante = request.form.getlist('idestudiante[]')
    codigoclase = request.form['codigoclase']
    fecha = request.form['fecha']
    
    for i in range(len(asistio)):
      unaAsistencia = asistencia(asistio = asistio[i], justificacion = justificacion[i], fecha = fecha, codigoclase = codigoclase, idestudiante = idestudiante[i])
      db.session.add(unaAsistencia)
    db.session.commit()
    return redirect ('/inicio/')

@app.route("/MostrarAsistencia/", methods=["POST", "GET"])
def mostrarAsistenciaRegistrada():
  if not session.get("correo"):
    redirect ("/")
  else:
    cursos = curso.query.filter(curso.idpreceptor == session.get("idpreceptor")).all()
    return render_template('mostrarAsistencia.html', cursos = cursos)

@app.route("/MuestraAsistencia/", methods=["POST", "GET"])
def muestraAsistencias():
  if not session.get("correo"):
    redirect ("/")
  else:
    fecha = request.form['fecha']
    curso = request.form['curso']
    codigoclase = request.form['codigoclase']
    pprint(fecha)
    estudiantes = estudiante.query.filter(estudiante.idcurso == curso).order_by(estudiante.apellido).all()
    asistencias = asistencia.query.filter(asistencia.codigoclase == codigoclase, asistencia.fecha == fecha).all()
    return render_template('muestraAsistencia.html',asistencias = asistencias,estudiantes = estudiantes,fecha = fecha, curso = curso, codigoclase =codigoclase)

@app.route('/cursosInforme/', methods=["POST", "GET"])
def informe():
  if not session.get("correo"):
    redirect ("/")
  else:
    cursos = curso.query.filter(curso.idpreceptor == session.get("idpreceptor")).all()
    return render_template('cursosInforme.html', cursos = cursos)

@app.route("/InformeAsistencias/", methods=["POST", "GET"])
def generarInforme():
  if not session.get("correo"):
    redirect ("/")
  else:
    idcurso = request.form['idcurso']
    estudiantes = estudiante.query.filter(estudiante.idcurso == idcurso).order_by(estudiante.apellido).all()
    asistencias = asistencia.query.all()
    return render_template('informeAsistencias.html', estudiantes = estudiantes,asistencias = asistencias, idcurso = idcurso)

@app.route('/logOut/')
def logOut():
  session["name"] = None
  return redirect ('/')

if __name__ == '__main__': 
  with app.app_context():
    db.create_all()
    app.run(debug=True)
