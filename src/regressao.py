from adaline import *
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show, output_file
import numpy as np


def coef_correlacao(X, Y):
    n = len(X)
    soma_x = sum(X)
    soma_y = sum(Y)
    soma_xy = sum( [x * y for x, y in zip(X, Y)] )
    soma_x2 = sum( [x**2 for x in X] )
    soma_y2 = sum( [y**2 for y in Y] )
    
    numerador = n * soma_xy - soma_x * soma_y
    denominador = ((n * soma_x2 - soma_x**2) ** (.5)) * ((n * soma_y2 - soma_y**2) ** (.5))
    
    return numerador / denominador


def regressao(X, Y):
    n = len(X)
    soma_x = sum(X)
    soma_y = sum(Y)
    soma_xy = sum( [x * y for x, y in zip(X, Y)] )
    soma_x2 = sum( [x**2 for x in X] )
    
    numerador = n * soma_xy - soma_x * soma_y
    denominador = n * soma_x2 - soma_x ** 2
    b = numerador / denominador
    
    x_medio, y_medio = sum(X) / n, sum(Y) / n
    a = y_medio - b * x_medio
    
    return a, b


def gerar_graficos(coeficientes, pontos, pesos_adaline):
    X, Y = pontos
    a, b = coeficientes
    w, bias = pesos_adaline
    
    x_reg = np.arange(-4, 11., 0.5)
    y_reg = [b * i + a for i in x_reg]
    
    x_adaline = np.arange(-4, 11., 0.5)
    y_adaline = [w * i + bias for i in x_adaline]
    
    output_file('./graph/regressao_adaline.html')
    figura = figure(title='Regresão Linear | Adaline', x_axis_label='X', y_axis_label='Y', width=900, tools=['pan','box_zoom','reset','save','hover','wheel_zoom'])
    figura.square(X, Y, legend_label='Dados', size=10, color='blue')
    figura.line(x_reg, y_reg, legend_label='Regressão Linear', color='red', line_width=5, line_dash='dashed')
    figura.line(x_adaline, y_adaline, legend_label='Adaline', color='green', line_width=5, line_dash='dashed')
    show(figura)
    
    plt.figure('3')
    plt.title('Regressão Linear')
    plt.plot(X, Y, 'bs', x_reg, y_reg, '--r', x_adaline, y_adaline, '--g')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig('./imgs/regressao.png')
    
    return None


def calcular_regressao(X, Y, PESOS_ADALINE):
    r = coef_correlacao(X, Y)
    
    a, b = regressao(X, Y)
    
    gerar_graficos((a, b), (X, Y), PESOS_ADALINE)

    return (a, b), r



def MSE(X, Y):
    ''' Erro média quadrática '''
    erro = 0
    a, b = regressao(X, Y)
    for x, y in zip(X, Y):
        y_reg = b * x + a
        erro += (y - y_reg) ** 2
        
    return erro / len(X)


def RMSE(X, Y):
    ''' Erro raiz média quadrática '''
    return MSE(X, Y) ** .5


def MAE(X, Y):
    ''' Erro médio absoluto '''
    erro = 0
    a, b = regressao(X, Y)
    for x, y in zip(X, Y):
        y_reg = b * x + a
        erro += abs(y - y_reg)
        
    return erro / len(X)


def R2(X, Y):
    ''' R Quadrado '''
    numerador = MSE(X, Y) * len(X)
    
    y_medio = sum(Y) / len(Y)
    denominador = sum([(y - y_medio)**2 for y in Y])
    
    return 1 - numerador / denominador


__all__ = ['calcular_regressao', 'MSE', 'RMSE', 'MAE', 'R2']