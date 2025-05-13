import Pyro5
import Pyro5.client
import Pyro5.api
import objetos

Pyro5.api.register_class_to_dict(objetos.objetoCRUD, objetos.converterParaDicionario)
Pyro5.api.register_dict_to_class("objetos.objetoCRUD", objetos.converterParaObjeto)

CRUD = Pyro5.client.Proxy("PYRONAME:CRUD")

if CRUD._pyroBind():
    print("temos objeto")
else:
    print("Deu ruim")

opcao = None
while opcao != 5:

    opcao = int(
        input(
            "Digite 1 para inserir, 2 pra buscar, 3 para atualizar, 4 para deletar, 5 pra sair: "
        )
    )
    match opcao:
        case 1:
            nome = input("Digite nome: ")
            classe = input("Digite classe: ")
            especie = input("Digite especie: ")
            nivel = int(input("Digite nível: "))
            personagem = objetos.objetoCRUD(nome, classe, especie, nivel)
            id = CRUD.adicionar(personagem)
            personagem.id = id
            print(
                personagem.id,
                personagem.nome,
                personagem.classe,
                personagem.especie,
                personagem.nivel,
            )
        case 2:
            id = int(input("Digite id de busca: "))
            personagem = CRUD.buscar(id)
            if personagem is not None:
                print(
                    personagem.id,
                    personagem.nome,
                    personagem.classe,
                    personagem.especie,
                    personagem.nivel,
                )
            else:
                print("Personagem não encontrado")
        case 3:
            id_upd = int(input("Digite ID para atualizar: "))
            # busca primeiro para mostrar valores atuais
            atual = CRUD.buscar(id_upd)
            if not atual:
                print("ID não existe.")
            else:
                print(
                    "Valores atuais:",
                    f"nome={atual.nome}, classe={atual.classe}, espécie={atual.especie}, nível={atual.nivel}",
                )
                # pede novos (ou ENTER para manter)
                novo_nome = input("Novo nome (ENTER para manter): ") or atual.nome
                nova_classe = input("Nova classe (ENTER para manter): ") or atual.classe
                nova_especie = (
                    input("Nova espécie (ENTER para manter): ") or atual.especie
                )
                novo_nivel_str = input("Novo nível (ENTER para manter): ")
                novo_nivel = int(novo_nivel_str) if novo_nivel_str else atual.nivel
                # cria objeto e chama atualizar
                p_upd = objetos.objetoCRUD(
                    novo_nome, nova_classe, nova_especie, novo_nivel, id_upd
                )
                resultado = CRUD.atualizar(p_upd)
                if resultado:
                    print(
                        f"Atualizado: ID={resultado.id}, nome={resultado.nome}, classe={resultado.classe}, espécie={resultado.especie}, nível={resultado.nivel}"
                    )
                else:
                    print("Falha na atualização.")
        case 4:
            id_rm = int(input("Digite ID para remover: "))
            p_rm = CRUD.remover(id_rm)
            if p_rm:
                print(f"Removido: ID={p_rm.id}, nome={p_rm.nome}")
            else:
                print("Falha na remoção (ID não existe).")
        case 5:
            break
