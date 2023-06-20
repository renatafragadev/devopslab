import random
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps"

@app.route("/random")
def list_names(): 
    randon_value = random.random()
    return str(randon_value)