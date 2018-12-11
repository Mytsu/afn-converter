"""
    INSTITUTO FEDERAL DE MINAS GERAIS - CAMPUS FORMIGA
    Jonathan Arantes Pinto <tlc.jooker@gmail.com>
    Saulo Cassiano de Carvalho <saulocarvalho64@gmail.com>
"""


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

    # Nesta função é adicionado o estado "Inicial" e "Final"
    def primeiro_passo(self):
        ini = Estado("I", 0, [])
        fin = Estado("F", 2, [])

        for i in range(len(self.getAutomato())):
            #Pegando todos iniciais e fazendo o "Inicial" tem uma ligação neles
            if self.automato[i].tipo == 0:
                self.automato[i].tipo = 1
                ini.transicoes.append(["#", self.automato[i].nome])

            #Pegando todos finais e ligando eles ao estado "Final"
            elif self.automato[i].tipo == 2:
                self.automato[i].tipo = 1
                self.automato[i].transicoes.append(["#", fin.nome])

        self.addEstado([ini.nome, ini.tipo, ini.transicoes])
        self.addEstado([fin.nome, fin.tipo, fin.transicoes])

    #Função que modifica os estados, em caso de hoiver vígulas entre os símbolos de transição e fecho
    def modificaTransicoes(self):
        for i in range(len(self.getAutomato())):
            for j in range(len(self.automato[i].transicoes)):
                if "," in self.automato[i].transicoes[j][0]:
                    aux = str(self.automato[i].transicoes[j][0])
                    aux = aux.replace(",", "+") #Substituindo na string a vírgula por símbolo "+"
                    self.automato[i].transicoes[j][0] = aux
                    self.automato[i].transicoes[j][0] = "(" + self.automato[i].transicoes[j][0] + ")"

                if self.automato[i].transicoes[j][1] == self.automato[i].nome:
                    self.automato[i].transicoes[j][0] = self.automato[i].transicoes[j][0] + "*" #Adicionando símbolo de fecho"

    #Função que pega todas transições que saem do estado que será deletado
    def saida_do_vertice_deletado(self, no_deletado):
        for i in range(len(self.getAutomato())):
            if self.automato[i].nome == no_deletado:
                return self.automato[i].transicoes

    #Função que retorna todos nomes dos vértices que tem transição para o estado a ser deletado
    def lista_entrada_do_vertice_deletado(self, no_deletado):
        lista_estados = []
        for i in range(len(self.getAutomato())):
            if self.verifica_se_existe_ligacao(self.automato[i].nome, no_deletado) != -1:
                lista_estados.append(i) #Todos os nomes dos estados que recebem transição serão adicionados na lista

        return lista_estados

    #Função que verifica se o estado tem ligação saindo dele para ele mesmo, caso não tenha retornará uma string "#"
    def verifica_laco_interno(self, no_deletado):
        for i in range(len(self.getAutomato())):
            if self.automato[i].nome == no_deletado:
                for j in range(len(self.automato[i].transicoes)):
                    if self.automato[i].transicoes[j][1] == no_deletado:
                        return self.automato[i].transicoes[j][0]    #Caso tenha ligação ele retornará o símbolo da transição

        return "#"

    #Função que verfica se existe algua transição entre dois estados, caso nao tenha retorna -1
    def verifica_se_existe_ligacao(self, estado_inicial, estado_final):
        for i in range(len(self.getAutomato())):
            if self.automato[i].nome == estado_inicial:
                for j in range(len(self.automato[i].transicoes)):
                    if self.automato[i].transicoes[j][1] == estado_final:
                        return j    #Caso tenha ligação retornará a posição dela no vetor de transições

        return -1

    #Função que pega a posição de determinado estado no vetor, caso não ache ele retorna -1
    def pega_estado(self, nome_estado):
        for i in range(len(self.getAutomato())):
            if self.automato[i].nome == nome_estado:
                return i    #Caso encontre retorne na posição do vetor

        return -1

    ##Função que trata os simbolos do estado de saida para o deletado e do deletado para o destino
    #Caso os três valores sejam "#" ele retornará apenas um "#"
    #Caso tenha pelo menos um símbolo diferente de "#" ele que será retornado
    def simbolos_transicao(self, vetor_simbolos):
        simbolo = ''
        for i in range(len(vetor_simbolos)):
            if vetor_simbolos[i] != "#":
                simbolo = simbolo + vetor_simbolos[i]   #Concatenando os símbolos diferentes de "#"

        if simbolo == '':   #Condição que verifica se a VAR símbolos tem algo ou vazia, caso esteja vazia retornará "#"
            return "#"
        else:
            return simbolo  #Caso contrário retornará "símbolo"

    #Função que remove o fecho de Klen no estado
    def remove_laco_interno(self, nome_no):
        posicao_ligacao = self.verifica_se_existe_ligacao(nome_no, nome_no) #pegando a posição da transição no vetor transição
        simbolo = self.verifica_laco_interno(nome_no)  #Pegando o símbolo da transição
        posicao_no = self.pega_estado(nome_no)  #Pegando a posição do estado no vetor
        self.automato[posicao_no].transicoes.pop(posicao_ligacao)   #Depois de pegar todos dados elimanará a transição de fecho de klen do estado
        for i in range(len(self.automato[posicao_no].transicoes)):
            if self.automato[posicao_no].transicoes[i][0] != "#":    #Caso o símbolo seja diferente de apenas "#", será concatenado aos outros símbolos
                aux = simbolo + self.automato[posicao_no].transicoes[i][0]
                self.automato[posicao_no].transicoes[i][0] = aux
            else:
                self.automato[posicao_no].transicoes[i][0] = simbolo    #Caso contrário apenas será atribuido o símbolo a lista

        return self.automato

    #Função que tratará as transições do estado a ser deletado e por fim deletará o mesmo
    def deleta_estado(self, deleta_nome):
        if self.verifica_laco_interno(deleta_nome) != "#":   #Já tratando o caso de laço interno no estado, fecho de Klen
            self.automato = self.remove_laco_interno(deleta_nome)

        posicao_no_vetor_do_no_deletado = self.pega_estado(deleta_nome) #Pega a posição do estado a ser deletado no vetor
        vertices_que_vao_ao_no = self.lista_entrada_do_vertice_deletado(deleta_nome)    #Lista com com os vértices que vão ao nó a ser deletado
        lista_transicoes_no_deletado = self.saida_do_vertice_deletado(deleta_nome)  #Lista com as transições que saem do estado a ser deletado
        #Nestes dois "FOR" será pego da lista do estados que vão ao no a ser deletado e as transições do no a ser deletado com os outros estados
        for i in range(len(vertices_que_vao_ao_no)):
            for j in range(len(lista_transicoes_no_deletado)):
                destino = self.automato[posicao_no_vetor_do_no_deletado].transicoes[j][1]   #Primeiro destino de uma transição do no a ser deletado
                if deleta_nome != destino:
                    """
                    #Seu Código vai vir aqui, var1 recebe a posicão da transiçaõ entre o no que tem uma transição partindo e chega ao no deletado
                    #var2 recebe a posição da ligação do no deletado ao no destino, no caso o primeiro que achar
                    #var1 e var2 dois sao posiçoes no vetor de transição dos nos
                    
                    
                    var1 = self.verifica_se_existe_ligacao(self.automato[vertices_que_vao_ao_no[i]].nome, deleta_nome)
                    var2 = self.verifica_se_existe_ligacao(deleta_nome, destino)
                    print("\n")
                    print(deleta_nome, var1, var2)
                    print("\n")
                    var1 = ""
                    var2 = ""
                    """

                    nome_origem = self.automato[vertices_que_vao_ao_no[i]].nome #Pegando o nome do priemiro estado no vetor que vai ao no deletado
                    aux = ''
                    if nome_origem != deleta_nome:  #Condição para evitar que pegue os símbolo de transição interno
                        aux = self.verifica_se_existe_ligacao(nome_origem, deleta_nome)
                        var1 = self.automato[vertices_que_vao_ao_no[i]].transicoes[aux]
                        aux = self.automato[vertices_que_vao_ao_no[i]].transicoes[aux][0]   #Se nao for fecho de klen, pegará o símbolo de transição

                    var2 = self.automato[posicao_no_vetor_do_no_deletado].transicoes[j]
                    simbolo_destino = self.automato[posicao_no_vetor_do_no_deletado].transicoes[j][0]   #Pegando o símbolo de transição do estado a ser deletado com o primeiro destino no vetor do "FOR"
                    aux = [aux, simbolo_destino]
                    simbolos_concatenados = self.simbolos_transicao(aux)    #tratando os simbolos pegos

                    pos_ligacao = self.verifica_se_existe_ligacao(nome_origem, destino) #pegando, se existe, a posição da ligação do no que tem transição para no deletado
                                                                                        # e do Nó a ser deletado para o No destino do Vetor
                    aux = self.automato[vertices_que_vao_ao_no[i]].transicoes[pos_ligacao][0]   #Pegando o símbolo da transição acima
                    if pos_ligacao != int(-1) and aux != "#":    #Caso exista e o simbolo de transião seja "#" é feita uma concatenação
                        aux = self.automato[vertices_que_vao_ao_no[i]].transicoes[pos_ligacao][0]
                        self.automato[vertices_que_vao_ao_no[i]].transicoes[pos_ligacao][0] = "(" + aux + \
                            "+" + simbolos_concatenados + ")"
                    else:
                        ligacao = [simbolos_concatenados, destino]  #Caso contrário apenas inserirá a transição do no origem para o nó a ser deletado
                        self.automato[vertices_que_vao_ao_no[i]].transicoes.append(ligacao)

            limpa_transicao = self.verifica_se_existe_ligacao(self.automato[vertices_que_vao_ao_no[i]].nome, deleta_nome)
            #"limpa_transicao" recebe a posicao da transição que está atual no "FOR" externo, caso I
            self.automato[vertices_que_vao_ao_no[i]].transicoes.pop(limpa_transicao)    #É deletado esta transição do estado origem que vai para o nó deletado
        self.automato.pop(posicao_no_vetor_do_no_deletado)  #Por fim deleta o estado deletado do vetor

