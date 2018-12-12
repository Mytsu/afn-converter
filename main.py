
"""
    INSTITUTO FEDERAL DE MINAS GERAIS - CAMPUS FORMIGA
    Jonathan Arantes Pinto <tlc.jooker@gmail.com>
    Saulo Cassiano de Carvalho <saulocarvalho64@gmail.com>
"""

import json
from estrutura_afn import Estado, Automato
from graphviz import Digraph

"""
FORMATO DO ARQUIVO DE DADOS JSON
{
    "af": {
        "estados": ["1", "2", "3"],
        "alfabeto": ["a", "b", "c", "d"],
        "transicoes": [
            ["1", "a", "1"],
            ["1", "#", "2"],
            ["2", "b", "2"],
            ["2", "#", "3"],
            ["3", "c", "3"],
            ["3", "a", "2"],
            ["3", "d", "2"]
        ],
        "iniciais": ["1", "3"],
        "finais": ["2"]
    },
    "r": ["1", "3", "2"]
}
"""
"""
    carregar_arquivo:
    Lê um arquivo json para carregar o automato finito
    retorna um tipo Automato e uma lista com a ordem dos
    estados a serem deletados
"""


def carregar_arquivo(filename: str) -> (Automato, []):
    estados = []
    automato = Automato()
    with open(filename) as file:
        data = json.load(file)
        for nome in data['af']['estados']:
            estados.append(Estado(nome, 1, []))
        for e in estados:
            for inicial in data['af']['iniciais']:
                if e.nome == inicial:
                    e.tipo = 0
            for final in data['af']['finais']:
                if e.nome == final:
                    e.tipo = 2
            for tr in data['af']['transicoes']:
                if e.nome == tr[0]:
                    e.transicoes.append([tr[1], tr[2]])
            automato.addEstado([e.nome, e.tipo, e.transicoes])
    return automato, data['r']


"""
    pintar_etapa:
    Gera uma imagem do automato dado como entrada, colore
    o estado indicado e suas transicoes
"""


def pintar_etapa(aut: Automato, etapa: int = 0, estado: str = None):
    dot = Digraph()
    dot.attr('node', shape='doublecircle')
    for est in aut.getAutomato():
        if est.tipo == 2:
            dot.node(est.nome, label=est.nome)
    dot.attr('node', shape='circle')
    dot.node('I', style='invisible')
    for est in aut.getAutomato():
        if est.tipo == 0:
            dot.edge('I', est.nome, label='#')
        if est.tipo != 2 and est.tipo != 0:
            dot.node(est.nome, label=est.nome)
        for transicao in est.transicoes:
            dot.edge(est.nome, transicao[1], label=transicao[0])
    dot.attr(label='Etapa #' + str(etapa))
    dot.render('saida/etapa' + str(etapa) + '.gv')


if __name__ == '__main__':
    automato, lista = carregar_arquivo('teste.json')
    pintar_etapa(automato, 0, automato.automato[2].nome)
    # Deixando em ordem do tipo, influencia a ordem que deleta os estados
    automato.automato.sort(key=lambda x: x.tipo)
    automato.primeiro_passo()  # Acrescenta o estado "I" e "F"
    automato.modificaTransicoes()  # Aqui troca "," por "+" e coloca "*"

    et = 0
    while automato.automato[0].tipo != 0:
        pintar_etapa(automato, etapa=et, estado=automato.getAutomato()[0])
        automato.deleta_estado(automato.automato[0].nome)
        et += 1
    pintar_etapa(automato, etapa=et)

    print("Expression Regular is: " +
          str(automato.automato[0].transicoes[0][0]))
