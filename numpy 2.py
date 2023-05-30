import numpy as np
#ZAD1  Utwórz dwie macierze1x3 różnych wartości a następnie wykonaj operację mnożenia.
print("ZAD1:")
macierz1 = np.array([1, 2, 3])
macierz2 = np.array([4, 5, 6])
print(macierz1)
print(macierz2)
wynik = np.dot(macierz1, macierz2)
print(wynik)

#ZAD2  Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.
print("ZAD2:")
macierz1 = np.array([[4, 2, 5], [1, 6, 3], [8, 7, 9]])
print(macierz1)
print(np.min(macierz1, axis=0))
print(np.min(macierz1, axis=1))

macierz2 = np.array([[9, 8, 7, 6], [5, 4, 3, 2], [1, 0, -1, -2], [-3, -4, -5, -6]])
print(macierz2)

print(np.min(macierz2, axis=0))
print(np.min(macierz2, axis=1))

#ZAD3  Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.
print("ZAD3:")
macierz1 = np.array([1, 2, 3])
macierz2 = np.array([4, 5, 6]).reshape((3,1))
print(macierz1)
print(macierz2)
wynik = np.dot(macierz1, macierz2)
print(wynik)

#ZAD4   Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.
print("ZAD4:")
macierz1 = np.array([1, 2, 3], dtype=int)
macierz2 = np.array([4.5, 5.5, 6.5])
print(macierz1)
print(macierz2)
wynik = np.dot(macierz1, macierz2)
print(wynik)

#ZAD5  Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”.
print("ZAD5:")
macierz = np.array([[1, 2, 3], [4, 5, 6]])
a = np.sin(macierz)
print(a)

#ZAD6  Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.
print("ZAD6:")
macierz = np.array([[2, 4, 6], [8, 10, 12]])
b = np.cos(macierz)
print(b)

#ZAD7  Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.
print("ZAD7:")
a = np.array([[0.84147098, 0.90929743, 0.14112001], [-0.7568025, -0.95892427, -0.2794155]])
b = np.array([[-0.41614684, -0.65364362, 0.96017029], [-0.14550003, -0.83907153, 0.84385396]])
c = a + b
print(c)

#ZAD8  Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.
print("ZAD8:")
macierz = np.random.rand(3, 3)
for row in macierz:
    print(row)

#ZAD9  Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia” macierzy. (użyj funkcji flat())
print("ZAD9:")
macierz = np.random.rand(3, 3)
for element in macierz.flat:
    print(element)

#ZAD10   Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?
print("ZAD10:")
macierz = np.random.rand(9, 9)
macierz_3x27 = macierz.reshape(3, 27)
print(macierz_3x27)
macierz_27x3 = macierz.reshape(27, 3)
print(macierz_27x3)
macierz_1x81 = macierz.reshape(1, 81)
print(macierz_1x81)

#ZAD11  Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?
print("ZAD11:")
vector = np.arange(12)
print(vector)
macierz_3x4 = vector.reshape(3, 4)
print(macierz_3x4)
macierz_4x3 = vector.reshape(4, 3)
print(macierz_4x3)
macierz_2x6 = vector.reshape(2, 6)
print(macierz_2x6)
print(macierz_3x4.flatten())
print(macierz_4x3.flatten())
print(macierz_2x6.flatten())