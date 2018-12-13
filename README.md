# AFN Converter

#### Instituto Federal de Minas Gerais - Campus Formiga

##### Jonathan Arantes - <tlc.jooker@gmail.com>
##### Saulo Cassiano de Carvalho - <saulocarvalho64@gmail.com>

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

Um autômato é meramente uma lista de estados, nesta estrutura. Por Exemplo:

```Python
automato = Automato()
automato.addEstado(Estado("1", 0, [['a', "2"], ["b", "3"]]))
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

R: Lista com as ordem de remoção dos estados.

### Passo a passo do algoritmo

1. Ler autômato recebido na entrada de dados;

2. Colocar estados _Inicial_ e _Final_ no autômato, modificar o autômato lido na entrada seguindo as regras:
    - Estado _Inicial_ deve ter uma transição deste para todos os estados marcados como iniciais, tendo como entrada λ;
    - Todos os estados finais devem ter uma transição destes para o estado _Final_, tendo como entrada λ.

3. Armazenar o autômato em uma lista;

4. Há um laço que deleta estado ate que chegue o estado inicial no vetor autômato, já prevista na estrada de dados;

5. No ```deleta_estado``` é feita uma verificação se determinado estado tem laço interno, caso tenha, irá removê-lo e já colocar seu símbolo com os outros de forma correta, caso tenha mais de uma transição naquele estado. Por fim retorna-se o novo automato depois da conversão;

6. Pega-se dados como posição do estado no vetor, os nomes dos vértices que vão ao nó deletado e por fim, dos vértices que recebem alguma ligação do no deletado;

7. Percorre um _for_ externo com os nos que vão ao no deletado e dentro dele um outro for que percorre os nos que recebem ligação do no deletado;

8. Verifica-se somente os estados envolvidos não são em um caso de loop (origem - estado deletado || estado deletado - destino);

9. Caso não seja, verifica-se se existe ligação do estado que vai ao deletado e do deletado ao próximo, se tiver ligação, depois concatena-se os os símbolos dos estados;

10. Uma vez feita a concatenação, pega a posição da transição do estado deletado e deleta ela, quando todas transições do estado acabar, deleta o estado do vetor;
