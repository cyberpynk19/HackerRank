import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class EqOnda():
    def __init__(self, A, Lambda, velocidade):
        self.A = A
        self.Lambda = Lambda
        self.velocidade = velocidade
        self.T = self.Lambda / self.velocidade
        self.pi = 2*np.pi
        self.velocidadeOnda = self.Lambda / self.velocidade

    def calculo(self, x, t):
        variacao = self.A * np.cos((self.pi/self.Lambda) * x - (self.pi/self.T) * t)
        return variacao

    def relatorio(self, x, t):
        for i in range(len(x)):
            for j in range(len(t)):
                variacao = self.calculo(x[i], t[j])
                print(f"Para x = {x[i]} e t = {t[j]}, a função de onda é {variacao:.3f}")

class AnimacaoEqOnda(EqOnda):
    def __init__(self, A, Lambda, velocidade):
        super().__init__(A, Lambda, velocidade)
        self.x = np.linspace(0, 10, 100)
        self.t = np.linspace(0, 50, 200)
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(self.x, self.calculo(self.x, self.t[0]))

    def animacao(self, frame):
        # Atualiza a posição do tempo t
        t_atual = self.t[frame]
        # Calcula a função de onda para todos os pontos em x
        y = self.calculo(self.x, t_atual)
        # Atualiza a posição da curva no gráfico
        self.line.set_ydata(y)
        # Adiciona o título com o tempo atual
        self.ax.set_title(f"Tempo = {t_atual:.2f}")
        return [self.line]

eq_onda = AnimacaoEqOnda(3, 4, 0.5)
animacao = FuncAnimation(eq_onda.fig, eq_onda.animacao, frames=len(eq_onda.t), interval=50)
eq_onda.relatorio(eq_onda.x, eq_onda.t)
plt.show()
