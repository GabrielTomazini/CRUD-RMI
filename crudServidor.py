import Pyro5
import Pyro5.api
import Pyro5.core
import Pyro5.server
import Pyro5.nameserver
import bd
import objetos


@Pyro5.server.expose
class CRUD:
    def __init__(self):
        self.banco = bd.Banco()

    def adicionar(self, personagem: objetos.objetoCRUD) -> int:
        id = self.banco.adicionar(
            personagem.nome, personagem.classe, personagem.especie, personagem.nivel
        )
        return id

    def buscar(self, id: int):
        tupla = self.banco.buscar(id)
        if tupla is not None:
            personagem = objetos.objetoCRUD(
                tupla[1],
                tupla[2],
                tupla[3],
                tupla[4],
                tupla[0],
            )
            return personagem
        else:
            return None

    def atualizar(self, personagem: objetos.objetoCRUD) -> objetos.objetoCRUD | None:
        # retorna nova tupla ou None
        tupla = self.banco.atualizar(
            personagem.id,
            personagem.nome,
            personagem.classe,
            personagem.especie,
            personagem.nivel,
        )
        if tupla:
            return objetos.objetoCRUD(tupla[1], tupla[2], tupla[3], tupla[4], tupla[0])
        return None

    def remover(self, id: int) -> objetos.objetoCRUD | None:
        tupla = self.banco.remover(id)
        if tupla:
            return objetos.objetoCRUD(tupla[1], tupla[2], tupla[3], tupla[4], tupla[0])
        return None


def main():
    daemon = Pyro5.server.Daemon()
    localizacao = daemon.register(CRUD)

    Pyro5.api.register_class_to_dict(
        objetos.objetoCRUD, objetos.converterParaDicionario
    )
    Pyro5.api.register_dict_to_class("objetos.objetoCRUD", objetos.converterParaObjeto)

    ns = Pyro5.core.locate_ns()
    ns.register("CRUD", localizacao)

    daemon.requestLoop()


if __name__ == "__main__":
    main()
