print("Witaj w progranie konwertującym liczby dziesiętne na rzymskie!")
liczba_d=input("Proszę, podaj liczbę w systemie dziesiętnym którą chesz przekonwertować:")
a=liczba_d.isnumeric()
while a==False:
    liczba_d=input("Nie wprowadzono liczby, proszę wprowadź liczbę w sys. dziesiętnym jeszcze raz:")
    a=liczba_d.isnumeric()
liczba_d=int(liczba_d)
while liczba_d>3999:
    if liczba_d%100==0 and setki<5:
        setki=setki+1
    else:
        print("Liczby nie da się zapisać w systemie rzymskim, zachowując zasady pisowni liczb w tym systemie")
m=int(liczba_d/1000)
c=int(liczba_d/100)-m*10
x=int(liczba_d/10)-m*100-c*10
if liczba_d-m*1000>900:
    


