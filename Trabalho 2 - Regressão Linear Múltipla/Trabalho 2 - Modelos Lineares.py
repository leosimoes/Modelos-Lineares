"""
Trabalho 2 de Modelos Lineares
Leonardo Simões e Leonardo T. Muzí de Carvalho
"""

import numpy as np
from numpy.linalg import inv
import matplotlib as mpl
import matplotlib.pyplot as plt

def lerArquivo(diretorio):
    arquivo = open(diretorio, 'r')
    X, Y = [], []
    for linha in arquivo:
        Y.append(float(linha.split()[0]))
        X.append([1.0]+[float(x) for x in linha.split()[1:]])
    arquivo.close()
    return (np.array(X),np.array(Y))

def QuadradosMinimos(X, Y):
    Xt = X.transpose()
    return (inv(Xt.dot(X)).dot(Xt)).dot(Y)

def plotarDispersãoBidimensional(X, Y, eixox):
    fig = plt.figure(1)
    plt.xlabel('Eixo '+ eixox[0])
    plt.ylabel('Eixo Y')
    plt.title('Dispersão Bidimensional entre Y e '+ eixox)
    plt.scatter(X, Y, label='Pontos', color='r', marker='o', s=10)
    plt.legend()
    plt.show()
    fig.savefig('Y vs ' + eixox +'.png')

def dispersãoBidimensional(X, Y):
    for i in range(1, len(X[0])):
        Xi = X[:,i]
        eixox = 'X'+str(i)
        plotarDispersãoBidimensional(Xi, Y, eixox)

def plotarResiduos(R):
    fig = plt.figure(1)
    plt.hist(R, bins=30)
    plt.title('Resíduos')
    plt.show()
    fig.savefig('Residuos.png')

#Coeficientes de correlação e determinação
def Sxx(X):
    soma = 0.0
    xm = np.average(X)
    for x in X:
        soma += (x - xm)**2
    return soma

def Syy(Y):
    soma = 0.0
    ym = np.average(Y)
    for y in Y:
        soma += (y - ym)**2
    return soma

def Sxy(X, Y):
    soma = 0.0
    xm = np.average(X)
    ym = np.average(Y)
    for i in range(len(X)):
        soma += (X[i] - xm)*(Y[i] - ym)
    return soma

def coeficienteDeCorrelacao(X, Y):
    return Sxy(X, Y)/((Sxx(X)*Syy(Y))**(1/2))

def coeficientesDeCorrelacaoMultiplos(X, Y):
    p = []
    for i in range(1, len(X[0])):
        p.append(coeficienteDeCorrelacao(X[:,i], Y))
    return p

def coeficienteDeDeterminacaoMultiplos(X, Y):
    R2 = []
    for i in range(1, len(X[0])):
        R2.append((coeficienteDeCorrelacao(X[:,i], Y)**2))
    return R2

#Função Principal - MAIN
if __name__ == '__main__':
    diretorio = 'D:\\data6_t2.txt'
    (X,Y) = lerArquivo(diretorio)

    #Item A
    dispersãoBidimensional(X, Y)
    
    #Item B
    p = coeficientesDeCorrelacaoMultiplos(X, Y)
    print('p = ', p)
    
    #Item C
    R2 = coeficienteDeDeterminacaoMultiplos(X, Y)
    print('R2 = ', R2)
    
    #Item D
    B = QuadradosMinimos(X, Y)
    print('B = ', B)
    
    #Item E
    Yc = np.dot(X, B)
    plotarDispersãoBidimensional(Y, Yc, 'Y^')
    print('Yc = ', Yc)
    
    #Item F
    R = np.subtract(Y, Yc)
    print('R = ', R)
    
    #Item G
    plotarResiduos(R)
