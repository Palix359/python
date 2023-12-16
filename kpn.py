import random
import os
os.system('cls')
print('Witaj w grze pt. "Kamień, papier, nożyce"!')
gracz=input("Podaj nazwę gracza: ")
print("Witaj,",gracz)
l=['kamień','papier','nożyce']
i=1
n=0
f=open("historia.txt","w",encoding="utf-8")
while i==1:
    n=n+1
    x=int(input("Wybierz swój ruch (kamień-1, papier-2, nożyce-3): "))
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
    else:
        f.write(f"| {n}. {gracz} 0:1 Komputer\n")
    i=int(input("Jeżeli chcesz zagrać jeszcze raz, wpisz 1, jeżeli nie, wpisz dowolną liczbę: "))
f.close()
f=open("historia.txt","r",encoding="utf-8")
os.system('cls')
print("=========================")
print("      GRA SKOŃCZONA      ")
print("=========================")
print("Twoje wyniki z",n,"gier:")
for line in f:
    print(line,end="")


    
