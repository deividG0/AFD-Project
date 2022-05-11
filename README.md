# AFD-Project

Aluno: Deivid Gomes Silva
Mat.: 2018106335

O algoritmo se encontra no arquivo main.py dentro da pasta pythonProject e contém comentários nas partes principais do algoritmo.

Como o algoritmo foi projetado:
  O algoritmo foi implementado na linguagem de programação Python e consistia na simulação de uma AFD com a estrutura de dados Grafo com arestas orientadas.
  Dessa forma, cada vértice era um estado com um nome e cada aresta era uma possível transição a ser feita.
  O trecho do código responsável pelo reconhecimento de palavras inicia no estado inicial e a partir da primeira levra da palavra.
  Uma transição é feita caso seja encontrada uma transição com essa letra atualmente analisada. 
  Caso nenhuma transição seja encontrada o AFD já imprime o resultado "N" para a palavra em questão.
  
Quais as estruturas de dados:
  A estrutura de dados escolhida foi o Grafo, como previamente citado.
  
Complexidade da implementação de reconhecimento:
  Tendo em mente que para cada letra da palavra de entrada o algoritmo de reconhecimento implementado faz uma busca em todas as arestas do grafo,
  pode se dizer que a complexidade do algoritmo é O(|w|) com |w| sendo o tamanho da palavra.
