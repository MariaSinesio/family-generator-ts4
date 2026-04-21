from flask import Flask, render_template
from script import generate_sim

app = Flask(__name__) # Isso aqui basicamente diz: "Ou, acorda", o name é o nome do modulo atual, é uma forma mais simples de dizer

@app.route("/")

def home(): 
    return render_template("index.html") # Define a rota da página principal e renderiza ela

