#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random
#from flask import Flask
#app = Flask(__name__)

#@app.route("/")
#def hello():
#    return app.send_static_file("index.html")
    
print("hello world")

import random

lista = ["piedra", "papel", "tijera"]
x = input("piedra papel o tijera?:")
y = random.choice(lista)

if x == y:
    print("Empate")
elif x == "piedra" and y == "papel": 
    print("Perdiste, papel le gana a piedra")
elif x == "piedra" and y == "tijera":
    print("Ganaste, piedra le gana a tijera")
elif x == "papel" and y == "piedra":
    print("Ganaste, papel le gana a piedra")
elif x == "papel" and y == "tijera":
    print("Perdiste, tijera le gana a papel")
elif x == "tijera" and y == "piedra":
    print("Perdiste, piedra le gana a tijera")
elif x == "tijera" and y == "papel":
    print("Ganaste, tijera le gana a papel")
else:
    print("No es una opción válida")
    

