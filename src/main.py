from adaline import *
from regressao import *

def main():
    base_dados = "basedeobservacoes.txt"
    
    adaline = Adaline(base_dados, 0.001)  
    w, b = adaline.treino()
    adaline.testa()
    
    X, Y = recupera_dados(base_dados)
    coeficientes, correlacao = calcular_regressao(X, Y, (w, b))
    
    print("\n" + "-" * 115)
    print("Cálculos da Regressão Linear")
    print(f"\t[+] Coeficiente de Correlação r = {correlacao}")
    print(f"\t[+] Coeficiente de Determinação r² = {correlacao**2}")
    print(f"\t[+] Erro Média Quadrática: {MSE(X, Y)}")
    print(f"\t[+] Erro Raiz Média Quadrática: {RMSE(X, Y)}")
    print(f"\t[+] Erro Médio Absoluto: {MAE(X, Y)}")
    print(f"\t[+] Erro R²: {R2(X, Y)}")
    
    print(f"\n\n\t[+] Regressão: Y = {coeficientes[1]} * X + {coeficientes[0]}")
    print(f"\t[+] Adaline: Y = {w} * X + {b}")
    
    
if __name__ == '__main__':
    main()
    
    