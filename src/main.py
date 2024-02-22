import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np


def calcula_erro(Y, target):
    # E = 0
    # for i in range(0, len(target)):
    #     E += abs(target[i] - Y[i])
    # return E / len(target)
    return sum(abs(target[i] - Y[i]) for i in range(len(target))) / len(target)


def LMS_algoritmo(entradas, target):
    LMS_erro = []
    LMS_ciclos = []

    erro_minimo = 0.37235741682805046
    ciclos = 0
    ciclos_maximo = 10000
    taxa_aprendizagem = 0.0001 #random.uniform(0.0, 1.0) [MIN: 0.0001, MAX: 0.03]
    w = [random.uniform(-0.5, 0.5) for _ in range(len(entradas[0]))]
    b = random.uniform(-0.5, 0.5)
    # taxa_aprendizagem = 0.05
    # w = [0.431626, -0.060849]
    # b = -0.162357
    
    erro = calcula_erro( [b + entradas[i][0] * w[0] + entradas[i][1] * w[1] for i in range(0, len(entradas))],
                        target)

    print(f"\nValores iniciais: \n\tW1: {w[0]}\n\tW2: {w[1]}\n\tB: {b}\n\tTaxa de Aprendizagem: {taxa_aprendizagem}\n\tErro inicial: {erro}\n")
    
    #while erro > erro_minimo:
    while erro > erro_minimo and ciclos < ciclos_maximo:
        E = 0
        ciclos += 1
        Y = []
        for i in range(0, len(entradas)):
            y = b
            for j in range(0, len(entradas[0])):
                y += entradas[i][j] * w[j]

            E += (target[i] - y) ** 2

            for j in range(0, len(entradas[0])):
                w[j] += taxa_aprendizagem * (target[i] - y) * entradas[i][j]
            b += taxa_aprendizagem * (target[i] - y)
            Y.append(y)

        erro = calcula_erro(Y, target)
        print(f"\t[+] Erro: {erro}")
        LMS_erro.append(E)
        LMS_ciclos.append(ciclos)

    print(f"\nCiclos: {ciclos}")
    return (w, b, taxa_aprendizagem), (LMS_ciclos, LMS_erro)


def gerar_graficos(LMS, FRONTEIRA, df):
    plt.figure('1')
    plt.title("Regra Delta (LMS)")
    plt.plot(LMS[0], LMS[1])
    plt.xlabel("Ciclos")
    plt.ylabel("Erro Quadrático")
    plt.savefig("./imgs/erro_quadratico.png")

    plt.figure('2')
    plt.title("Fronteira de Separação")
    plt.plot(df['s1'], df['s2'], 'bs', FRONTEIRA[0], FRONTEIRA[1], '--r')
    plt.savefig("./imgs/fronteira_separacao.png")

    plt.figure('3')
    plt.title("Distribuição das Dados")
    plt.plot(df['s1'], df['s2'], 'bs')
    plt.savefig("./imgs/dados.png")


def testa(entradas, target, pesos):
    theta = 0
    w, b, taxa_aprendizagem = pesos[0], pesos[1], pesos[2]
    print(f"PESOS\n\tW1: {w[0]}\n\tW2: {w[1]}\n\tB: {b}\n\tTaxa de Aprendizagem: {taxa_aprendizagem}")
    print("\n\n[S1]\t\t[S2]\t\t[T]\t\t[Y Líquido]\t\t\t[R]\n" + '-'*85)
    for i in range(0, len(entradas)):
        y = w[0] * entradas[i][0] + w[1] * entradas[i][1] + b
        r = 1 if y >= theta else -1
        print(f"{entradas[i][0]}\t\t{entradas[i][1]}\t\t{target[i]}\t\t{y}\t\t{r}")


def main():
    df = pd.read_excel('./data/Basedados_B2.xlsx')

    entradas = []
    target = []
    for column in range(0, df.shape[0]):
        entradas.append( [df['s1'][column], df['s2'][column]] )
    target = df['t'].to_list()

    print('-'*85 + '\nTreinando a Rede Neural')
    pesos, LMS = LMS_algoritmo(entradas, target)

    w, b = pesos[0], pesos[1]

    valores = np.arange(-1.,3.,0.1)
    Y = []
    for i in valores:
        Y.append(-(w[0] * i + b)/w[1])

    FRONTEIRA = (valores, Y)
    gerar_graficos(LMS, FRONTEIRA, df)

    print('-'*85 + '\nTestando a Rede Neural')
    testa(entradas, target, pesos)


if __name__ == '__main__': 
    main()