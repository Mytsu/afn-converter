class Estado(object):

    def __init__(self, nome=None, tipo=None, matriz_transicoes=None):
        self.nome = nome
        self.tipo = tipo#0 - Inicial. 1 - Intermediário, 2 - Final
        # Lista de transições no formato (símbolo, estado_destino) como segue: [('a', 2), ('b', 3)]
        self.transicoes = matriz_transicoes


class Automato(object):
    def __init__(self):
        self.automato = [] #Vetor de estados

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
                ini.transicoes.append([None, self.automato[i]])
            elif self.automato[i].tipo == 2:
                self.automato[i].tipo = 1
                self.automato[i].transicoes.append(fin)

        self.addEstado([ini.nome, ini.tipo, ini.transicoes])
        self.addEstado([fin.nome, fin.tipo, fin.transicoes])

    def segundo_passo(self):
        pass

    def deletaEstado(self):
        lista_automatos_quechegam = []
        lista_automatos_querecebem = []
        while self.automato[1].tipo == 1:
            for i in range(len(self.getAutomato())):
                if i != 1:
                    for j in range(len(self.automato[i].transicoes)):
                        if self.automato[i].transicoes[j][1] == self.automato[1]:
                            lista_automatos_quechegam.append(self.automato[i])

            for i in range(len(self.automato[1].transicoes)):
                lista_automatos_querecebem.append(self.automato[1].transicoes[i])
                #continua depois para ver como faz

    def modificaTransicoes(self):
        for i in range(len(self.getAutomato())):
            for j in range(len(self.automato[i].transicoes)):
                if "," in self.automato[i].transicows[j][0]:
                    self.automato[i].transicows[j][0].str.replace(",", "+")
                    self.automato[i].transicows[j][0] = "(" + self.automato[i].transicows[j][0] + ")"

                if self.automato[i].transicoes[j][1] == self.automato[i]:
                    self.automato[i].transicows[j][0] = self.automato[i].transicows[j][0] + "*"














