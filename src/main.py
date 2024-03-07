import random
from math import e
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import gridplot


def sigmoide(x):
    return (2 / (1 + e**(-x))) - 1



def MLP(x, y):
    amostras = len(x)
    LMS_erro, LMS_ciclo = [], []
    
    neuronios_entrada = 1
    neuronios_internos = 4
    neuronios_saida = 1
    
    erro_minimo = .0002 # .002 .0005 .0003
    ciclos, num_ciclos = 0, 500000
    taxa_aprendizagem = .03
    
    # Inicialização dos pesos da CAMADA INTERNA
    w_int = [random.uniform(-.5, .5) for i in range(neuronios_internos)]
    b_int = [random.uniform(-.5, .5) for i in range(neuronios_internos)]
    delta_int = [0] * neuronios_internos
    
    # Inicialização dos pesos da CAMADA DE SAÍDA
    w = [random.uniform(-.5, .5) for i in range(neuronios_internos)]
    b = random.uniform(-.5, .5)
    delta = [0] * neuronios_saida
    
    # Erro inicial (considerando os pesos que levam ao neurônio de saída)
    Y = []
    for i in range(amostras):
        Zin = [x[i] * w_int[j] + b_int[j] for j in range(neuronios_internos)]
        Z = [sigmoide(Zin[j]) for j in range(neuronios_internos)]
        
        Yin = b
        Yin += sum(Z[j] * w[j] for j in range(neuronios_internos))
        Y.append( sigmoide(Yin) )   
    erro = sum((y[i] - Y[i]) ** 2 for i in range(amostras)) / amostras 
    
    print("-" * 115)
    print("Treinando a Rede Neural MLP\n")
    print(f"\t[+] W: {w}\n\t[+] B: {b}\n\t[+] W Internos: {w_int}\n\t[+] B Internos: {b_int}\n\t[+] Taxa de aprendizagem: {taxa_aprendizagem}\n\t[+] Limiar: {erro_minimo}\n\t[+] Erro inicial: {erro}\n\t[+] Ciclos máximos: {num_ciclos}\n")
    
    while erro > erro_minimo and ciclos < num_ciclos:
        E = 0
        ciclos += 1
        
        for i in range(amostras):
        
            '''
                Fase Feedforward
            Inserção de cada padrão de treinamento na entrada da rede neural
            e cálculos das saídas (Z) dos neurônios internos
            '''
            # Cálculo das saídas dos neurônios internos
            Zin = [0] * neuronios_internos
            Z = [0] * neuronios_internos
            for j in range(neuronios_internos):
                Zin[j] = x[i] * w_int[j] + b_int[j]
                Z[j] = sigmoide(Zin[j]) # Sigmóide e Bipolar
                
            # Cálculo da saída da rede
            Yin = b
            Yin += sum([Z[j] * w[j] for j in range(neuronios_internos)])
            Y = sigmoide(Yin)
            
            
            '''
                Fase da Retropropagação
            '''
            # Cálculo da atualização dos pesos da camada do neurônio de saída
            delta_w = (y[i] - Y) * .5 * (1 + Y) * (1 - Y)
            
            Delta_w = [taxa_aprendizagem * delta_w * Z[j] for j in range(neuronios_internos)]
            Delta_b = taxa_aprendizagem * delta_w
            
            # Cálculo para a atualização dos pesos dos neurônios da camada interna
            for j in range(neuronios_internos):
                delta_int[j] = delta_w * w[j] * .5 * (1 + Z[j]) * (1 - Z[j])
                
            Delta_int = [taxa_aprendizagem * delta_int[j] * x[i] for j in range(neuronios_internos)]
            Delta_b_int = [taxa_aprendizagem * delta_int[j] for j in range(neuronios_internos)]
            
            # Atualização dos pesos dos neurônios da camada de saída
            for j in range(neuronios_internos):
                w[j] += Delta_w[j]
            b += Delta_b
            
            # Atualização dos pesos dos neurônios da camada interna
            for j in range(neuronios_internos):
                w_int[j] += Delta_int[j]
                b_int[j] += Delta_b_int[j]
            
            # Cálculo do erro quadrático
            E += .5 * ((y[i] - Y) ** 2)
        
        erro = E / amostras
        LMS_ciclo.append(ciclos)
        LMS_erro.append(E)
    
    print("Fim do treinamento\n")
    print(f"\t[+] Erro: {erro}\n\t[+] Ciclos: {ciclos}\n")
    
    return (w_int, b_int), (w, b), (LMS_ciclo, LMS_erro)


def testa(x, y, pesos_internos, pesos_saida):
    EixoY = []
    amostras = len(x)
    neuronios_internos = len(pesos_internos[0])
    
    print("-" * 115)
    print("Testando a Rede Neural MLP (Função Sigmóide Bipolar)\n")
    print(f"\t[+] W: {pesos_saida[0]}\n\t[+] B: {pesos_saida[1]}\n\t[+] W Internos: {pesos_internos[0]}\n\t[+] B Internos: {pesos_internos[1]}\n\n")
    print("-" * 115)
    print("Comparação dos resultados\n")
    
    for i in range(amostras):
        Zin = [x[i] * pesos_internos[0][j] + pesos_internos[1][j] for j in range(neuronios_internos)]
        Z = [sigmoide(Zin[j]) for j in range(neuronios_internos)]
        
        Yin = pesos_saida[1]
        Yin += sum(Z[j] * pesos_saida[0][j] for j in range(neuronios_internos))
        Y = sigmoide(Yin)

        print(f"\t[+] Y({i+1}): {y[i]:.4f}\tYmlp({i+1}): {Y}\n")
        EixoY.append(Y)
    
    return (x, EixoY)


def gerar_graficos(LMS, FUNCAO, PONTOS):
    output_file('./graph/rede_multicamadas.html')
    
    figura_erro = figure(title="Erro Quadrático", x_axis_label='ciclos', y_axis_label='erro', width=800, tools=["pan","box_zoom","wheel_zoom","hover","save","reset"])
    figura_erro.line(LMS[0], LMS[1], legend_label="Erro Quadrático", color="red", line_width=5)
    
    figura_aproximacao = figure(title="Função Aproximada", x_axis_label="x", y_axis_label="y", width=800, tools=["pan","box_zoom","wheel_zoom","hover","save","reset"])
    figura_aproximacao.square(PONTOS[0], PONTOS[1], legend_label="Dados", size=10, color="blue")
    figura_aproximacao.line(FUNCAO[0], FUNCAO[1], legend_label="Função", color="red", line_width=5)
    
    layout = gridplot([[figura_erro], [figura_aproximacao]])
    show(layout)
    
    return None


def main():
    x = (0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1)
    y = (-.9602, -.5770, -.0729, .3771, .6405, .6600, .4609, .1336, -.2013, -.4344, -.5)
    
    pesos_internos, pesos_saida, LMS = MLP(x, y)
    funcao = testa(x, y, pesos_internos, pesos_saida)
    
    gerar_graficos(LMS, funcao, (x, y))


if __name__ == '__main__':
    main()