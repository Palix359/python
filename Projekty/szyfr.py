alfabet={
        "A": 1,"Ą": 2,"B": 3,"C": 4,"Ć": 5,"D":6,"E":7,"Ę":8,"F":9,"G":10,
        "H":11,"I":12,"J":13,"K":14,"L":15,"Ł":16,"M":17,"N":18,"Ń":19,"O":20,"Ó":21,
        "P":22,"R":23,"S":24,"Ś":25,"T":26,"U":27,"W":28,"Y":29,"Z":30,"Ź":31,"Ż":32
    }
alfabet1=["A","Ą","B","C","Ć","D","E","Ę","F","G","H","I","J","K","L","Ł","M","N","Ń","O","Ó","P","R","S","Ś","T","U","W","Y","Z","Ź","Ż"]
print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
print("Witaj w programie szyfrującym wiadomości!")
print("Program szyfruje wiadomości przy pomocy szyfru cezara")
print("Wiadomości można szyfrować przy użyciu polskich znaków")
print("Nie wolno używać znaków specjalnych")
print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
print("Szyfr cezara polega na przypisaniu każdej literze tekstu\nliterę o pewną wartość przesuniętą od niej w alfabecie\ncyfry w wiadomościach będą pomijane\n ")
print("| Jeżeli chesz zaszyfrować wiadomośc - wprowadź 1\n| Jeżeli chesz odszyfrować wiadomość - wprowadź 2")
wybor=input("Twój wybór: ")
i = wybor.isnumeric()
while i==False:
    wybor=input("Nie wprowadzono cyfry, proszę wprowadź cyfrę jeszcze raz: ")
    i = wybor.isnumeric()
wybor=int(wybor)
while wybor!=1 and wybor!=2:
    wybor=input("Nie ma takiej opcji do wyboru, proszę wprowadź cyfrę jeszcze raz: ")
    i=wybor.isnumeric()
    while i==False:
        wybor=input("Nie wprowadzono cyfry, proszę wprowadź cyfrę jeszcze raz: ")
        i=wybor.isnumeric()
    wybor=wybor(int)
if wybor==1:
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    x=input("Podaj proszę wartość o jaką mają być przesunięte litery w szyfrze: ")
    i = x.isnumeric()
    while i==False:
        x=input("Podana wartość nie składa się tylko z cyrf, proszę podaj tę wartość jeszcze raz: ")
        i=x.isnumeric()
    x=int(x)
    wiadomosc=input("Podaj wiadomość do zaszyfrowania: ")
    szyfr=''
    for j in wiadomosc:
        j=j.upper()
        if j=="1"or j=="2"or j=="3"or j=="4"or j=="5" or j=="6" or j=="7" or j=="8" or j=="9"or j=="0":
            continue
        elif j==" ":
            szyfr=szyfr+' '
        else:
            lp=alfabet[j]+x-1
            if lp>31:
                lp=lp-32
            szyfr=szyfr+alfabet1[lp]
    print("Oto twoja zaszyfrowana wiadomość:",szyfr)
elif wybor==2:
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    szyfr=input("Wprowadź wiadomość do odszyfrowania: ")
    x=input("Jeżeli wiesz o ile zostały przesunięte litery w szyfrze, wprowadź tą wartość, jeżeli nie - wpisz 0: ")
    i=x.isnumeric()
    if i==False:
        x=input("Nie wprowadzono wartości zawieracjącej same cyfry, proszę wpisz tę wartość jeszcze raz: ")
        i=x.isnumeric()
    x=int(x)
    if x==0:
        for x in range(0,32):
            wiadomosc=''
            for j in szyfr:
                j=j.upper()
                if j=="1"or j=="2"or j=="3"or j=="4"or j=="5" or j=="6" or j=="7" or j=="8" or j=="9"or j=="0":
                    continue
                elif j==" ":
                    wiadomosc=wiadomosc+' '
                else:
                    lp=alfabet[j]-x-1
                    if lp<0:
                        lp=lp+32
                    wiadomosc=wiadomosc+alfabet1[lp]
            if x==0:
                print("Oto wszystkie możliwe sposoby odszyfrowania tej wiadomości:")
            else:
                print(f"{x}.| {wiadomosc} (przesunięcie o {x})")
    else:
        wiadomosc=''
        for j in szyfr:
            j=j.upper()
            if j=="1"or j=="2"or j=="3"or j=="4"or j=="5" or j=="6" or j=="7" or j=="8" or j=="9"or j=="0":
                continue
            elif j==" ":
                wiadomosc=wiadomosc+' '
            else:
                lp=alfabet[j]-x-1
                if lp<0:
                    lp=lp+32
                wiadomosc=wiadomosc+alfabet1[lp]
        print("Odszyfrowana wiadomość:",wiadomosc)

    