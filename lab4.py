#Zad 1

plik=open("lab4.txt","a")

lista=[]

for i in range (0,31):
    lista+=[i]

for i in lista:
    lista[i]*=2

plik.writelines(str(lista))

plik.close()