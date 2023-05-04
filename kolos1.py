#Zestaw A

#Zadanie 1
import math
x = pow(math.log(math.sin(24)+math.pi), 1/3)
x_rounded = round(x, 2)
print("Wyrazenie ma wartosc: ", x_rounded)

#Zadanie 2
numbers = [2, 3.4, -9, 411, -64, 7, -6.78]
odd_numbers = [number for number in numbers if number % 2 == 1]
print("Pierwsza lista: ", numbers)
print("Lista liczb nieparzystuych: ", odd_numbers)

#Zadanie 3
def add_next(list):
    result = [list[i] + list[i+1] for i in range(len(list) - 1)]
    result.append(list[len(list) - 1] + list[0])
    return result

numbers2 = [5, 7.4, -5.9, -23, 6, 66, -1]
sums_of_pairs = add_next(numbers2)
print("Lista sum par liczb: ", sums_of_pairs)

#Zadanie 4
with open("tekst.txt", "r", encoding="utf-8") as file1:
    file1.seek(62)
    text = file1.read(29)

print(text)
text = text.upper()
print(text)

#Zadanie 5
try:
    n = int(input("Podaj dodatnia liczbe calkowita n: "))
    sum = 0
    for i in range(1, n + 1):
        sum += 5 * (i + 2) - 4
    with open("Suma ciagu.txt", "w") as file2:
        file2.write("Suma {} wyrazow ciagu 5(n+2)-4 wynosi {}".format(n, sum))
except ValueError:
    print("Blad! Podana wartosc nie jest dodatnia liczba calkowita.")
