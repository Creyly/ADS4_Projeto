from db import db #Importa banco de dados

#Criação do modelo para peças
class PecaModel(db.Model):
    __tablename__ = 'pecas'

    #Adicionando tabelas ao db
    numero_peca = db.Column(db.String, primary_key=True, unique=True)
    descricao = db.Column(db.String(80), nullable=False)
    marca = db.Column(db.String(20), nullable=False)
    lote = db.Column(db.Integer, nullable=False)

    #Construção da classe
    def __init__(self, numero_peca, descricao, marca, lote):
        self.numero_peca = numero_peca
        self.descricao = descricao
        self.marca = marca
        self.lote = lote

    #Representação da classe
    def __repr__(self, ):
        return f'PecaModel(Numero peça = {self.numero_peca}, descrição={self.descricao}, marca={self.marca}, lote={self.lote})'

    #Transformação em json
    def json(self, ):
        return {
            'numero_peca': self.numero_peca,
            'descricao': self.descricao,
            'marca': self.marca, 
            'lote': self.lote
        }

    #busca por numero da peça
    @classmethod
    def find_by_peca(cls, numero_peca):
        return cls.query.filter_by(numero_peca = numero_peca).first()

    #Busca todos os itens do db
    @classmethod
    def find_all(cls):
        return cls.query.all()

    #Salva alterações no db
    def save_to_db(self, ):
        db.session.add(self)
        db.session.commit()

    #Deleta informações do db
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()