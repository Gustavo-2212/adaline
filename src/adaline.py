import random
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import gridplot
import numpy as np


def recupera_dados(file):
    entradas, saidas = [], []
    with open(f"./data/{file}", "r") as file:
        df = file.read()
        
        # Tratando o conteúdo
        linhas = df.split('\n')
        for linha in linhas[1:]:
            vetor_linha = linha.split(' ')
            entradas.append( float(''.join(vetor_linha[0:len(vetor_linha)//2 + 1])) )
            saidas.append( float(''.join(vetor_linha[len(vetor_linha)//2 + 1:])) )
        
    return entradas, saidas


class Adaline:
    _ciclos = 0
    _w, _b, _taxa_aprendizagem = None, None, None
    def __init__(self, file, taxa_aprendizagem=0.001):
        self._taxa_aprendizagem = taxa_aprendizagem
        self._entradas, self._saidas = recupera_dados(file)
    
    
    def treino(self):
        amostras = len(self._entradas)
        
        # Valores para plotar o gráfico Erro Quadrático
        LMS_erro, LMS_ciclos = [], []
        
        erro_minimo = 0.02
        ciclos, ciclos_max = 0, 5000
        
        w = random.uniform(-0.5, 0.5)
        b = random.uniform(-0.5, 0.5)
        
        Y = [b + w * self._entradas[i] for i in range(amostras)]
        erro = sum((self._saidas[i] - Y[i]) ** 2 for i in range(amostras)) / amostras
        
        print("-" * 115)
        print("Treinando a Rede Neural\n")
        print(f"\t[+] W: {w}\n\t[+] B: {b}\n\t[+] Taxa de aprendizagem: {self._taxa_aprendizagem}\n\t[+] Limiar: {erro_minimo}\n\t[+] Erro inicial: {erro}\n\n")
        
        erro_anterior = 0
        diferenca = erro - erro_anterior
        while diferenca > 0 and erro > erro_minimo and ciclos < ciclos_max:
            E = 0
            ciclos += 1
            Y = []
            for i in range(amostras):
                # Cálculo do y líquido
                y = b + w * self._entradas[i]
                
                # Cálculo da distribuição do erro em função dos ciclos
                E += (self._saidas[i] - y) ** 2
                
                # Atualização dos pesos
                w += self._taxa_aprendizagem * (self._saidas[i] - y) * self._entradas[i]
                b += self._taxa_aprendizagem * (self._saidas[i] - y)
                Y.append(y)
            
            # Cálculo do erro por ciclo    
            erro = E / amostras
            # print(f"[+] Erro: {erro}")
            diferenca = abs(erro - erro_anterior)
            erro_anterior = erro
            LMS_erro.append(E)
            LMS_ciclos.append(ciclos)
    
        self._w, self._b = w, b
              
        FRONTEIRA = (np.arange(-4., 2., 0.5),
            [-(b * i)/w for i in np.arange(-4., 2., 0.5)])
        
        self.__gerar_graficos((self._entradas, self._saidas), (LMS_ciclos, LMS_erro), FRONTEIRA)
        
        self._ciclos = ciclos
        return (w, b)
            
    
    def testa(self):
        if not self._w or not self._b:
            self._w, self._b = self.treino()
            
        amostras = len(self._entradas)
        print("-" * 115)
        
        print(f"PESOS\n\tW: {self._w}\n\tB: {self._b}\n\tTaxa de Aprendizagem: {self._taxa_aprendizagem}\n\tCiclos: {self._ciclos}")
        
        print("\n\t[X]\t\t\t[Y]\t\t\t[Y Líquido]\t\t\t[DIFERENÇA]\n" + "-" * 115)
        for i in range(amostras):
            y = self._w * self._entradas[i] + self._b
            print(f"\t{self._entradas[i]}\t\t{self._saidas[i]}\t\t{y}\t\t{abs(self._saidas[i] - y)}")
        
        return None
    
    
    @staticmethod
    def __gerar_graficos(PONTOS, LMS, FRONTEIRA):
        plt.figure('1')
        plt.title('Regra Delta (LMS)')
        plt.plot(LMS[0], LMS[1])
        plt.xlabel("Ciclos")
        plt.ylabel("Erro Quadrático")
        plt.savefig("./imgs/erro_quadratico.png")
        
        plt.figure('2')
        plt.title("Fronteira de Separação")
        plt.plot(PONTOS[0], PONTOS[1], 'bs', FRONTEIRA[0], FRONTEIRA[1], '--r')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.savefig("./imgs/fronteira_separacao.png")
        
        output_file('./graph/adaline.html')
        
        figura_fronteira = figure(title='Fronteira de Separação', x_axis_label='X', y_axis_label='Y', width=800, tools=['pan','box_zoom','wheel_zoom','hover','save','reset'])
        figura_fronteira.square(PONTOS[0], PONTOS[1], legend_label='Dados', size=10, color='blue')
        figura_fronteira.line(FRONTEIRA[0], FRONTEIRA[1], legend_label='Fronteira', color='red', line_width=5, line_dash='dashed')
        
        figura_erro = figure(title='Erro Quadrático', x_axis_label='ciclos', y_axis_label='Erro', width=800, tools=['pan','box_zoom','wheel_zoom','save','reset','hover'])
        figura_erro.line(LMS[0], LMS[1], legend_label='Erro', color='red', line_width=5, line_dash='dashed')
        
        layout = gridplot([[figura_erro], [figura_fronteira]])
        show(layout)
        
        return None


__all__ = ['Adaline', 'recupera_dados']   
    