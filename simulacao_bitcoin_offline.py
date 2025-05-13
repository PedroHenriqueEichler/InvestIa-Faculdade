# Estrutura inicial do projeto Investe.AI - Simulação com Ações da Petrobras (PETR4)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

SEED = 42
np.random.seed(SEED)
random.seed(SEED)

data = pd.DataFrame({
    'Open':   [25.10, 25.60, 26.00, 25.90, 26.20, 26.50, 26.40, 26.80, 27.10, 27.00],
    'High':   [25.70, 26.10, 26.50, 26.30, 26.80, 26.90, 26.70, 27.00, 27.30, 27.20],
    'Low':    [24.90, 25.30, 25.80, 25.60, 25.90, 26.20, 26.10, 26.60, 26.90, 26.80],
    'Close':  [25.50, 26.00, 26.20, 26.00, 26.60, 26.60, 26.50, 26.90, 27.10, 27.05],
    'Volume': [1000000, 1200000, 1100000, 1150000, 1250000, 1300000, 1270000, 1350000, 1400000, 1380000]
})

class SimpleTradingSim:
    def __init__(self, df, initial_balance=10000):
        self.df = df.reset_index()
        self.initial_balance = initial_balance
        self.reset()

    def reset(self):
        self.balance = self.initial_balance
        self.shares_held = 0
        self.net_worth = self.initial_balance
        self.history = []

    def step(self, index):
        row = self.df.iloc[index]
        action = self.decide_action(index)

        if action == 1: 
            shares_bought = int(self.balance // row['Close'])
            self.balance -= shares_bought * row['Close']
            self.shares_held += shares_bought

        elif action == 2: 
            self.balance += self.shares_held * row['Close']
            self.shares_held = 0

        self.net_worth = self.balance + self.shares_held * row['Close']
        self.history.append({
            'Dia': index + 1,
            'Acao': ['Hold', 'Buy', 'Sell'][action],
            'Preco': row['Close'],
            'Saldo': round(self.balance, 2),
            'Acoes': self.shares_held,
            'Patrimonio': round(self.net_worth, 2)
        })

    def decide_action(self, index):
        if index == 0:
            return 0
        if self.df.iloc[index]['Close'] > self.df.iloc[index - 1]['Close']:
            return 1  
        elif self.df.iloc[index]['Close'] < self.df.iloc[index - 1]['Close']:
            return 2  
        else:
            return 0  

    def run(self):
        for i in range(len(self.df)):
            self.step(i)
        return pd.DataFrame(self.history)

sim = SimpleTradingSim(data)
resultados = sim.run()

print(resultados[['Dia', 'Acao', 'Preco', 'Saldo', 'Acoes', 'Patrimonio']])

plt.figure(figsize=(10, 5))
plt.plot(resultados['Dia'], resultados['Patrimonio'], marker='o', linestyle='-')
plt.title("Evolução do Patrimônio - Simulação PETR4")
plt.xlabel("Dia")
plt.ylabel("Valor em R$")
plt.grid(True)
plt.tight_layout()
plt.show()
