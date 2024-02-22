# Projeto ADALINE - README

## Autor
- **Nome:** Gustavo Alves de Oliveira
- **Disciplina:** Aprendizagem de Máquina
- **Faculdade:** Universidade Federal de Uberlândia

## História do ADALINE 📚

O ADALINE, abreviação para *Adaptive Linear Neuron*, foi introduzido por Bernard Widrow e Ted Hoff em 1960 na Universidade de Stanford. O ADALINE é considerado um dos primeiros modelos de rede neural artificial e foi uma contribuição significativa para o campo emergente da inteligência artificial naquela época. Ele é um precursor do perceptron, outro tipo de modelo de rede neural.

## Sobre o Projeto 🤖

O projeto ADALINE consiste na implementação e teste de uma rede neural ADALINE utilizando a linguagem Python. A rede é treinada e testada em cima de uma base de dados fornecida em formato Excel (.xlsx). O programa gera gráficos que mostram a distribuição dos dados de entrada, o comportamento do erro quadrático conforme os ciclos de treinamento aumentam e a fronteira de separação obtida pelo ADALINE.

## Funcionamento do ADALINE 🧠

O ADALINE é uma rede neural de única camada composta por um único neurônio, que opera de maneira semelhante a um modelo de regressão linear. Ele recebe entradas, multiplica-as por pesos associados e soma-as. Esta soma é então processada por uma função de ativação linear, que produz a saída da rede.

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
