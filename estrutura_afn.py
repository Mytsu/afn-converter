class Estado(object):

    def __init__(self, nome=None, tipo=None, matriz_transicoes=None):
        self.nome = nome
        # 0 - Inicial. 1 - Intermediário, 2 - Final
        self.tipo = tipo
        # Lista de transições no formato (símbolo, nome do estado destino)
        self.transicoes = matriz_transicoes


class Automato(object):
    def __init__(self):
        # Vetor de estados
        self.automato = []

    def addEstado(self, estado):
        self.automato.append(Estado(estado[0], estado[1], estado[2]))

    def getAutomato(self):
        return self.automato

    def primeiro_passo(self):
        ini = Estado("I", 0, [])
        fin = Estado("F", 2, [])

        for i in range(len(self.getAutomato())):

            if self.automato[i].tipo == 0:
                self.automato[i].tipo = 1
                ini.transicoes.append(["None", self.automato[i].nome])

            elif self.automato[i].tipo == 2:
                self.automato[i].tipo = 1
                self.automato[i].transicoes.append(["None", fin.nome])

        self.addEstado([ini.nome, ini.tipo, ini.transicoes])
        self.addEstado([fin.nome, fin.tipo, fin.transicoes])

    def modificaTransicoes(self):
        for i in range(len(self.getAutomato())):
            for j in range(len(self.automato[i].transicoes)):
                if "," in self.automato[i].transicoes[j][0]:
                    aux = str(self.automato[i].transicoes[j][0])
                    aux = aux.replace(",", "+")
                    self.automato[i].transicoes[j][0] = aux
                    self.automato[i].transicoes[j][0] = "(" + self.automato[i].transicoes[j][0] + ")"

                if self.automato[i].transicoes[j][1] == self.automato[i].nome:
                    self.automato[i].transicoes[j][0] = self.automato[i].transicoes[j][0] + "*"

    def saida_do_vertice_deletado(self, no_deletado):
        for i in range(len(self.getAutomato())):
            if self.automato[i].nome == no_deletado:
                return self.automato[i].transicoes

    def lista_entrada_do_vertice_deletado(self, no_deletado):
        lista_estados = []
        for i in range(len(self.getAutomato())):
            if self.verifica_se_existe_ligacao(self.automato[i].nome, no_deletado) != -1:
                lista_estados.append(i)

        return lista_estados

    def verifica_laco_interno(self, no_deletado):
        for i in range(len(self.getAutomato())):
            if self.automato[i].nome == no_deletado:
                for j in range(len(self.automato[i].transicoes)):
                    if self.automato[i].transicoes[j][1] == no_deletado:
                        return self.automato[i].transicoes[j][0]

        return "None"

    def verifica_se_existe_ligacao(self, estado_inicial, estado_final):
        for i in range(len(self.getAutomato())):
            if self.automato[i].nome == estado_inicial:
                for j in range(len(self.automato[i].transicoes)):
                    if self.automato[i].transicoes[j][1] == estado_final:
                        return j

        return -1

    def substitui_estados(self, novo_no):
        for i in range(len(self.getAutomato())):
            if self.automato[i].nome == novo_no.nome:
                self.automato[i] = novo_no

        return self.automato

    def pega_estado(self, nome_estado):
        for i in range(len(self.getAutomato())):
            if self.automato[i].nome == nome_estado:
                return i

        return -1

    def simbolos_transicao(self, vetor_simbolos):
        simbolo = ''
        for i in range(len(vetor_simbolos)):
            if vetor_simbolos[i] != 'None':
                simbolo = simbolo + vetor_simbolos[i]

        if simbolo == '':
            return "None"
        else:
            return simbolo

    def remove_laco_interno(self, nome_no):
        posicao_ligacao = self.verifica_se_existe_ligacao(nome_no, nome_no)
        simbolo = self.verifica_laco_interno(nome_no)
        posicao_no = self.pega_estado(nome_no)
        self.automato[posicao_no].transicoes.pop(posicao_ligacao)
        for i in range(len(self.automato[posicao_no].transicoes)):
            if self.automato[posicao_no].transicoes[i][0] != "None":
                aux = simbolo + self.automato[posicao_no].transicoes[i][0]
                self.automato[posicao_no].transicoes[i][0] = aux
            else:
                self.automato[posicao_no].transicoes[i][0] = simbolo

        return self.automato

    def deleta_estado(self, deleta_nome):
        if self.verifica_laco_interno(deleta_nome) != "None":
            self.automato = self.remove_laco_interno(deleta_nome)

        posicao_no_vetor_do_no_deletado = self.pega_estado(deleta_nome)
        vertices_que_vao_ao_no = self.lista_entrada_do_vertice_deletado(deleta_nome)
        lista_transicoes_no_deletado = self.saida_do_vertice_deletado(deleta_nome)

        for i in range(len(vertices_que_vao_ao_no)):
            for j in range(len(lista_transicoes_no_deletado)):
                destino = self.automato[posicao_no_vetor_do_no_deletado].transicoes[j][1]
                if deleta_nome != destino:

                    nome_origem = self.automato[vertices_que_vao_ao_no[i]].nome
                    aux = ''
                    if nome_origem != deleta_nome:
                        aux = self.verifica_se_existe_ligacao(nome_origem, deleta_nome)
                        aux = self.automato[vertices_que_vao_ao_no[i]].transicoes[aux][0]

                    simbolo_destino = self.automato[posicao_no_vetor_do_no_deletado].transicoes[j][0]
                    aux = [aux, simbolo_destino]
                    simbolos_concatenados = self.simbolos_transicao(aux)

                    pos_ligacao = self.verifica_se_existe_ligacao(nome_origem, destino)
                    aux = self.automato[vertices_que_vao_ao_no[i]].transicoes[pos_ligacao][0]
                    if pos_ligacao != int(-1) and aux != "None":
                        aux = self.automato[vertices_que_vao_ao_no[i]].transicoes[pos_ligacao][0]
                        self.automato[vertices_que_vao_ao_no[i]].transicoes[pos_ligacao][0] = "(" + aux + \
                            "+" + simbolos_concatenados + ")"
                    else:
                        ligacao = [simbolos_concatenados, destino]
                        self.automato[vertices_que_vao_ao_no[i]].transicoes.append(ligacao)

            limpa_transicao = self.verifica_se_existe_ligacao(self.automato[vertices_que_vao_ao_no[i]].nome, deleta_nome)
            self.automato[vertices_que_vao_ao_no[i]].transicoes.pop(limpa_transicao)
        self.automato.pop(posicao_no_vetor_do_no_deletado)


t = []

automato = Automato()

t.append("1")
t.append(0)
aux = [["a", "2"], ["b", "3"]]
t.append(aux)
automato.addEstado(t)

t.clear()
t.append("2")
t.append(1)
aux = [["a", "4"], ["b", "2"]]
t.append(aux)
automato.addEstado(t)

t.clear()
t.append("3")
t.append(1)
aux = [["b", "4"]]
t.append(aux)
automato.addEstado(t)

t.clear()
t.append("4")
t.append(2)
aux = []
t.append(aux)
automato.addEstado(t)

automato.primeiro_passo()
automato.modificaTransicoes()
automato.deleta_estado('2')
automato.deleta_estado('3')
automato.deleta_estado('4')
automato.deleta_estado('1')

"""
t.append("1")
t.append(0)
aux = [["a", "1"], ["None", "2"]]
t.append(aux)
automato.addEstado(t)

t.clear()
t.append("3")
t.append(0)
aux = [["c", "3"], ["a,d", "2"]]
t.append(aux)
automato.addEstado(t)

t.clear()
t.append("2")
t.append(2)
aux = [["b", "2"], ["None", "3"]]
t.append(aux)
automato.addEstado(t)

automato.primeiro_passo()
automato.modificaTransicoes()
automato.deleta_estado("1")
automato.deleta_estado("3")
automato.deleta_estado("2")
"""
print("Final")
























