class objetoCRUD:

    def __init__(self, nome, classe, especie, nivel, id=None):
        self.nome = nome
        self.classe = classe
        self.especie = especie
        self.nivel = nivel
        self.id = id


def converterParaDicionario(objeto: objetoCRUD) -> dict:
    return {
        "__class__": "objetos.objetoCRUD",
        "id": objeto.id,
        "nome": objeto.nome,
        "classe": objeto.classe,
        "especie": objeto.especie,
        "nivel": objeto.nivel,
    }


def converterParaObjeto(classname, dicionario: dict):
    personagem = objetoCRUD(
        dicionario["nome"],
        dicionario["classe"],
        dicionario["especie"],
        dicionario["nivel"],
        dicionario["id"],
    )
    return personagem
