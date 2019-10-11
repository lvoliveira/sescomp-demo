from flask import Flask
from flask_restalchemy import Api

from declarative import db
from model.acordo_leniencia import AcordoLeniencia
from model.empresa import Empresa
from serializer.acordo_leniencia import AcordoLenienciaSerializer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
db.init_app(app)

api = Api(app)

api.add_model(Empresa)
api.add_model(AcordoLeniencia, serializer_class=AcordoLenienciaSerializer)


@app.route("/")
def hello():
    return u'Olá mundo!'


@app.route("/init_db")
def create_db():
    db.drop_all()
    db.create_all()
    return 'Banco iniciado'
