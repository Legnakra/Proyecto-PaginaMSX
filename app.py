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

app.run('0.0.0.0', debug=False)