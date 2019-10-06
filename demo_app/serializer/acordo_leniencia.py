from flask_restalchemy.serialization import ModelSerializer, NestedModelField

from model.empresa import Empresa


class AcordoLenienciaSerializer(ModelSerializer):

    empresa = NestedModelField(Empresa)
