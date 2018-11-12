# AFN Converter

#### Instituto Federal de Minas Gerais - Campus Formiga

##### Jonathan Arantes <<tlc.jooker@gmail.com>>
##### Saulo Cassiano

Trabalho Prático da disciplina de Linguagens Formais de Autômatos (LFA) - Conversor de Autômatos Finitos Não-Determísticos (AFN) para Expressão Regular (Regex)

___

### Estrutura de Dados do Autômato

```Python
class Estado(object):
    def __init__(self, nome, tipo, trs):
        self.nome = nome
        self.tipo = tipo # None = intermediario; False = Final; True = Inicial
        # Lista de transições no formato (símbolo, estado_destino) como segue: [('a', 2), ('b', 3)]
        self.transicoes = trs
```

Exemplo de autômato:

```Python
automato = [
                Estado(1, True, [('a', 2)]), 
                Estado(2, None, [('b', 1), ('a', 3)]), 
                Estado(3, False, [('a', 3), ('b', 2)])
           ]
```

### Entrada de Dados

O autômato a ser lido na entrada de dados deve ser entregue na forma de um arquivo JSON, o formato do arquivo foi feito seguindo a estrutura de dados construída dentro da aplicação:

```JSON
{
    "automato": [{
            "nome": 1,
            "tipo": true,
            "transicoes": [
                {"simbolo": "a", "estado": 2}
            ]
        }
        {
            "nome": 2,
            "tipo": "",
            "transicoes": [
                {"simbolo":"b", "estado": 1},
                {"simbolo":"a", "estado": 3}
            ]
        }
        {
            "nome": 3,
            "tipo": false,
            "transicoes": [
                {"simbolo": "a", "estado": 3},
                {"simbolo": "b", "estado": 2}
            ]
        }
    ]
}
```

### Passo a passo do algoritmo

1. Ler autômato recebido na entrada de dados;
2. Colocar estados _Inicial_ e _Final_ no autômato, modificar o autômato lido na entrada seguindo as regras:;
    - Estado _Inicial_ deve ter uma transição deste para todos os estados marcados como iniciais, tendo como entrada λ;
    - Todos os estados finais devem ter uma transição destes para o estado _Final_, tendo como entrada λ;
3. Armazenar o autômato em uma pilha;
4. Transformar todo símbolo de transição:
    - Remover `,` e adicionar `()` às conjunções de símbolos;
5. Remover um estado do autômato (exceto os estados _Inicial_ e _Final_), concatenando os símbolos de transição do estado à transição gerada;
6. Se não houver apenas os estados _Inicial_ e _Final_ na pilha, repetir passo 3.
