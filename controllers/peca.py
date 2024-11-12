from flask import request
from flask_restx import Resource, fields

from models.peca import PecaModel
from schemas.peca import PecaSchema

from server.instance import server

peca_ns = server.peca_ns

peca_schema = PecaSchema()
peca_list_schema = PecaSchema(many=True)

ITEM_NOT_FOUND = 'Item não encontrado'

item = peca_ns.model('Peca', {
    'numero_peca': fields.String(description='Número peça'),
    'descricao': fields.String(description='Descrição'),
    'marca': fields.String(description='Marca'),
    'lote': fields.Integer(description='Lote')
})

class Peca(Resource):

    def get(self, numero_peca):
        peca_data = PecaModel.find_by_peca(numero_peca)
        if peca_data:
            return peca_schema.dump(peca_data), 200
        return {'message': ITEM_NOT_FOUND}, 404

class PecaList(Resource):
    def get(self, ):
        return peca_list_schema.dump(PecaModel.find_all()), 200


    @peca_ns.expect(item)
    @peca_ns.doc('Criar um item') #Documentação
    def post(self, ):
        peca_json = request.get_json()
        peca_data = peca_schema.load(peca_json)

        peca_data.save_to_db()

        return peca_schema.dump(peca_data), 201

