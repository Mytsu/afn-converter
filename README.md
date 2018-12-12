# AFN Converter

#### Instituto Federal de Minas Gerais - Campus Formiga

##### Jonathan Arantes <<tlc.jooker@gmail.com>>
##### Saulo Cassiano

Trabalho Prático da disciplina de Linguagens Formais de Autômatos (LFA) - Conversor de Autômatos Finitos Não-Determísticos (AFN) para Expressão Regular (Regex)

___

### Estrutura de Dados do Autômato

Um estado é constituído por:

- Nome;

    Um identificador único para reconhecer o estado;

- Tipo:

    Define se este estado é _inicial_, _comum_ (intermediário) ou _final_;

- Transições;

Uma lista de transições que segue o formato:

```Python
            transicao = [simbolo, estado_destino]
```

Um autômato é meramente uma lista de estados, nesta estrutura.

```Python
automato = Automato()
automato.addEstado(Estado("1", 0, [['a', "2"], ["b", "3"]])),
automato.addEstado(Estado("2", 1, [['b', "2"], ["a", "4"]])),
automato.addEstado(Estado("3", 1, [['b', 4]]))
automato.addEstado(Estado("4", 2, []))
```

### Entrada de Dados

O autômato a ser lido na entrada de dados deve ser entregue na forma de um arquivo JSON, o formato do arquivo foi feito seguindo a estrutura de dados construída dentro da aplicação:

```JSON
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
```

O arquivo é definido pelos campos:

AF:

- Lista de Estados;
- Alfabeto;
- Lista de Transições;
- Lista de Estados iniciais;
- Lista de Estados finais.

R:

- Lista com as ordem de remoção dos estados.

### Passo a passo do algoritmo

1. Ler autômato recebido na entrada de dados;
2. Colocar estados _Inicial_ e _Final_ no autômato, modificar o autômato lido na entrada seguindo as regras:;
    - Estado _Inicial_ deve ter uma transição deste para todos os estados marcados como iniciais, tendo como entrada λ;
    - Todos os estados finais devem ter uma transição destes para o estado _Final_, tendo como entrada λ;
3. Armazenar o autômato em uma lista;
4. Transformar todo símbolo de transição:
    - Remover `,` e adicionar `()` às conjunções de símbolos;
5. Remover um estado do autômato (exceto os estados _Inicial_ e _Final_), concatenando os símbolos de transição do estado à transição gerada;
6. Se não houver apenas os estados _Inicial_ e _Final_ na pilha, repetir passo 3.
