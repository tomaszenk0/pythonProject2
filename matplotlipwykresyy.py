import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import math

#prosta krecha
# y = np.arange(2,9,2)
# plt.plot(y)
# plt.show()

#rosnaca krecha z punktami
# x = np.array([1,2,3,4])
# y = x**2
# plt.plot(x, y, 'ro-')
# plt.axis([0,6, 0,20])
# plt.plot(x, y, 'r-')
# plt.plot(x, y, 'o')
# plt.axis([0,6, 0,20])
# plt.show()

#linie kwadraty trojkaty, zapis zdjecia pil
#a = np.arange(0, 5, 0.2)
# plt.plot(a, a, 'r-', a, a**2, 'bs', a, a**3, 'g^')
# plt.legend(labels=['liniowa', 'kwadratowa', 'sześcienna'], loc='center left')
# plt.show()

# plt.plot(a, a, 'r-', label='liniowa')
# plt.plot(a, a**2, 'bs', label='kwadratowa')
# plt.plot(a, a**3, 'g^', label='sześcienna')
# plt.legend()
# plt.title('wykres')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.savefig('wykres.png')
# plt.show()
# img= PIL.Image.open('wykres.png')
# img = img.convert('RGB')
# img.save('wykres.jpg')

# x = np.arange(0, 5, 0.2)
# plt.plot(x, x, 'r--', label='liniowa')
# plt.plot(x, x**2, 'bo', label='kwadratowa')
# plt.plot(x, x**3, 'g^', label='szescienna')
# plt.legend(loc='center')
# plt.show()

# sin cos tg ctg
# b= np.arange(0,10.1, 0.1)
# plt.plot(b, np.sin(b), 'r-', label='sinus')
# plt.plot(b, np.cos(b), 'g', label='cos')
# plt.plot(b, np.tan(b), 'c', label='tan')
# plt.plot(b, 1/np.tan(b), 'b', label='ctan')
# plt.ylim(-4, 4)
# plt.legend()
# plt.show()

# kropki
# data = {'a': np.arange(50),
#         'c': np.random.randint(0,50,50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# plt.scatter('a', 'b', c='c', s='d', data=data, cmap='plasma')
# plt.xlabel('a')
# plt.ylabel('b')
# plt.show()

#wykres sin i cos
# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
# plt.subplot(2, 1, 1)
# plt.plot(x1, y1)
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('wykres sin(x)')
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2)
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()

#wykres sin i cos 4 sloty pionowo 1top sin 4bottom cos
# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
# plt.subplot(4, 1, 1)
# plt.plot(x1, y1)
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('wykres sin(x)')
# plt.subplot(4, 1, 4)
# plt.plot(x2, y2)
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()

#wykres na 6 slotow (topl rightm botl)
# fig, axs = plt.subplots(3, 2)
# axs[0, 0].plot(x1,y1,'r')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('sin(x)')
# axs[0, 0].set_title('wykres sin(x)')
# axs[1, 1].plot(x2,y2,'g')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('cos(x)')
# axs[1, 1].set_title('wykres cos(x)')
# axs[2, 0].plot(x1,y1,'r')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('sin(x)')
# axs[2, 0].set_title('wykres sin(x)')
# fig.delaxes(axs[0,1])
# fig.delaxes(axs[1,0])
# fig.delaxes(axs[2,1])
# plt.show()

# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
# y1 = np.sin(x1 * np.pi * 2)
# y2 = np.cos(x2 * np.pi * 2)
# fig, axs = plt.subplots(3, 2)
# axs[0, 0].plot(x1, y1)
# axs[0, 0].set_title('Sinus')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('y')
# axs[1, 1].plot(x2, y2)
# axs[1, 1].set_title('Cosinus')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('y')
# axs[2, 0].plot(x1, y1, 'r')
# axs[2, 0].set_title('Sinus')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('y')
# plt.subplots_adjust(hspace=0.5, wspace=0.5)
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
# plt.show()

#random niebieski gory
# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# ts.plot()
# plt.show()

# populacja na kontynentach wykres slupkowy suma
# data={'Kraj':['Belgia','Indie','Brazylia','Polski'],
# 'Stolica':['Bruksela','New Delhi','Brasilia','Warszawa'],
# 'Kontynent':['Europa','Azja','Ameryka Południowa','Europa'],
# 'Populacja':[11109846,1303171035,207847528,39674311]}
# df=pd.DataFrame(data)
# grupa=df.groupby('Kontynent').agg({'Populacja':['sum']})
# grupa.plot(kind='bar',xlabel='kontynent',ylabel='Populacja',legend=True, title='Populacja na kontynent',rot=0)
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Kontynenty')
# wykres.set_ylabel('Populacja')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('Populacja na kontynentach')
# plt.show()

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467]}
#
# df = pd.DataFrame(data)
# print(df)
# grupa = df.groupby('Kontynent')
# etykiety = list(grupa.groups.keys())
# wartosci = list(grupa.agg('Populacja').sum())
# plt.bar(etykiety, wartosci, color=['yellow', 'red', 'green'])
# plt.xlabel('Kontynenty')
# plt.ylabel('Populacja')
# plt.show()
# grupa = df.groupby('Kontynent').agg({'Populacja': ['sum']})
# print(grupa)
# grupa.plot(kind='bar', xlabel='Kontynenty', ylabel='Populacja',
#            legend=True, rot=0, title='Populacja na kontynentach')
# plt.savefig('wykres.png')
# plt.show()

# pobieranie danych z excela
# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
# grupa = df.groupby('Imię i nazwisko').agg({'Wartość zammówienia':['sum']})
# grupa.plot(kind='pie', subplots='True', autopct='%.2f%%',
# fontsize=20, colors=['red','green'])
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
# grupa = df.groupby('Imię i nazwisko').agg('Wartość zamówienia')
# grupa.plot(kind='pie', subplot=True, autopct='%.2f%%', fontsize=20, figsize=(6, 6), colors=['red', 'green'])
# plt.legend(loc='lower right')
# plt.title('Procent zamowienia dla sprzedawcy')
# plt.show()

#wykres kolowy z excela
# df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
# print(df)
# seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
# wedges, texts, autotext = plt.pie(x=seria, labels=seria.index,
# autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"), colors=['red','green'])
# plt.title('Suma zamowien dla sprzedawcow')
# plt.legend(loc='lower right')
# plt.ylabel('procentowy wynik wartosci zamowienia')
# plt.show()

# random wykresy 2 linie zoltle i niebieskie
# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# df = pd.DataFrame(ts, columns=['wartosci'])
# print(df)
# df['Srednia kroczaca'] = df.rolling(window=50).mean()
# df.plot()
# plt.legend()
# plt.show()

#ukosny
# plt.plot([1, 3, -5, 7])
# plt.show()

# wykres sinusa na przedziale x<0,10> wartosci zmieniaja sie co 0.1
# x = np.arange(0, 10, 0.1)
# y = [math.sin(i) for i in x]
# plt.plot(x, y)
# plt.xlabel('os x')
# plt.ylabel('os y')
# plt.legend(labels=['sin(x)'])
# plt.title('wykres liniowy funkcji sinus')
# plt.show()

#kropki
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)
# }
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
# plt.scatter('a', 'b', c='c', s='d', data=data, cmap='plasma')
# plt.xlabel('klucz a')
# plt.ylabel('klucz b')
# plt.show()

# zielona gora
# x = np.random.randn(10000)
# plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=False)
# plt.xlabel('Wartości')
# plt.ylabel('Prawdopodobieństwo')
# plt.title('Histogram')
# plt.grid()
# plt.show()

# 1. funkcja/przedzial na x/ukladanie elementow/ przedzialy z jakiej strony
# 2. siatka z pliku/wektor z x/y legenda/
# 3. macierz i wyciaganie elementow
# 4 i 5 wykresy na danych / slupkowy kolowy / punktowy liniowy / otwarcie wczytywanie pliku
# etykiety limity na osiach
