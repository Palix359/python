#Program: Weryfikacja numeru pesel
#Numer pesel sprawdzany jest na podstawie danych z: gov.pl/web/gov/czym-jest-numer-pesel
lista=[]
m={
    1:"Stycznia",
    2:"Lutego",
    3:"Marca",
    4:"Kwietnia",
    5:"Maja",
    6:"Czerwca",
    7:"Lipca",
    8:"Sierpnia",
    9:"Września",
    10:"Października",
    11:"Listopada",
    12:"Grudnia"
}
print("Witaj w programie weryfikującym numer pesel!")
i="TAK"
while i=="TAK":
    lista.clear()
    p=input("Proszę, podaj nr pesel do weryfikacji: ")
    while len(p)!=11:
        p=input("Podano pesel o nieprawdiłowej długości, proszę podaj jeszcze raz: ")
    t=1
    while t>0:
        t=0
        for x in p:
            if x!="0" and x!="1" and x!="2" and x!="3" and x!="4" and x!="5" and x!="6" and x!="7" and x!="8" and x!="9":
                p=input("W nr pesel nie zawierają się same liczby, podaj inny nr pesel: ")
                while len(p)!=11:
                    p=input("Podano pesel o nieprawdiłowej długości, proszę podaj jeszcze raz: ")
                t=1
                break
        
    for x in p:
        x=int(x)
        lista.append(x)
    a=lista[0]*1
    a=a%10
    b=lista[1]*3
    b=b%10
    c=lista[2]*7
    c=c%10
    d=lista[3]*9
    d=d%10
    e=lista[4]*1
    e=e%10
    f=lista[5]*3
    f=f%10
    g=lista[6]*7
    g=g%10
    h=lista[7]*9
    h=h%10
    i=lista[8]*1
    i=i%10
    j=lista[9]*3
    j=j%10
    suma=a+b+c+d+e+f+g+h+i+j
    suma=suma%10
    if lista[2]==8 or lista[2]==9: 
        stulecie=18
    elif lista[2]==0 or lista[2]==1:
        stulecie=19
    elif lista[2]==2 or lista[2]==3:
        stulecie=20
    elif lista[2]==4 or lista[2]==5:
        stulecie=21
    else:
        stulecie=22
    miesiac=lista[3]
    if lista[2]%2!=0:
        miesiac=miesiac+9
    if 10-suma!=lista[10]:
        print("Podany nr pesel jest niepoprawny")
    else:
        print("Podany nr pesel jest poprawny")
        if lista[9]%2==0:
            print(f"Podany nr pesel należy do kobiety, która urodziła się dnia {lista[4]}{lista[5]} {m[miesiac]} {stulecie}{lista[0]}{lista[1]}r. ")
        else:
            print(f"Podany nr pesel należy do mężczyzny, który urodził się dnia {lista[4]}{lista[5]} {m[miesiac]} {stulecie}{lista[0]}{lista[1]}r.")
    i=input('Jeżeli chcesz jeszcze raz użyć programu, wpisz "tak": ')
    i=i.upper()