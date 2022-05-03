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
@app.route('/',methods=["GET","POST"])
def inicio():
    return render_template("inicio.html")

#Definir ruta de /juegos
@app.route('/listajuegos', methods=["POST"])
def listajuegos():
	cadena=request.form.get("name")
	juegos=[]
	desarrolladores=[]
	identificadores=[]
	for juego in games:
		if cadena in (str(juego["nombre"])):
			juegos.append(str(juego["nombre"]))
			desarrolladores.append(str(juego["desarrollador"]))
			identificadores.append(str(juego["id"]))
			filtro=zip(juegos,desarrolladores,identificadores)	
		elif cadena == "":
			juegos.append(juego["nombre"])
	return render_template("juegos1.html",juegos=filtro)


app.run('0.0.0.0', debug=False)