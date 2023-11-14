import math

operacje=['+','-','*','/','**','%']
print("=-=-=-=-=-=-=-=-=-=-=-=")
print("Kalkulator matematyczny")
print("=-=-=-=-=-=-=-=-=-=-=-=")
a=int(input("Podaj proszę pierwszą liczbę: "))
print("=-=-=-=-=-=-=-=-=-=-=-=")
print("Dostępne działania: ",*operacje)
operacja=0
operacja=int(input("Wybierz działanie - wpisz numer od 1 do 6 wg kolejności wypisanych działań: "))
while operacja<1 or operacja>6:
    print("Podano nieprawidłową daną")
    operacja=int(input("Wybierz działanie jeszcze raz - wpisz numer od 1 do 6 wg kolejności wypisanych działań: "))
operacja=operacja-1
print("=-=-=-=-=-=-=-=-=-=-=-=")
b=int(input("Podaj 2 liczbę: "))
dzialanie=operacje[operacja]
print("=-=-=-=-=-=-=-=-=-=-=-=")
print("Twoje działanie: ",a,dzialanie,b)
pot=str(input("Czy potwierdzasz wykonanie operacji? (Wpisz drukowane litery: TAK/NIE): "))
while pot!='NIE'and pot!='TAK':
    print("Podano złe polecenie, spróbuj jeszcze raz")
    pot=str(input("Czy potwierdzasz wykonanie operacji? (Wpisz drukowane litery: TAK/NIE): "))
while pot=='NIE':
    print("Co chciałbyś zmienić?")
    print("Pierwszą liczbę - wpisz 1")
    print("Typ działania - wpisz 2")
    print("Drugą liczbę - wpisz 3")
    zm=int(input())
    while zm>3 or zm<1:
        zm=int(input("Podano złą liczbę, podaj liczbę z zakresu od 1 do 3"))
    if zm==1:
        a=int(input("Podaj nową pierwszą liczbę: "))
    elif zm==2:
        print("Dostępne działania: ",*operacje)
        operacja=int(input("Wybierz działanie - wpisz numer od 1 do 6 wg kolejności wypisanych działań: "))
        while operacja<1 or operacja>6:
            print("Podano złą liczbę")
            operacja=int(input("Wybierz działanie jeszcze raz - wpisz numer od 1 do 6 wg kolejności wypisanych działań: "))
        operacja=operacja-1
        dzialanie=operacje[operacja]
    else:
        b=int(input("Podaj drugą liczbę: "))
    print("Twoja nowa operacja: ",a,dzialanie,b)
    pot=str(input("Czy potwierdzasz wykonanie operacji? (Wpisz drukowane litery TAK/NIE): "))
    while pot!='NIE'and pot!='TAK':
        print("Podano złe polecenie, spróbuj jeszcze raz")
        pot=str(input("Czy potwierdzasz wykonanie operacji? (Wpisz drukowane litery: TAK/NIE): "))

if pot=='TAK':
    if dzialanie=='+':
        print("Suma wynosi: ", a+b)
    elif dzialanie=='-':
        print("Rónica wynosi: ", a-b)
    elif dzialanie=='*':
        print("Iloczyn wynosi: ", a*b)
    elif dzialanie=='/':
        if b==0:
            print("Dzielnikiem nie moe być liczba 0")
        else:  
            print("Iloraz wynosi: ", a/b)
    elif dzialanie=='**':
        print("Wynik potęgowania wynosi: ", math.pow(a, b))
    elif dzialanie=='%':
        if b==0:
            print("Dzielnikiem nie może być liczba 0")
        else:  
            print("Wynik dzielania modulo wynosi: ", a%b)


