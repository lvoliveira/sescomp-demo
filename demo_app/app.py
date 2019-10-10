import os

from flask import Flask
from flask_restalchemy import Api

from declarative import db
from model.acordo_leniencia import AcordoLeniencia
from model.empresa import Empresa
from serializer.acordo_leniencia import AcordoLenienciaSerializer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db.init_app(app)

api = Api(app)

api.add_model(Empresa)
api.add_model(AcordoLeniencia, serializer_class=AcordoLenienciaSerializer)
api.add_relation(Empresa.acordoLeniencia, serializer_class=AcordoLenienciaSerializer)


@app.route("/")
def hello():
    return u'Olá mundo!'


@app.route("/init_db")
def create_db():
    db.create_all()
    return 'Banco iniciado'
