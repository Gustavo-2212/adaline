# Projeto de Aprendizado de Máquina com Adaline e Regressão Linear 🧠
---
### Autor
- **Nome:** Gustavo Alves de Oliveira
- **Matrícula:** 12311ECP026
- **Disciplina:** Aprendizagem de Máquina
- **Faculdade:** Universidade Federal de Uberlândia


🤖📊🔍

Este projeto utiliza técnicas de Aprendizado de Máquina para realizar análises estatísticas e preditivas sobre um conjunto de dados, incluindo a implementação do algoritmo Adaline e o cálculo da regressão linear simples.

### Introdução ao Adaline

O Adaline (Adaptive Linear Neuron) é um modelo de neurônio artificial que realiza a classificação de padrões com base em uma função linear. Ele ajusta os pesos e o bias do neurônio para minimizar uma função de custo, geralmente a função de erro quadrático médio (MSE).

ℹ️ O Adaline é uma extensão do Perceptron, capaz de lidar com saídas contínuas e não binárias.

### Regressão Linear

A Regressão Linear é uma técnica estatística que modela a relação entre uma variável dependente (Y) e uma ou mais variáveis independentes (X). O objetivo é encontrar a melhor linha de ajuste que minimize a soma dos quadrados das diferenças entre os valores observados e os valores previstos.

ℹ️ A Regressão Linear é frequentemente usada para prever valores de uma variável com base em outras variáveis conhecidas.

### Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- **./imgs**: Contém os gráficos gerados pelo Matplotlib, incluindo distribuição dos dados, retas de regressão e do Adaline, erro quadrático do Adaline e função de separação.
- **./data**: Armazena a base de observações em um arquivo de texto.
- **./graph**: Responsável pela geração dos gráficos interativos usando a biblioteca Bokeh.
- **./src**: Contém os códigos-fonte, incluindo `main.py` como o arquivo executável principal, `adaline.py` com a implementação do Adaline, `regressao.py` para calcular a regressão e os erros, e outras funções relacionadas.

### Dependências do Projeto

Para executar o projeto, é necessário instalar a seguinte biblioteca Python:

- Bokeh: Biblioteca para criar visualizações interativas em navegadores da web.

```bash
pip install bokeh
```

### Como Executar o Projeto

1. Clone o repositório do projeto.
2. Instale as dependências listadas acima.
3. Execute o arquivo `main.py` dentro da pasta `./src` para gerar os gráficos e realizar as análises estatísticas.

### Conclusões

Ao analisarmos os resultados podemos notar que a função linear plotada em cima dos dados de observações, fazendo o uso dos coeficientes calculados do Adaline chegam bem próximos da função linear gerada com os coeficientes calculados pela Regressão, que é um modelo matemático.

🚀🔍💡

---
