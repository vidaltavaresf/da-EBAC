
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')
df.plot(x='dia', y='venda')
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.savefig('gasolina.png')
plt.show
