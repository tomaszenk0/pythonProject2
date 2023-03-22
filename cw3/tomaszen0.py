#zadanie 1
import math

x='e^10'
print(x)
y=math.sqrt(math.log(5+math.sin(8)**2))
print(y)
z=3.55
q=4.80
print(abs(z))
print(abs(q))
#zadanie 2
IMIE='TOMASZ'
NAZWISKO='SZAFRANSKI'

print(IMIE.capitalize())
print(NAZWISKO.capitalize())
#zadanie 3
bicior='la , la, la, la, la, la'
print(bicior.count("la"))
#zadanie 4
imie=['t','o','m','a','s','z']
print(imie[0])
print(imie[5])


#zadanie 6
float_cyfra=float(3.5323)
print(float_cyfra)
string_wyraz="tekst"
szesnastka=hex(241)
print(szesnastka)


#zadanie 5
p=szesnastka.split("f")
print(p)
#zadanie 7
lista=['silownia','rower', 'plywanie']
lista.reverse()
lista.append("hokej")

print(lista)
#zadanie 8
skroty={
    "np":"na przyklad",
    "pl":"placek",
    "nd":"nie zdam"
}
print(skroty)
#zadanie 9
slownik={

    "a":"minecraft",
    "a":"cs",
    "a":"lol"
}
print(slownik.count("a"))

#zadanie 10
zdanie=input('daj mi zdanie: ')
zdanie.count("a")
print(zdanie)
#zadanie 11
a=2
b=3
c=4
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else :
    print(c)
#zadanie 12
liczby=[1,2.5,3,5,7]
for i in range(len(liczby)):
    liczby[i]=liczby[i]**2
    print(liczby)
    #zadanie 13
    lista=[]
    liczba=0
    i=0
    while i<10:
        liczba=int(input("daj liczbę:"))
        if liczba%2==0:
            lista.append(liczba)
            i+=1
            print(lista)
