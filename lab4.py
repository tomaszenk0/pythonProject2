#Zad 1

plik=open("lab4.txt","a")

lista=[]

for i in range (0,31):
    lista+=[i]

for i in lista:
    lista[i]*=2

plik.writelines(str(lista))

plik.close()
#Zad 2

plik=open("lab4.py","r")


linia=plik.readlines()

plik.close()

print(linia)

#Zad.4


class NaZakupy:
    nazwa_produktu=''
    ilosc=''
    jednostka_miary=''
    cena_jed='zl'
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka = jednostka_miary
        self.cena = cena_jed

    def wyswietl_produkt(self):
        return nazwa+' '+ilosc+' '+jednostka+' '+cena+' zl'

    def ile_produktow(self):
        return ilosc+' '+jednostka
    def ile_kosztuje(self):
        wynik=int(ilosc) * int(cena)
        return str(wynik)


nazwa=input("Podaj nazwe produktu: ")
ilosc=input("Podaj ilosc: ")
jednostka=input("Podaj jednostkę miary:")
cena=input("Podaj cenę jednostkową: ")

nowy=NaZakupy(nazwa_produktu=str(nazwa),ilosc=int(ilosc),jednostka_miary=str(jednostka),cena_jed=int(cena))

print(nowy.wyswietl_produkt())

print("Ilosc Produktow: "+nowy.ile_produktow())

print("Koszt: "+nowy.ile_kosztuje()+" zl")
#Zad.5


 class CiagiArytmetyczne:
    lista1=[]
    lista2=[]

     def wyswietl_dane(self):
         return

    def pobierz_elementy(self,lista1):
         elementy=input("Podaj liczby ciagu arytmetycznego: ")
         lista1+=[elementy]

     def pobierz_parametry(self):
         pierwsza=input("Podaj pierwszą watrość: ")
         roznica=input("Podaj różnicę: ")
        ilosc=input("Podaj ilość elementów ciągu: ")

        for i in ilosc:


