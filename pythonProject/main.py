import sys

class Aresta:

    # Classe Aresta com atributos de letra da transição, vértice de inicio e vértice de fim

    def __init__(self, letter, inicio, fim):
        self.letter = letter
        self.inicio = inicio
        self.fim = fim

class Vertice:

    # Classe Vertice com atributos de dado (nome do estado), se é inicial e se é final.

    isInitial = False
    isFinal = False

    def __init__(self, dado):
        self.dado = dado

class Grafo:

    # Classe Grafo com atributos de lista de vertices, listas de arestas e vertice inicial.

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

    # O método isRecognized() é o método responsável por ler uma nova palavra e identificar se ela é reconhecida pelo AFD
    # O loop interno inicia no estado inicial e com a primeira letra da palavra lida
    # e passa para o próximo estado caso encontre uma transição com essa letra
    # Caso nenhuma transição não seja encontrada o AFD iria para o estado de erro, ou seja, o resultado da palavra é "N"

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

    # Entrada de estados
    estados = sys.stdin.readline()
    for s in estados.rstrip():
        if s != ' ':
            grafo.adicionarVertice(s)

    # Entrada do alfabeto
    alfabeto = sys.stdin.readline()
    for a in alfabeto:
        if a != ' ':
            alfabeto = alfabeto + a

    # Entrada do numero de transicoes
    n_transicoes = sys.stdin.read(1)

    # Entrada transicoes
    n = 0
    while n < int(n_transicoes):
        transicoes = sys.stdin.readline()
        if transicoes.rstrip() != '':
            n = n + 1
            grafo.adicionarAresta(transicoes[2], transicoes[0], transicoes[4])

    # Entrada do estado inicial
    estado_inicial = sys.stdin.readline()
    grafo.setInitial(estado_inicial.rstrip())

    # Entrada de estados finais
    estados_finais = sys.stdin.readline()
    for s in estados_finais.rstrip():
        if s != ' ':
            grafo.setFinal(s)

    # Entrada das palavras
    palavras = sys.stdin.readline()
    cont = 0
    for p in palavras.rstrip():
        if p != ' ':
            word = word + p
        else:
            words.append(word)
            word = ''

        cont = cont + 1

        if cont == len(palavras.rstrip()):
            words.append(word)

    for w in words:
        out.write(grafo.isRecognized(w) + '\n')