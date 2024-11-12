from flask import jsonify
from marshmallow import ValidationError

from ma import ma
from db import db
from controllers.peca import Peca, PecaList

from server.instance import server 

api = server.api 
app = server.app

@app.before_request
def create_tables():
    db.create_all()

api.add_resource(Peca, '/pecas/<string:numero_peca>')
api.add_resource(PecaList, '/pecas/')


#Comando padrão, serve para iniciar o app
if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()
