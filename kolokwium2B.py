import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Grupa B
# Zad 1
# Za pomocą bibliotek matplotlib utwórz wykres liniowy funkcji f(x)=(x2+3x)/5 + sin(x) dla
# wartości x z przedziału [-3,5], wartości x zmieniają się co 0.3.
# Dodaj odpowiednie etykiety do osi wykresu, tytuł linii, legendę oraz tytuł wykresu.
# Dodatkowo wyświetl oba wektory przekazywane na wykres.Ustaw zakres oś x na granice przedziału.

# liczby z przedziału od -3 do 5 co 0.3
x = np.arange(-3, 5, 0.3)
y = (x**2 + 3 * x) / 5 + np.sin(x)
# tworzenie wykresu: oś x, oś y, kolor i rodzaj linii
plt.plot(x, y, 'g-')
# ustawienie zakresu osi x
plt.xlim([-3, 5])
# etykiety osi wykresu
plt.xlabel('x')
plt.ylabel('y')
# tytuł linii i legenda
plt.legend(labels='f(x)')
# tytuł wykresu
plt.title('wykres liniowy')
# zapisanie wykresu do pliku o rozszerzeniu .png
plt.savefig('zad1')
# wyświetlenie wykresu
plt.show()

#wyświetlenie wektorów
print(x)
print(y)

# Zad 2
# Za pomocą matplotlib odwzoruj siatkę wykresów z poniższego zdjęcia. Siatkę zapisz do pliku(imie_nazwisko_zad2.png)

# siatka 3 wiersze, 1 kolumna, 1 miejsce
plt.subplot(3, 1, 1)
# liczby od -1 do 1, ilość liczb - 200
x1 = np.linspace(-1, 1, 200)
# liczby od -1 do 1 co 0.1 - wynik ten sam
# x1 = np.arange(-1, 1, 0.1)
y1_1 = np.cos(x1) * np.sin(x1)
y1_2 = np.cos(x1) - np.tan(x1)
# niebieski liniowy ('b-') z oznaczeniem legendy
plt.plot(x1, y1_1, 'b-', label='cos(x)*sin(x)')
# pomarańczowy (color='orange') liniowy (linestyle='-') z oznaczeniem legendy
# (jeśli punkty mają być widoczne (marker='o' między color i linestyle)
plt.plot(x1, y1_2, color='orange', linestyle='-', label='cos(x)-tan(x)')
plt.xlim([-1, 1])
plt.xlabel('x')
plt.ylabel('wyniki funkcji')
# legenda jeśli nie będzie oznaczeń w plt.plot
# plt.legend(labels=['cos(x)*sin(x)', 'cos(x)-tan(x)'])
plt.legend()
plt.title('Wykres dwóch funkcji')



# 3 miejsce w siatce - drugi wykres
plt.subplot(3, 1, 3)
x2 = np.linspace(1, 4, 4)
y2 = x2**2 / np.sqrt(x2)
# żółty punktowy, trójkąty ('y>')
plt.plot(x2, y2, 'y>', label='x^2/sqrt(x)')
plt.xlabel('x')
plt.ylabel('wyniki funkcji')
# lokalizacja górny lewy róg
plt.legend(loc='upper left')
plt.title('Wykres funkcji')


plt.savefig('zad2')
plt.show()

# Zad3
# Używając biblioteki pandas wczytaj zawartość pliku ‘glass.data’ do ramki danych i wykonaj następujące kroki:
# •Utwórz nową ramkędanych gdzie znajdą się te wiersze w których typ szkła równa się 6 lub 7
# •Na nowej ramce danych dokonaj grupowania danych po kolumnie Type of glass
# •Na wykresie kołowym przedstaw procentowy udział każdego z typów szkła.

# ramka (tabela) wczytana z pliku z pominięciem wiersza nagłówków (header=0), oddzieleniem pól tabeli jako przecinek
# i przecinek w liczbach zmiennoprzecinkowych jako kropka
df = pd.read_csv('glass.data', header=0, sep=',', decimal='.')
# utworzenie nowej ramki z 6 i 7 typu szkła (wszystkie były od 1 do 7)
df_new = df[(df['Type of glass'] > 5)]
# grupowanie danych po typie szkła zliczając ile jest danego typu
group = df_new.groupby('Type of glass')['Id number'].count()
# tworzenie wykresu kołowego (kind='pie'), jako udział procentowy z 2 miescami po przecinku(autopct=%.2f% %), ze zwiększoną czcionką
group.plot(kind='pie', autopct='%.2f%%', fontsize=20, colors=['red', 'green'])
plt.legend()
# ustawienie oznaczenia osi y na nniewidoczną
plt.ylabel('')
plt.title('Udział procentowy')
plt.savefig('zad3')
plt.show()

#Zad 4
# Za pomocą biblioteki pandaswczytaj zawartość pliku „glass.data”,następnie na wykresie słupkowym
# z biblioteki seaborn przedstaw ilość każdego z rodzajów szkła (type of glass).
# Na wykresie mają być podpisane etykiety dotyczące osi, legenda, tytuł wykresu. Ustaw styl wykresu na podstawowy.

df = pd.read_csv('glass.data', header=0, sep=',', decimal='.')
# tworzymy wykres słupkowy z ramki df, gdzie słupki ą różnymi typami szkłą (x='Type of glass'),
# zliczamy po Id (y='Id number i estimator=np.count_nonzero), kolorowanie różnych typów szkłą (hue='Type of glass'),
# ewentualny dokładny wybór kolorów, nie zawsze potrzebny (palette=[])
wykres = sns.barplot(data=df, x='Type of glass', y='Id number',
                   hue='Type of glass', estimator=np.count_nonzero, dodge=False)#, palette=['red', 'green', 'blue', ...])
plt.xlabel('Rodzaj szkła')
plt.ylabel('Ilość szkła')
plt.legend(title='Rodzaj szkła')
wykres.set(title='Wykres słupkowy')
plt.savefig('zad4')
plt.show()

