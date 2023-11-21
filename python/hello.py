print("Hello  world") #komentarz

'''Komentarz
wielo
linijkowy'''

zmienna=10
rzeczywista=10.5

print(zmienna)
print('%.20f'%rzeczywista) #określanie ile miejsc po przecinku liczby ma być wypisane (w tym przypadku 20)

tekst1="hellow world"
tekst2='hello world'
tekst3="hello 'world'" # w "" na zapisaywać ' ' 
print(tekst3)
print("Wartość zmiennej 'zmienna' to: ", zmienna)
print(f"Wartść zmiennej 'zmienna' to: {zmienna}")
print("Wartość zmiennej 'zmienna' to: %.0f"%zmienna)
print("Wartość zmiennej 'zmienna' to: " + str(zmienna))

imie=input("Jak masz na imię?")
lata=int(input("Ile masz lat?")) #deklarowanie oczekiwanej zmiennej

print(f"Masz na imię {imie}")
print("masz",lata,"lat")

#importy bibliotek robi się na początku
import random
los=random.randint(1,20)
print(los)

import math
potega=math.pow(2, 8)
print(potega)

suma=2+2
roznica=4-2
iloczyn=4*2
iloraz=4/2
potega2=3**2
modulo=7%5


liczba=int(input("Proszę podać liczbę: "))

if liczba>0:
    print("Podana liczba jest większa od zera")
elif liczba<0:
    print("Liczba jest mniejsza od zera")
else:
    print("Liczba jest równa zero")

if liczba>0:
    print("Podana liczba jest większa od zera")
elif liczba==0:
    print("Liczba jest równa zero")
else:
    print("Liczba jest mniejsza od zero")

liczba1=int(input("Proszę podać liczbę: "))
if liczba1%2==0:
    print("Liczba jest podzielna przez dwa")
else:
    print("Liczba nie jest podzielna przez dwa")

print("Liczba jest podzielna przez dwa") if liczba%2==0 else print("Liczba nie jest podzielna przez dwa") #drugi sposób zapisu if

for i in range(3):
    print("Numer: ", i) #python liczy pętle od 0 (w tym przypadku od 0 do 2)


for i in range(3):
    print("Numer: ", i+1) #teraz wypisujemy od 1 do 3

for i in range(1, 100): #nie jest uwzgęldniona 100 (przedział otwarty)
 if i%2==0:
     print(i)

for i in range(1, 101, 2):
    print(i)

for i in range(100, 0, -1):
    print(i)

for litera in "slowo":
    if litera=="o":
        break
    print(litera)

for litera in "slowo":
    if litera=="o":
        continue 
    print(litera)


while liczba<0:
    liczba=int(input("Podaj liczbę jeszcze raz"))


# while True:
#     print("Prawda")         Pętla nieskończona

def powitanie():
    print("Cześć")

powitanie()

def powiatnie_imienne(imie):
    print("Cześć,",imie)

powiatnie_imienne("Jacek")

def dzielenie(dzielna, dzielnik):
    if dzielnik==0:
        return "Nie dziel przez 0"
    else:
        return dzielna/dzielnik
    
print(dzielenie(5,2))
print(dzielenie(3,0))
iloraz=dzielenie(3,4)
print(iloraz)


lista=[1,2,3,9,6,8,7]
print(type(lista))

print(lista)
print(*lista)
print(*lista, sep=";")
lista.sort()
print(lista)
lista.reverse()  #lista.sort(reverse=True)
print(lista)     #print(lista)

print(lista.count(3))

lista.remove(3)
print(lista)

lista.append(1)
print(lista)

print(lista[0])
# print(lista[8])
print(len(lista))

lista[0]=1
print(lista)

for i in lista:
    print(i)

krotka=(1,2,3)
print(krotka)

tupla=1,2,3.5,"abc"
print(tupla)

krotka2=("abc",)      #krotka2=("abc",)                  
print(type(krotka2))  # print(type(krotka2))

print(len(krotka))
print(len(tupla))


kontakty={} #słownik
kontakty["Jan"] = 123456789
kontakty["Jacek"]=234567890
kontakty={
    "Jan": 123456789,
    "Jacek": 234567890,
    "Janusz": 987654321,
}

print(kontakty["Janusz"])

for imie, numer in kontakty.items():
    print("%s ma numer: %d" %(imie, numer)) #print("%s ma numer: %i" %(imie, numer))

print(kontakty.keys())
print(kontakty.values())

del kontakty["Jacek"]

print(kontakty.keys())

f=open("text.txt", "r")
print(f.read())

for i in f:
    print("Linijka: ", i)
f.close()

f=open("text.txt", "a")
f.write("eeeee\n")
f.close()