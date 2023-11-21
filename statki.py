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

litery=['X ','A','B','C','D','E','F','G','H','I','J']
prow1=[1,'','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]',]
prow2=[2,'','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]',]
prow3=[3,'','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]',]
prow4=[4,'','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]',]
prow5=[5,'','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]',]
prow6=[6,'','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]',]
prow7=[7,'','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]',]
prow8=[8,'','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]',]
prow9=[9,'','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]',]
prow10=[10,'[]','[]','[]','[]','[]','[]','[]','[]','[]','[]',]

czerwony = "\033[1;31m"
biały = "\033[0m"
niebieski = "\033[94m"
zielony = "\033[92m"
podkreślenie = "\033[4m"
pogrubienie= "\033[1m"

w_menu = int
print(menu(w_menu))
# plansza1(litery,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10)
