#zadanie 1
import numpy as np
macierz1= np.array([1,2,3])
macierz2= np.array([1,1,7])
wynik=np.dot(macierz1, macierz2)
print(wynik)
#zadanie 2
macierza= np.array([[6,2,3],[1,7,2],[1,1,3]])
macierzb= np.array([[6,2,3],[1,7,2],[1,1,3], [9,2,6]])
rzedya=np.min(macierza, axis=1)
kolumnya=np.min(macierza, axis=0)
print(rzedya, kolumnya)

rzedyb=np.min(macierzb, axis=1)
kolumnyb=np.min(macierzb, axis=0)
print(rzedyb, kolumnyb)

#zadanie 3
wynik=np.dot(macierz1, macierz2)
print(wynik)

#zadanie 4
ma1= np.array([1,2,3],dtype=int)
ma2= np.array([1.2,1.6,7.9], dtype=float)
w=np.multiply(ma1, ma2)
print(w)

#zadanie 5
macierz= np.array([[6,2,3],[1,7,2]])
a=np.sin(macierz)
print(a)

#zadanie 6
m= np.array([[6,2,3],[1,7,2]])
b=np.cos(m)
print(b)

#zadanie 7
c=a+b
print(c)


#zadanie 8
macierza= np.array([[6,2,3],[1,7,2],[1,1,3]])
for rzedy in macierza:
    print(rzedy)

#zadanie 9
macierza= np.array([[6,2,3],[1,7,2],[1,1,3]])
for e in macierza.flat:
    print(e)

 #zadanie 10
g=np.arange(1, 82).reshape((9,9))
print(g)

f=g.reshape((3,27))
print(f)

 #zadanie 11
vektor=np.arange(12)
m34=vektor.reshape(3,4)
m43=vektor.reshape(4,3)
m26=vektor.reshape(2, 6)
print(m34.flatten())
print(m43.flatten())
print(m26.flatten())

print(m34.flatten())
print(m43.flatten())
print(m26.flatten())

