import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import math
print(matplotlib.rcParams.keys())

# 2 wykresy liniowe
# sns.set(rc={'figure.figsize':(8, 6)})
# sns.set()
# sns.lineplot(x=[1, 2, 3, 4], y=[1, 4, 9, 16], label='linia nr',color='red', marker='o', linestyle=':')
# sns.lineplot(x=[1, 2, 3, 4], y=[2, 5, 10, 17], label='linia nr',color='green', marker='o', linestyle=':')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('wykres liniowy')
# plt.show()

# wykres liniowy gorki
# sns.set()
# s = pd.Series(np.random.randn(1000))
# s = s.cumsum()
# wykres = sns.relplot(kind='line', data=s, label='dane z serii')
# wykres.fig.set_size_inches(8, 6)
# wykres.fig.suptitle('Wykres liniowy')
# wykres.set_xlabels('indeksy')
# wykres.set_ylabels('wartości')
# wykres.add_legend()
# wykres.figure.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
# plt.show()

#pobieranie z pliku
#sepal length,sepal width,petal length,petal width,class
# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# print(df)
# sns.lineplot(data=df, x=df.index, y='sepal length', hue='class',
# palette=['yellow','green','red'])
# plt.xlabel('indeksy')
# plt.title('wykres liniowy danych z iris dataset')
# plt.show()

#kropki
# data={'a': np.arange(50),
# 'c': np.random.randint(0, 50, 50),
# 'd': np.random.randn(50)}
# data['b']= data['a'] + 10 * np.random.randn(50)
# data['d']= np.abs(data['d']) * 100
# df = pd.DataFrame(data)
# plot = sns.relplot(data=df, x='a', y='b', hue='c', palette='bright',
#                   size='d', legend=True)
# plot.set(xticks=data['a'])
# plt.show()

#wykres slupkowy
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#          'Kontynent': ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa'],
#          'Populacja': [11190846, 1303171035, 207847528, 38675467]}
# df = pd.DataFrame(data)
# plot = sns.barplot(data=df, x='Kontynent', y='Populacja', hue='Kontynent',
# estimator=np.sum, errorbar=None, dodge=False, palette=['red','green','blue'])
# plot.legend(title='Populacja na kontynentach')
# plot.set(title='Wykres słupkowy')
# plt.show()
zad1 
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(2, 9.5, 0.5)
y = np.sqrt(x + 3*x) / (4*x + 5)
plt.plot(x, y,'r',label='f(x) = (sqrt(x)+3*x) / (4x + 5)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x)')
plt.legend()
plt.xlim(2, 9)
plt.show()
zad2
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-3,5.5,0.5)
y = x**2 + (np.sin(x**2) / x)
plt.plot(x, y, "r^", label="x^2 + (sin(x^2)/x)")
plt.xlabel("x")
plt.ylabel("wykres funkcji")
plt.title("x^2 + (sin(x^2)/x)")
plt.xlim(-3, 5)
plt.ylim(-1.5, 26)
plt.legend(loc="upper left")
plt.savefig(‘imię_nazwisko_nr_zadania.png')
plt.show()

            zad3
           import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('handel.csv')
plt.figure(figsize=(10, 6))
df_stacje_paliw = df[df['Wyszczegolnienie'] == 'stacje paliw']
grouped = df_stacje_paliw.groupby('Wyszczegolnienie')['Wartosc'].sum()
grouped.plot(kind='bar')
plt.ylabel('Suma wartości')
plt.xlabel('Stacja paliw')
plt.xticks(fontsize=14, rotation='horizontal')
plt.xticks([])  # Usunięcie etykiet słupków
plt.title('Wartości dla stacji paliw na przestrzeni lat')
plt.savefig('imie_nazwisko_nrzadania.png')
plt.show()
            zad4
        import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('handel.csv')
grouped = df.groupby('Wyszczegolnienie')['Wartosc'].sum()
grouped = grouped.round(2)
plt.rcParams['font.size'] = 14
fig, ax = plt.subplots(figsize=(10, 6))
grouped.plot(kind='bar', ax=ax)
plt.xlabel('Wyszczególnienie')
plt.ylabel('Całkowita wartość')
plt.title('Całkowita wartość dla obydwu wyszczególnień na przestrzeni lat')
ax.legend(["Stacje paliw", "Sklepy"])
plt.savefig('imie_nazwisko_nrzadania.png')
plt.show()
