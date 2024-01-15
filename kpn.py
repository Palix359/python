import random
import os
os.system('clear')
print('Witaj w grze pt. "Kamień, papier, nożyce"!')
gracz=input("Podaj nazwę gracza: ")
print("Witaj,",gracz)
l=['kamień','papier','nożyce']
i=1
n=0
g1=0
gc=0
f=open("historia.txt","w",encoding="utf-8")
while i==1:
    n=n+1
    x=input("Wybierz swój ruch (kamień-1, papier-2, nożyce-3): ")
    while x!='1' and x!='2' and x!='3':
        x=input("Wprowadziłeś złą cyfrę, proszę wybierz jeszcze raz: ")
    x=int(x)
    x=x-1
    ruch=l[x]
    y=random.randrange(0,2)
    ruch_c=l[y]
    print(f"Twój wybór: {ruch}")
    print(f"Wybór przeciwnika: {ruch_c}")
    if x == 1:
        if y == 1:
            print('Wynik: remis')
            w=1
        elif y==2:
            print("Wynik: przegrana")
            w=0
        else:
            print("Wynik: wygrana")
            w=3
    elif x==2:
        if y==1:
            print("Wynik: wygrana")
            w=3
        elif y==2:
            print("Wynik: remis")
            w=1
        else:
            print("Wynik: przegrana")
            w=0
    else:
        if y==1:
            print("Wynik: przegrana")
            w=0
        elif y==2:
            print("Wynik: wygrana")
            w=3
        else:
            print("Wynik: remis")
            w=1
    if w==1:
        f.write(f"| {n}. {gracz} 1:1 Komputer\n")
    elif w==3:
        f.write(f"| {n}. {gracz} 1:0 Komputer\n")
        g1=g1+1
    else:
        f.write(f"| {n}. {gracz} 0:1 Komputer\n")
        gc=gc+1
    i=int(input("Jeżeli chcesz zagrać jeszcze raz, wpisz 1, jeżeli nie, wpisz dowolną liczbę: "))
f.close()
f=open("historia.txt","r",encoding="utf-8")
os.system('cls')
print("=========================")
print("      GRA SKOŃCZONA      ")
print("=========================")
if g1==1:
    print("Wygrałeś w 1 grze")
else:
    print("Wygrałeś w",g1,"grach")
if gc==1:
    print("Komputer wygrał w 1 grze")
else:
    print("Komputer wygrał w",gc,"grach")
if n-g1-gc==1:
    print("Był 1 remis")
else:
    print("Było",n-g1-gc,"remisów")
if n==1:
    print("Twoje wyniki z 1 gry:")
else:
    print("Twoje wyniki z",n,"gier:")
for line in f:
    print(line,end="")


    
