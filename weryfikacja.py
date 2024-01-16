lista=[]
def l(o):
    o=o%10
print("Witaj w programie weryfikującym numer pesel!")
p=input("Proszę, podaj nr pesel do weryfikacji: ")
while len(p)!=11:
    p=input("Podano pesel o nieprawdiłowej długości, proszę podaj jeszcze raz: ")
t=0
while t==0:
    for x in p:
        if x!="0" and x!="1" and x!="2" and x!="3" and x!="4" and x!="5" and x!="6" and x!="7" and x!="8" and x!="9":
            p=input("W nr pesel nie zawierają się same liczby, podaj inny nr pesel: ")
            t=0
for x in p:
    x=int(x)
    lista.append(x)
a=lista[0]*1
l(a)
b=lista[1]*3
l(b)
c=lista[2]*7
l(c)
d=lista[3]*9
l(d)
e=lista[4]*1
l(e)
f=lista[5]*3
l(f)
g=lista[6]*7
l(g)
h=lista[7]*9
l(h)
i=lista[8]*1
l(i)
j=lista[9]*3
l(j)
suma=a+b+c+d+e+f+g+h+i+j
l(suma)
if 10-suma!=lista[10]:
    print("Podany nr pesel jest niepoprawny")
print("Podany nr pesel jest poprawny")
if lista[9]%2==0:
    print(f"Podany nr pesel należy do kobiety, która urodziła się ")
else:
    print(f"Podany nr pesel należy do mężczyzny, który urodził się ")
