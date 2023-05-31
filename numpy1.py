import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import math

#inicjalizacja tablicy
#a = np.array([[0, 1], [2, 3]])
#print(a)
#lub drugi sposób
#a = np.arange(2, 5, 0.1)
#print(a)

# #wypisanie typu zmienej tablicy (nie jej elementów)
# print(type(a))

# #sprawdzenie typu danych tablicy
# print(a.dtype)

# #inicjalizacja tablicy z konkretnym typem danych
# a = np.arange(2, dtype='int64')
# print(a.dtype)

# #zapisywanie kopii tablicy jako tablicy z innym typem
# b = a.astype('float')
# print(b)
# print(b.dtype)

# #wypisanie rozmiaru tablicy
# print(b.shape)

# #można też sprawdzić ilość wymiarów tablicy
# print(a.ndim)

# #stworzenie tablicy wielowymiarowej może wyglądać tak
# parametrem przekazywanym do funkcji array jest obiekt,
# może to być pythonowa lista
# m = np.array([np.arange(2), np.arange(2)])
# print(m.shape)
# #ponownie typem jest ndarray
# print(type(m))

# 3 rodzaje tablic
# zera = np.zeros((5, 5), dtype='int32')
# jedynki = np.ones((4, 4))
# print(zera)
# print(jedynki)
# #warto sprawdzić jaki jest domyslny typ danych takich tablic
# print(zera.dtype)
# print(jedynki.dtype)
# #można również stworzyć "pusta" macierz o podanych wymiarach
# #wartości umieszane są losowo, najpierw podawana jest
# pusta = np.empty((2, 2))
# print(pusta)
# #przez indexy
# macierz = np.array([[12, 11], [2, 1]])
# print(macierz)
# #do elementów tablicy możemy odwołać się tak jak do elementów
# poz_1 = macierz[1, 1]
# poz_2 = macierz[0][1]
# print(poz_1)
# print(poz_2)

# #tworzenie macierzy 2x2 wraz z uzupełnieniem
# macierz2 = np.array([[1,2],[3,4]])
# print(macierz2)
# #funcka arange potrafi także tworzyć ciągi liczb zmiennych
# liczby = np.arange(1,2,0.1)
# print(liczby)
# #podobnie działa funkcja linspace, które działanie jest
# liczby_lin = np.linspace(1,2,5, endpoint=False)
# print(liczby_lin)
# #a teraz możemy utworzyć dwie macierze, najpierw wartości
# z = np.indices((5, 3))
# print(z)
# print(z[0][1][2])

# #podobnie jak w matlabie możemy tworzyć macierze diagonalną
# mat_diag = np.diag([a for a in range(5)], k=1)
# mat_diag = np.diag([a for a in range(5)], k=-1)
# print(mat_diag)
# #mat_diag_k = np.diag([a for a in range(5)], 1)
# #print(mat_diag_k)
# #nump 1wymiarowa
# #z = np.fromiter(range(5), dtype='int32')
# #print(z)

# #znaki
# znaki = b'ogolna'
# z1 = np.frombuffer(znaki,dtype='S1')
# print(z1)
# z2 = np.frombuffer(znaki,dtype='S2')
# print(z2)
# #
# znaki = 'ogolna'
# z3 = np.array(list(znaki))
# z4 = np.array(list(znaki), dtype='S1')
# z5 = np.array(list(b'ogolna'))
# z6 = np.fromiter(znaki,dtype='S1')
# print(z3)
# print(z4)
# print(z5)
# print(z6)
# #
# a = np.arange(10)
# print(a)
# s = slice(2,7,2)
# print(a[s])
# s = range(2,7,2)
# print(a[s])

# #możemy ciąć tablice również w sposób znany z cięcia linii
# print(a[2:7:2])
# #lub
# print(a[1:])
# print(a[2:5])
# #
# mat = np.arange(25)
# #jednowymiarowa w macierz
# mat = mat.reshape((5,5))
# print(mat)
# print(mat[1:]) #od 2 wiersza
# print(mat[:, 1]) #2 kolumna jako wektor
# print(mat[:, -1]) #ostatnia kolumna
# print(mat[2:5, 1:3]) #2 i 3 kolumna dla 3,4,5 wierszy
# print(mat[:, [2,4]]) # 3 i 5 kolumna
# print('')

# #wierzcholki macierzy
# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print(x)
# rows = np.array([[0, 0], [3, 3]])
# cols = np.array([[0, 2], [0, 2]])
# y = x[rows,cols]
# print(y)
# ###

# ZAD1 Za pomocą funkcji arange stwórz tablicę numpy składającą się z 20 kolejnych wielokrotności liczby 4
# print('ZAD1')
# arr = np.arange(20) * 4
# print(arr)

# # ZAD2 Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej
# kopię przekonwertowaną na typ int32
# print('ZAD2')
# lst_float = [1.2, 2.3, 3.4, 4.5, 5.6]
# lst_int32 = np.array(lst_float, dtype='int32')
# print(lst_int32)

# # ZAD3 Napisz funkcję, która będzie:
# • Przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
# • Zwracała tablicę Numpy o wymiarach n*n kolejnych potęg liczby 2
# print('ZAD3')
# def podwa(n):
#     return np.array([2 ** i for i in range(n * n)]).reshape((n, n))
# print(podwa(3))
#
# # ZAD4 Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji
# potęgowania oraz ilość kolejnych potęg do wygenerowania. Korzystając z funkcji logspace generuj
# tablicę jednowymiarową kolejnych potęg podanej liczby, np. generuj(2,4) -> [2,4,8,16]
# print('ZAD4')
# def generuj(base, n):
#     return np.logspace(0, n - 1, n, base=base)
# print(generuj(2, 4))
#
#
# # ZAD5 Napisz funkcję, która:
# • Na wejściu przyjmuje jeden parametr określający długość wektora
# • Na podstawie parametru generuj wektor, ale w kolejności odwróconej
# • Generuj macierz diagonalną z w/w wektorem na przekątnej oddalonej o 2 w górę od głównej
# przekątnej macierzy
# print('ZAD5')
# def macierz(n):
#     reversed_vector = np.arange(n)[::-1]
#     diagonal_vector = np.diag(reversed_vector, k=2)
#     return diagonal_vector
# print(macierz(5))

# # ZAD6 Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci
# wykreślanki, gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie.
# Jedno z tych słów powinno być wypisane od prawej do lewej
# print('ZAD6')
# words = ['macierz', 'numpy', 'python', 'wektor']
# n_rows = len(words)
# n_cols = max(len(word) for word in words)
# macierz = np.zeros((n_rows, n_cols), dtype='U1')
# for i, word in enumerate(words):
#     macierz[i, :len(word)] = list(word)
# for i in range(n_rows):
#     for j in range(n_cols):
#         if macierz[i, j] != '':
#             print(macierz[i, j], end=' ')
#         else:
#             print(' ', end=' ')
#     print()
# diagonal_word = 'main'
# for i in range(len(diagonal_word)):
#     macierz[i, n_cols - len(diagonal_word) + i] = diagonal_word[i]
# print()
# for i in range(n_rows):
#     for j in range(n_cols):
#         if macierz[i, j] != '':
#             print(macierz[i, j], end=' ')
#         else:
#             print(' ', end=' ')
#     print()
#
# # ZAD7 Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
# [[2 4 6]
# [4 2 4]
# [6 4 2]]
# Przy założeniach:
# funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i umieszcza wielokrotność
# liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.
# print('ZAD7')
# def genmacierz(n):
#     macierz = np.zeros((n, n), dtype=int)
#     for i in range(n):
#         macierz[i, i] = 2 * (i + 1)
#         if i < n - 1:
#             macierz[i, i + 1] = 2 * (i + 1)
#             macierz[i + 1, i] = 2 * (i + 1)
#     return macierz

# def generuj_macierz(n):
#     macierz = np.zeros((n, n))
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 macierz[i, j] = (i + 1) * 2
#             elif i == j + 1 or i == j - 1:
#                 macierz[i, j] = 2
#     return macierz
#
# n = 3
# wynik = generuj_macierz(n)
# print(wynik)
# # ZAD7
# print('ZAD7')
# def genmacierz(n):
#     macierz = np.zeros((n, n), dtype=int)
#     for i in range(n):
#         macierz[i, i] = 2 * (i + 1)
#         if i < n - 1:
#             macierz[i, i + 1] = 2 * (i + 1)
#             macierz[i + 1, i] = 2 * (i + 1)
#     return macierz
#
#
# # ZAD8 Zadanie 8
# Napisz funkcję, która:
# • jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr
# ‘kierunek’,
# • parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
# • funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat, że ilość
# wierszy lub kolumn, w zależności od kierunku podziału, nie pozwala na operację)
#     print('ZAD8')
# def podziel_tablice(tablica, kierunek):
#     if kierunek == 'pionowo':
#         if tablica.shape[0] % 2 != 0:
#             print("Ilość wierszy nie pozwala na podział.")
#             return None
#         podziel = np.split(tablica, 2, axis=0)
#     elif kierunek == 'poziomo':
#         if tablica.shape[1] % 2 != 0:
#             print("Ilość kolumn nie pozwala na podział.")
#             return None
#         podziel = np.split(tablica, 2, axis=1)
#     else:
#         print("Nieprawidłowy kierunek podziału.")
#         return None
#     return podziel
#
# tablica = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# kierunek = 'pionowo'
# wynik = podziel_tablice(tablica, kierunek)
# if wynik is not None:
#     print(wynik)

#     # ZAD9 Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz macierz 5x5, która będzie
# zawierała kolejne wartości ciągu arytmetycznego.
# start = 1  # Wartość początkowa ciągu arytmetycznego
# krok = 2  # Różnica pomiędzy kolejnymi elementami ciągu
# macierz = np.arange(start, start + 5*5*krok, krok).reshape(5, 5)
# print(macierz)




import numpy as np
import matplotlib.pyplot as plt

print('ZADANIE 1')
#Za pomocą biblioteki matplotllib utwórz wykres liniowy funkcji f(x) = cos(x)/x^2, dla x w przedziale [3,7],
#wartości x zmieniają się co 0.25. Dodaj odpowiednie etykiety
#do osi wykresu, tytuł linii, legendę, oraz tytuł wykresu.
#Dodatkowo wyświetl oba wektory przekazywane na wykres.
#Ustaw zakres oś x na granice przedziału

# Utwórz wektor x z wartościami od 3 do 7 z krokiem 0.25
x = np.arange(2.75, 7.25, 0.25)

# Oblicz wartości funkcji f(x)
fodx = np.cos(x) / x**2

# Utwórz wykres liniowy
plt.plot(x, fodx, 'b-', label='f(x)=cos(x)/x^2')

# Dodaj etykiety osi
plt.xlabel('x')
plt.ylabel('y')

# Ustaw zakres osi x
plt.xlim(3, 7)

# Dodaj tytuł wykresu
plt.title('Wykres funkcji')

# Dodaj legendę
plt.legend()

# Wyświetl oba wektory przekazywane na wykres
plt.show()

print('\n ZADANIE 2- pierwszy wykres')
#Odwzorowywanie funkcji

#definiowanie funkcji kwadratowej
def f(x):
    return 5 * x**2 + 3 * x + 2

#określenie zakresów
plt.axis([-4, 4, 0, 100])

# Tworzenie wektora x
x = np.linspace(-10, 10, 100)
# Zakres od -10 do 10, 100 równoodległych punktów

# Obliczanie wartości funkcji f(x) dla każdego punktu x
y = f(x)

# Tworzenie wykresu
plt.plot(x, y)

# Dodawanie etykiet osi
plt.xlabel('x')
plt.ylabel('wykres funkcji')

plt.plot(x, y, label='f(x) = (5 * x**2) * 3 * x + 2')  # Dodanie etykiety do krzywej

# Dodawanie tytułu wykresu
plt.title('Pierwszy Wykres')

plt.legend(loc='upper right')

# Wyświetlanie wykresu
plt.show()

print('\n ZADANIE 2- drugi wykres')
#Odwzorowywanie funkcji
x = np.linspace(-10, 10, 100)
y = (-2 * x ** 3) + 5
plt.axis([-4, 4, -100, 100])
plt.plot(x, y, 'g-', linewidth=5, label='-2x^3 + 5')

plt.xlabel('x')
plt.ylabel('wykres funkcji')
plt.title('Drugi wykres')

plt.legend(loc='upper center')

plt.show()

print('\n ZADANIE 3')
# używając biblioteki pandas wczytaj zawartości pliku 'wine.data' do ramki danych i wykonaj następujące kroki:
# 1. Utwórz nową ramkę danych, gdzie znajdzie się sto losowych wierszy, wiersze mogą się powtarzać.
# 2. na nowej ramce danych dokonaj grupowania danych  po kolumnie class.
# 3. na wykresie kołowym przedstaw  procentowy udział każdej z klasy


# df = pd.read_csv('wine.data')
#
# print(df)
#
# randomowe = [np.random.randint(0, len(df)-1) for _ in range(100)]
# df2 = df.iloc[randomowe]
#
# grupy = df2.groupby('Class').size()
#
# plt.pie(grupy, labels=grupy.index, autopct='%1.1f%%')
# plt.legend()
# plt.title("Udział klas")
# plt.show()

print('ZADANIE 4')

# za pomocą biblioteki pandas wczytaj zawartość pliku "wine.data",
# następnie na wykresie kolumnowym z biblioteki seaborn przedstaw średnie wartości alkoholu dla każdej  z klasy (kolumny alcohol i class).
# Na wykresie mają być podpisane etykiety dotyczące osi, legenda, tytuł wykresu. Ustaw styl wykresu na podstawowy.

# df1 = pd.read_csv('wine.data')
# plt.show()
#
# plot = sns.barplot(data=df1, x='Class', y='Alcohol',
#                    errorbar=None, hue='Class', estimator=np.mean,
#                    dodge=False, palette=['red', 'green', 'yellow'])
# plot.legend(title='Klasa')
# plot.set(title='Średnie Wartośći Alkoholu')
#
# plt.show()

Grupa 3 zestaw A
#Zadanie 1
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 5, 25)
y = (8*x**2)/4 + np.cos(x)
plt.plot(x, y, label='f(x) = (8*x**2)/4 + cos(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x)')
plt.legend()
plt.xlim(-3, 5)
plt.scatter(x, y, color='red', label='Wartości punktów')
plt.legend()
plt.show()

Grupa 3 zestaw B
#Zadanie 1
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3, 5, 0.3)
y = (x**2 + 3*x) / 5 + np.sin(x)
plt.plot(x, y, label='f(x)=(x^2+3x)/5 + sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(-3, 5)
plt.legend()
plt.title('Wykres funkcji f(x)')
plt.show()

