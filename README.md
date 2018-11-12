# AFN Converter

#### Instituto Federal de Minas Gerais - Campus Formiga

##### Jonathan Arantes <<john.mytsu@gmail.com>>
##### Saulo Cassiano

Trabalho Prático da disciplina de Linguagens Formais de Autômatos (LFA) - Conversor de Autômatos Finitos Não-Determísticos (AFN) para Expressão Regular (Regex)

___

### Estrutura de Dados do Autômato

```Python
class Estado(object):
    def __init__(self, tipo, trs):
        self.tipo = tipo # None = intermediario; False = Final; True = Inicial

```

### Passo a passo do algoritmo

1. Colocar estados _Inicial_ e _Final_;
2. Transformar todo símbolo de transição:
    - Remover `,` e adicionar `()` às conjunções de símbolos;
3. Remover um estado do autômato (exceto os estados _Inicial_ e _Final_), concatenando os símbolos de transição do estado à transição gerada;
4. Se não houver apenas os estados _Inicial_ e _Final_ na lista, repetir passo 3.
