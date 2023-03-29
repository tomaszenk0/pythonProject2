#zadanie 1
a=int(input("podaj liczbę a: "))

b=int(input("podaj liczbę b:" ))
print(a * a + a * b + b * b)


#zadanie 2
lista1=[2,5,7,3,2,7]
lista2=[6,44,8,2,8]
lista3=[]
lista3.append(lista1[2]+lista2[3])
print(lista3)

#zadanie 3
tekst= open("tekst1.txt", "r+", encoding="utf-8 ")
    tekst=tekst.read()
    znaki=[]
    litery=[]
    for i in range(100, 135):
        znaki.append(tekst[i])
        if tekst[i].isupper():
        litery.append(tekst[i])
        try:
            a=sum(1 for i in znaki if i.supper())
            print(litery)
            print("litery:", a)
        except ValueError:
            if a==0:
                print("nie ma litter")

#zadanie 4
import math
lista=[2,5,7,2]
a=10
zadanie4=[lista[i] for i in range(len(lista)) if lista[i]>b]
print(zadanie4)

#zadanie 5
a=pow((2/7),3)
cos=pow(math.cos(39),2)
e=pow(math.e, 3)
b=pow((e+cos),(1/5))
wynik=a+b+math.pi
print(round(wynik, 2))


