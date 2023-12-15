import random
import os
os.system('cls')
print('Witaj w grze pt. "Kamień, papier, nożyce"!')
print()
l=['kamień','papier','nożyce']
x=int(input("Wybierz swój ruch (kamień-1, papier-2, nożyce-3): "))
x=x-1
ruch=l[x]
y=random.randrange(0,2)
ruch_c=l[y]
print()
print(f"Twój wybór: {ruch}")
print(f"Wybór przeciwnika: {ruch_c}")
if x == 1:
    if y == 1:
        print('Wynik: remis')
    elif y==2:
        print("Wynik: przegrana")
    else:
        print("Wynik: wygrana")
elif x==2:
    if y==1:
        print("Wynik: wygrana")
    elif y==2:
        print("Wynik: remis")
    else:
        print("Wynik: przegrana")
else:
    if y==1:
        print("Wynik: przegrana")
    elif y==2:
        print("Wynik: wygrana")
    else:
        print("Wynik: remis")
