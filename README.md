# Projeto ADALINE - README

## Autor
- **Nome:** Gustavo Alves de Oliveira
- **Disciplina:** Aprendizagem de Máquina
- **Faculdade:** Universidade Federal de Uberlândia

## História do ADALINE 📚

O ADALINE, abreviação para *Adaptive Linear Neuron*, foi desenvolvido por Bernard Widrow e Ted Hoff na Universidade de Stanford em 1960. Este modelo foi uma das primeiras tentativas de construir uma rede neural artificial.

### Contexto Histórico

- **Década de 1960**: Neste período, os cientistas estavam começando a explorar os conceitos de redes neurais e aprendizado de máquina. O ADALINE foi uma resposta a esse interesse crescente, sendo desenvolvido como uma extensão do conceito de neurônio artificial, proposto pelo neurofisiologista Warren McCulloch e pelo matemático Walter Pitts em 1943.

## Funcionamento do ADALINE

O ADALINE opera de maneira semelhante ao Perceptron, outro modelo de neurônio artificial. Aqui está uma descrição básica de como o ADALINE funciona:

1. **Entradas e Pesos**: O ADALINE recebe um conjunto de entradas, cada uma multiplicada por um peso associado. Estas entradas e pesos formam um vetor de entrada.

2. **Soma Ponderada**: O ADALINE calcula a soma ponderada das entradas e pesos.

3. **Função de Ativação Linear**: Ao contrário do Perceptron, o ADALINE utiliza uma função de ativação linear. Esta função é usada para ajustar a saída do neurônio de acordo com a soma ponderada das entradas e pesos.

4. **Ajuste de Pesos**: Durante o treinamento, os pesos são ajustados para minimizar uma função de custo. Isso geralmente é feito usando algoritmos de otimização, como o Gradiente Descendente.

5. **Saída**: A saída do ADALINE é uma combinação linear das entradas e pesos, passada através da função de ativação linear.

### Diferença entre ADALINE e Perceptron

A principal diferença entre o ADALINE e o Perceptron está na função de ativação utilizada. Enquanto o Perceptron utiliza uma função de ativação degrau, o ADALINE utiliza uma função de ativação linear. Isso significa que o ADALINE pode produzir saídas contínuas em vez de saídas binárias.

### Aplicações do ADALINE

O ADALINE foi inicialmente aplicado em problemas de reconhecimento de padrões e controle adaptativo. Com o tempo, suas aplicações foram estendidas para uma variedade de áreas, incluindo processamento de sinais, comunicações e sistemas de controle.

## Sobre o Projeto 🤖

O projeto ADALINE consiste na implementação e teste de uma rede neural ADALINE utilizando a linguagem Python. A rede é treinada e testada em cima de uma base de dados fornecida em formato Excel (.xlsx). O programa gera gráficos que mostram a distribuição dos dados de entrada, o comportamento do erro quadrático conforme os ciclos de treinamento aumentam e a fronteira de separação obtida pelo ADALINE.

### Algoritmo de Treinamento LMS (Least Mean Squares)

O algoritmo de treinamento utilizado é o LMS, sigla para *Least Mean Squares*. Ele é um algoritmo de aprendizado de máquina supervisionado que ajusta os pesos da rede de acordo com o erro entre a saída esperada e a saída real. O algoritmo minimiza o erro quadrático médio, atualizando os pesos de forma iterativa.

## Estrutura do Projeto 📂
```Python
./adaline
├── data
│   └── Basedados_B2.xlsx
├── imgs
│   ├── dados.png                     # Distribuição dos dados de entrada
│   ├── erro_quadratico.png           # Comportamento do erro
│   └── fronteira_separacao.png       # Fronteira de separação
└── src
    └── main.py
```


## Executando o Programa 🚀

Para executar o programa, siga os seguintes passos:

1. Certifique-se de ter o Python 3.11 instalado em seu sistema.
2. Instale as bibliotecas necessárias executando o comando abaixo:
    ```bash
    pip install pandas matplotlib numpy
    ```
3. Execute o arquivo `main.py` com o comando:
    ```bash
    python main.py
    ```

---

Com este projeto, esperamos explorar e compreender os princípios fundamentais por trás das redes neurais e do algoritmo de treinamento LMS. O ADALINE continua sendo uma pedra angular no desenvolvimento da inteligência artificial e da computação moderna.
