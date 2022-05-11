class Teste:
   dic = {}
   def __init__(self):
      self.dic[id(self)] = []
   def getList(self):
      return self.dic[id(self)]
   def insList(self,x):
      self.dic[id(self)].append(x)
   def remList(self,indice):
      self.dic[id(self)].pop(indice)

if __name__ == '__main__':
    # Criando as instâncias
    a = Teste()
    b = Teste()

    # Inserindo valores
    a.insList(123)
    b.insList(456)

    # Recuperando Listas com os Valores
    print(a.getList())
    print(b.getList())

