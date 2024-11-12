from ma import ma
from models.peca import PecaModel

class PecaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PecaModel
        load_instance = True