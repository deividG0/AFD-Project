import sys


class Aresta:
    def __init__(self, letter, inicio, fim):
        self.letter = letter
        self.inicio = inicio
        self.fim = fim


class Vertice:
    isInitial = False
    isFinal = False

    def __init__(self, dado):
        # self.arestasSaida = []
        # self.arestasEntrada = []
        self.arestasSaida = []
        self.arestasEntrada = []
        self.dado = dado

    def adicionarArestaEntrada(self, aresta):
        # self.arestasEntrada.append(aresta)
        self.arestasEntrada.append(aresta)

    def adicionarArestaSaida(self, aresta):
        # self.arestasSaida.append(aresta)
        self.arestasSaida.append(aresta)

    def getArestasSaida(self):
        # return self.arestasSaida
        return self.arestasSaida

    def getArestasEntrada(self):
        # return self.arestasEntrada
        return self.arestasEntrada


class Grafo:

    # verticeInitial = Vertice

    def __init__(self):
        self.verticeInitial = None
        self.arestas = []
        self.vertices = []

    def adicionarVertice(self, dado):
        vertice = Vertice(dado)
        self.vertices.append(vertice)

    def adicionarAresta(self, letter, dadoInicio, dadoFim):
        inicio = self.getVertice(dadoInicio)
        fim = self.getVertice(dadoFim)

        aresta = Aresta(letter, inicio, fim)

        self.arestas.append(aresta)

        # a = fim.getArestasSaida
        # inicio.adicionarArestaSaida(aresta)
        # fim.arestasSaida = a

        # b = inicio.getArestasEntrada
        # fim.adicionarArestaEntrada(aresta)
        # inicio.arestasEntrada = b

    def getVertice(self, dado):
        for v in self.vertices:
            if v.dado == dado:
                return v

    def setInitial(self, dado):
        for v in self.vertices:
            if v.dado == dado:
                v.isInitial = True
                self.verticeInitial = v
                break

    def setFinal(self, dado):
        for v in self.vertices:
            if v.dado == dado:
                v.isFinal = True
                break

    def isRecognized(self, word):
        currentState = self.verticeInitial
        letterIndex = 0
        found = False
        currentWordLetter = ''

        while letterIndex < len(word):
            currentWordLetter = word[letterIndex]
            found = False
            for a in self.arestas:
                if a.inicio == currentState and a.letter == currentWordLetter:
                    currentState = a.fim
                    letterIndex = letterIndex + 1
                    found = True
                    break

            if not found:
                return "N"

        if currentState.isFinal:
            return "S"
        else:
            return "N"


if __name__ == '__main__':

    grafo = Grafo()

    alfabeto = []
    word = ''
    words = []
    out = sys.stdout
    # grafo.adicionarVertice("0")
    # grafo.adicionarVertice("1")
    #
    # grafo.adicionarAresta("a", "0", "1")
    # grafo.adicionarAresta("a", "1", "1")
    # grafo.adicionarAresta("b", "1", "1")
    #
    # grafo.setInitial("0")
    #
    # grafo.setFinal("1")
    #
    # palavra = sys.stdin.readline()
    # print(grafo.isRecognized(palavra.rstrip()))

    # text = sys.stdin.read(1)

    # Entrada de estados
    #print('ESTADOS: ')
    estados = sys.stdin.readline()
    for s in estados.rstrip():
        if s != ' ':
            #print(s)
            grafo.adicionarVertice(s)

    # Entrada do alfabeto
    #print('ALFABETO: ')
    alfabeto = sys.stdin.readline()
    for a in alfabeto:
        if a != ' ':
            alfabeto = alfabeto + a

    # Entrada do numero de transicoes
    #print('N TRANSICOES: ')
    n_transicoes = sys.stdin.read(1)

    # Entrada transicoes
    #print('TRANSICOES: ')
    n = 0
    while n < int(n_transicoes):
        transicoes = sys.stdin.readline()
        if transicoes.rstrip() != '':
            #print(transicoes.rstrip())
            n = n + 1
            #print('{}, {}, {}', transicoes[2], transicoes[0], transicoes[4])
            grafo.adicionarAresta(transicoes[2], transicoes[0], transicoes[4])

    # Entrada do estado inicial
    #print('ESTADO INICIAL: ')
    estado_inicial = sys.stdin.readline()
    grafo.setInitial(estado_inicial.rstrip())

    # Entrada de estados finais
    #print('ESTADOS FINAIS: ')
    estados_finais = sys.stdin.readline()
    for s in estados_finais.rstrip():
        if s != ' ':
            grafo.setFinal(s)

    # Entrada das palavras
    #print('PALAVRAS: ')
    palavras = sys.stdin.readline()
    cont = 0
    for p in palavras.rstrip():
        #print(f'{p}')
        if p != ' ':
            word = word + p
        else:
            words.append(word)
            word = ''

        cont = cont + 1

        if cont == len(palavras.rstrip()):
            words.append(word)

    #print(words)

    for w in words:
        out.write(grafo.isRecognized(w) + '\n')

    # text2 = sys.stdin.readline()

    # for line in text:
    #     # Remove trailing newline characters using strip()
    #     line.
    #     if 'exit' == line.strip():
    #         print('Found exit. Terminating the program')
    #         exit(0)
    #     else:
    #         print('Message from sys.stdin: ---> {} <---'.format(line))
