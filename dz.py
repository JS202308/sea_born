import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# df = sns.load_dataset('tips')
# sns.histplot(data=df, x='total_bill', bins=20, kde=True, hue='smoker', color=['blue', 'red'], alpha=0.5)
# plt.title('Розподіл Суми Рахунку за Категорією Курців')
# plt.xlabel('Сума Рахунку (USD)')
# plt.ylabel('Щільність Ймовірності')
# plt.legend(title='Курці', labels=['Ні', 'Так'])
# plt.show()

#завдання 2

# df = sns.load_dataset('tips')
# sns.histplot(data=df, x='total_bill',bins=20, kde=True, color='brown', alpha=0.7, linewidth=3)
# plt.title('Розподіл Суми Рахунку з Налаштуваннями Графіка')
# plt.xlabel('Сума Рахунку (USD)')
# plt.ylabel('Щільність Ймовірності')
# plt.show()

#Включіть категоріальні змінні у кореляційну матрицю, перетворивши їх на числові коди.


# df = sns.load_dataset('penguins')
# data = df.select_dtypes(include=[float, int])
# data = data.corr()
# print(data)