"""
    INSTITUTO FEDERAL DE MINAS GERAIS - CAMPUS FORMIGA
    Jonathan Arantes Pinto <tlc.jooker@gmail.com>
    Saulo Cassiano <>
"""

import json
from estrutura_afn import Estado, Automato
from graphviz import Digraph

"""
FORMATO DO ARQUIVO DE DADOS JSON

{
    "af": [
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
    ],
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
            estados.append(Estado(nome, '1', []))
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
            automato.addEstado(e)
    return automato, data['r']

"""
    pintar_etapa:
    Gera uma imagem do automato dado como entrada, colore
    o estado indicado e suas transicoes
"""
def pintar_etapa(estado: str, automato: Automato, etapa: int):
    dot = Digraph()
    for est in automato.automato:
        if est.nome == estado:
            dot.node_attr.update(color='red')
        else:
            dot.node_attr.update(color='black')
        dot.node(est.nome, label = est.nome)
        for transicao in est.transicoes:
            if transicao[1] == estado:
                dot.edge_attr.update(color='red')
            else: dot.edge_attr.update(color='black')
            dot.edge(estado.nome, transicao[1], label = transicao[0])
    dot.attr(label = 'Etapa #' + str(etapa))
    dot.render('saida/etapa' + str(etapa) + '.gv')