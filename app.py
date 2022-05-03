#Importar herramientas necesarias de flask
from flask import Flask, render_template, abort,request

#Importar librería os para emplear environ
import os

#Importar json para lectura de MSX.json
import json

#Variable app por flask
app = Flask(__name__)

#Leer fichero json
with open("MSX.json") as fichero:
    games=json.load(fichero)

#Definir ruta de inicio
@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")


#Definir ruta juegos
@app.route('/juegos',methods=["GET","POST"])
def juegos():
    categorias=[]
    categorias.append("")
    for i in games:
        if i["categoria"] not in categorias:
            categorias.append(i["categoria"])
    categorias.sort()
    if request.method=="GET":
        return render_template("juegos.html",categorias=categorias)
    else:
        nombre=request.form.get("name")
        categoria=request.form.get("category")
        for i in games:
            if (nombre == "" or str(i["nombre"]).startswith(nombre)) and (categoria == "" or categoria == i["categoria"]):
                return render_template('juegos.html',juegos=games,nombre=nombre,categoria=categoria,categorias=categorias)
        return render_template('juegos.html',nombre=nombre,categoria=categoria,categorias=categorias)

#Definir ruta juego
@app.route('/juego/<int:identificador>',methods=["GET"])
def juego(identificador):
    for i in games:
        if i["id"] == identificador:
            return render_template('juego.html',juego=i)
    abort(404)

app.run('0.0.0.0', debug=False)