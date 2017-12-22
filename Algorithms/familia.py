import json
import uuid


class Pessoa(object):
    pessoas = {}

    def __init__(self, nome, filhos=None, id=None):
        self.nome = nome
        self.filhos = filhos or []
        self.id = id or str(uuid.uuid4())
        Pessoa.pessoas[self.id] = self

    def to_dict(self):
        return {
            "nome": self.nome,
            "filhos": self.filhos,
        }

    def __repr__(self):
        return "<{}>".format(self.nome)

    @staticmethod
    def salva_pessoas():
        pessoas_serializadas = {pessoa.id: pessoa.to_dict()
                                for pessoa in Pessoa.pessoas.itervalues()}
        with open("pessoas.json", "w") as file:
            json.dump(pessoas_serializadas, file, indent=4)

    @staticmethod
    def carrega_pessoas():
        with open("pessoas.json", "r") as file:
            pessoas_serializadas = json.load(file)
            for id, dados in pessoas_serializadas.iteritems():
                Pessoa(nome=dados['nome'], filhos=dados['filhos'], id=id)

#Pessoa.carrega_pessoas()
