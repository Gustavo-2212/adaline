# Projeto de Aprendizado de Máquina com Redes Multicamadas 🧠
---
### Autor
- **Nome:** Gustavo Alves de Oliveira
- **Matrícula:** 12311ECP026
- **Disciplina:** Aprendizagem de Máquina
- **Faculdade:** Universidade Federal de Uberlândia


🤖📊🔍

Este projeto utiliza técnicas de Aprendizado de Máquina para calcular a função aproximada que passa por todos os pontos de um conjunto de amostras dado.

### Redes Neurais Perceptrons de Multicamadas (MLP)

As Redes Neurais Perceptrons de Multicamadas (MLPs) são uma classe de redes neurais artificiais que consistem em uma rede de nós (neurônios) organizados em camadas. As MLPs são compostas por uma camada de entrada, uma ou mais camadas ocultas e uma camada de saída.

### Funcionamento das MLPs:

1. **Camada de Entrada:**
   - Os nós na camada de entrada representam as características (features) dos dados de entrada. Cada nó nesta camada corresponde a uma característica específica.

2. **Camadas Ocultas:**
   - As camadas ocultas são compostas por neurônios que processam os dados de entrada e aprendem a representação dos padrões nos dados.
   - Cada neurônio em uma camada oculta recebe entradas das camadas anteriores, realiza uma combinação linear das entradas ponderadas por pesos, aplica uma função de ativação não linear e passa o resultado para as camadas posteriores.
   - A presença de camadas ocultas permite que as MLPs aprendam representações mais complexas e não lineares dos dados.

3. **Camada de Saída:**
   - A camada de saída produz a saída final da rede neural. A estrutura desta camada depende do tipo de problema que está sendo abordado, como classificação (por exemplo, softmax para classificação multiclasse) ou regressão (um único neurônio de saída para prever um valor contínuo).

>![MLP](https://www.researchgate.net/publication/293013889/figure/fig1/AS:335717596188674@1457052720824/Figura-1-Exemplo-simplificado-de-uma-rede-neural-multicamadas-HAYKIN-2001-Figure-1.png)

### Idealização e Desenvolvimento:

As MLPs não têm um único idealizador. O desenvolvimento das MLPs foi uma evolução das redes neurais perceptrons originais propostas por Frank Rosenblatt em 1957. As MLPs foram introduzidas para superar a limitação das redes perceptrons de uma única camada, que só podiam resolver problemas linearmente separáveis. A ideia de adicionar camadas ocultas e usar algoritmos de treinamento como o backpropagation permitiu que as MLPs aprendessem a representar relações mais complexas nos dados.

### Função Sigmóide Bipolar como Função de Ativação:

A função sigmóide bipolar, também conhecida como função de ativação bipolar, é uma função matemática usada em redes neurais como uma função de ativação. Sua fórmula é:

\[ f(x) = \frac{2}{1 + e^{-x}} - 1 \]

Esta função mapeia os valores de entrada para o intervalo [-1, 1]. Ela é suave e diferenciável em todos os pontos, o que a torna adequada para o treinamento de redes neurais utilizando algoritmos de otimização baseados em gradiente, como o backpropagation.

A função sigmóide bipolar tem sido historicamente utilizada como função de ativação nos neurônios das camadas ocultas das MLPs. No entanto, devido a problemas como o desaparecimento do gradiente durante o treinamento profundo e a propagação do gradiente muito lenta em camadas profundas, funções de ativação alternativas, como ReLU (Rectified Linear Unit) e suas variantes, tornaram-se mais populares em redes neurais profundas modernas.

> ![Sigmóide Bipolar](https://www.researchgate.net/publication/331087209/figure/fig4/AS:726046831820800@1550114462005/Figura-54-Funcion-de-Activacion-Sigmoide-Bipolar.jpg)

### Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- **./graph**: Responsável pela geração dos gráficos interativos usando a biblioteca Bokeh.
- **./src**: Contém os códigos-fonte, incluindo `main.py` como o arquivo executável principal.

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

Podemos ver que a função consegue aproximar bem dos pontos das amostras. O que ainda podemos testar são outros tipos de arquiteturas de redes neurais, bem como outras funções de ativação, verificando se o desempenho da rede neural é melhorado ou não.

🚀🔍💡

---
