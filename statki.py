import os
import time
def wait():
    time.sleep(0.5)
    os.system('clear')
def menu(w_menu):
    print(f"{biały}===============================================================")
    print(f"|                         {pogrubienie}GRA w STATKI{biały}                        |")
    print("|                                                /|           |")
    print(f"| {podkreślenie}Wybierz opcje:{biały}                                / |           |")
    print("|    - Gra jednoosobowa  (wciśnij 1)           /  |           |")
    print("|    - Gra dwuosobowa   (wciśnij 2)           /_ _|           |")
    print("|    - Ustawienia       (wciśnij 3)        _ _ _ _|_ _ _      |")
    print("|                                          \ _ _ _ _ _ /      |")
    print("| v.0.1.1                                                     |")
    print("===============================================================")

    w_menu=int(input("Tutaj wpisz liczbę: "))
    if w_menu==1:
        wait()
        print(f"{niebieski}Gra jednoosobowa jest obecnie niedostępna{biały}")
        menu(w_menu)
    elif w_menu==2:
        wait()
        # print(f"{niebieski}Gra dwuosobowa jest obecnie niedostępna{biały}")
        # menu(w_menu)
    elif w_menu==3:
        wait()
        print(f"{niebieski}Ustawienia są obecnie niedostępne{biały}")
        menu(w_menu)
    else:
        os.system('clear')
        print(f"{czerwony}Podano nieprawdiłową liczbę{biały}")
        menu(w_menu)
    
def plansza1(litery,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10):
    print(*litery, sep='  ')
    print(*prow1)
    print(*prow2)
    print(*prow3)
    print(*prow4)
    print(*prow5)
    print(*prow6)
    print(*prow7)
    print(*prow8)
    print(*prow9)
    print(*prow10)
def ukladanie1(statek,spoj,litery):
    for i in spoj:
        plansza1(litery,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10)
        print(f"Pozostało jeszcze: {spoj} statków pojdynczych")
        l_set=str(input("Podaj literę kolumny: "))
        n_set=int(input("Podaj numer wiersza: "))
        kol=k_litery[l_set]
        kol=kol+1
        if n_set==1:
            prow1[kol]=statek
        elif n_set==2:
            prow2[kol]=statek
        elif n_set==3:
            prow3[kol]=statek
        elif n_set==4:
            prow4[kol]=statek           
        elif n_set==5:
            prow5[kol]=statek
        elif n_set==6:
            prow6[kol]=statek
        elif n_set==7:
            prow7[kol]=statek
        elif n_set==8:
            prow8[kol]=statek
        elif n_set==9:
            prow9[kol]=statek
        else:
            prow10[kol]=statek
        plansza1(litery,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10)
        spoj=spoj-1


czerwony = "\033[1;31m"
biały = "\033[0m"
niebieski = "\033[94m"
zielony = "\033[92m"
podkreślenie = "\033[4m"
pogrubienie= "\033[1m"

statek='■ '
woda='□ '
t_statek='◆ '
t_woda='◇ '

litery=['  ','A','B','C','D','E','F','G','H','I','J']
prow1=[1,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ']
prow2=[2,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ']
prow3=[3,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ']
prow4=[4,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ']
prow5=[5,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ']
prow6=[6,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ']
prow7=[7,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ']
prow8=[8,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ']
prow9=[9,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ']
prow10=[10,'','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ']


w_menu = int
print(menu(w_menu))
spoj=9
k_litery={
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
    }

ukladanie1(statek,spoj,litery)
plansza1(litery,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10)
