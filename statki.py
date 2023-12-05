import os
import time
def wait():
    time.sleep(0.5)
    os.system('clear')
def menu(w_menu,spoj,spoj2,zm,ust,limit,stat,stat2):
    print(f"{biały}===============================================================")
    print(f"|                         {pogrubienie}GRA w STATKI{biały}                        |")
    print("|                                                /|           |")
    print(f"| {podkreślenie}Wybierz opcje:{biały}                                / |           |")
    print("|    - Gra jednoosobowa  (wciśnij 1)           /  |           |")
    print("|    - Gra dwuosobowa   (wciśnij 2)           /_ _|           |")
    print("|    - Ustawienia       (wciśnij 3)        _ _ _ _|_ _ _      |")
    print("|                                          \ _ _ _ _ _ /      |")
    print("| v.0.1.2                                                     |")
    print("===============================================================")

    w_menu=int(input("Tutaj wpisz liczbę: "))
    if w_menu==1:
        wait()
        print(f"{niebieski}Gra jednoosobowa jest obecnie niedostępna{biały}")
        menu(w_menu,spoj,spoj2,zm,ust,limit,stat,stat2)
    elif w_menu==2:
        wait()
        ukladanie1(statek,spoj,k_litery,l_set,n_set,kol,cnt)
        ukladanie2(statek,spoj2,k_litery,l_set,n_set,kol,cnt)
        gra(stat,stat2,n_set,l_set,k_litery,kol,statek,t_woda,spoj)
        # print(f"{niebieski}Gra dwuosobowa jest obecnie niedostępna{biały}")
        # menu(w_menu)
    elif w_menu==3:
        ust=100
        while ust!=0:    
            wait()
            print(f"{biały}===============================================================")
            print("|                          USTAWIENIA                         |")
            print("|                                                /|           |")
            if spoj>9:
                print(f"|  {pogrubienie}1 - Liczba statków w grze:{biały} {spoj}                / |           |")
            else:
                print(f"|  {pogrubienie}1 - Liczba statków w grze:{biały} {spoj}                 / |           |")
            if limit==f"{czerwony}wył.{biały}":
                print(f"|  {pogrubienie}2 - Limit trwania ruchu:{biały} {limit}               /  |           |")
            else:
                if limit>9 and limit<100:
                    print(f"|  {pogrubienie}2 - Limit trwania ruchu:{biały} {limit}s                /  |           |")
                elif limit>99:
                    print(f"|  {pogrubienie}2 - Limit trwania ruchu:{biały} {limit}s               /  |           |")
                else:
                    print(f"|  {pogrubienie}2 - Limit trwania ruchu:{biały} {limit}s                  /  |           |")
            print("|                                             /_ _|           |")
            print("|                                          _ _ _ _|_ _ _      |")
            print("|   0 - Powrót do ekr. startowego          \ _ _ _ _ _ /      |")
            print("|                                                             |")
            print("===============================================================")
            ust=int(input("Wpisz cyrfę: "))
            if ust==1:
                zm=int
                zm=10
                while zm!=0:
                    wait()
                    print(f"{biały}===============================================================")
                    print("|                         STATKI w GRZE                       |")
                    print("|                                                /|           |")
                    if spoj>9:
                        print(f"|  {pogrubienie}Aktualna liczba statków w grze:{biały} {spoj}           / |           |")
                    else:
                        print(f"|  {pogrubienie}Aktualna liczba statków w grze:{biały} {spoj}            / |           |") 
                    print("|    | Aby zmienić wciśnij 1                   /  |           |")
                    print("|                                             /_ _|           |")
                    print("|                                          _ _ _ _|_ _ _      |")
                    print("|   0 - Powrót do ustawień                 \ _ _ _ _ _ /      |")
                    print("|                                                             |")
                    print("===============================================================")
                    zm=int(input("Tutaj wpisz cyrfę: "))
                    if zm==1:
                        spoj=int(input("Podaj nową liczbę statków w grze: "))
                        while spoj>20:
                            wait()
                            print(f"{czerwony}Liczba statków nie może przekraczać 20!{biały}")
                            time.sleep(2)
                            spoj=int(input("Podaj nową liczbę statków: "))
                        while spoj<4:
                            wait()
                            print(f"{czerwony}Liczba statków nie może być mniejsza niż 4!{biały}")
                            time.sleep(2)
                            spoj=int(input("Podaj nową liczbę statków: "))
                        wait()
                        print(f"{zielony}Nowa liczba statków ustawiona pomyślnie!{biały}")
                        spoj2=spoj
                        stat=spoj
                        stat2=spoj2
                        time.sleep(1)
                    elif zm!=0:
                        wait()
                        print(f"{czerwony}Podano nieprawidłową cyfrę!{biały}")
                        time.sleep(1)
            elif ust==2:
                zm=10
                while zm!=0:
                    wait()
                    print(f"{biały}===============================================================")
                    print("|                    LIMIT TRWANIA RUCHU                      |")
                    print("|                                                /|           |")
                    if limit==f"{czerwony}wył.{biały}":
                        print(f"|  {pogrubienie}Aktualny limit trwania ruchu:{biały} {limit}           / |           |")
                    else:
                        if limit>9 and limit<100:
                            print(f"|  {pogrubienie}Aktualny limit trwania ruchu:{biały} {limit}s            / |           |")
                        elif limit>99:
                            print(f"|  {pogrubienie}Aktualny limit trwania ruchu:{biały} {limit}s           / |           |")    
                        else:
                            print(f"|  {pogrubienie}Aktualny limit trwania ruchu:{biały} {limit}s             / |           |")
                    print("|    | Aby zmienić/włączyć wciśnij 1           /  |           |")
                    if limit==f"{czerwony}wył.{biały}":
                        print("|                                             /_ _|           |")
                    else:
                        print("|    | Aby wyłączyć wciśnij 2                 /_ _|           |")
                    print("|                                          _ _ _ _|_ _ _      |")
                    print("|   0 - Powrót do ustawień                 \ _ _ _ _ _ /      |")
                    print("|                                                             |")
                    print("===============================================================")
                    zm=int(input("Tutaj wpisz cyfrę: "))
                    if zm==1:
                        limit=int
                        limit=int(input("Podaj nowy limit trwania ruchu (w sekundach): "))
                        while limit>120:
                            wait()
                            print(f"{czerwony}Limit trwania ruchu nie może przekraczać 120 sekund!{biały}")
                            time.sleep(2)
                            limit=int(input("Podaj nowy limit trwania ruchu (w sekundach): "))
                        while limit<10:
                            wait()
                            print(f"{czerwony}Limit trwania ruchu nie może być mniejszy niż 10 sekund!{biały}")
                            time.sleep(2)
                            limit=int(input("Podaj nowy limit trwania ruchu (w sekundach): "))
                        wait()
                        print(f"{zielony}Nowy limit trwannia ruchu ustawiony pomyślnie!{biały}")
                        time.sleep(1)
                    elif zm==2:
                        limit=str
                        limit=f"{czerwony}wył.{biały}"    
                    elif zm!=0:
                        wait()
                        print(f"{czerwony}Podano nieprawidłową cyfrę!{biały}")
                        time.sleep(1)
                        
            elif ust==0:
                wait()
                menu(w_menu,spoj,spoj2,zm,ust,limit,stat,stat2)
            else:
                print(f"{czerwony}Podano nieprawidłową liczbę!{biały}")
                     
        # print(f"{niebieski}Ustawienia są obecnie niedostępne{biały}")
        # menu(w_menu)
    else:
        wait()
        print(f"{czerwony}Podano nieprawdiłową liczbę{biały}")
        menu(w_menu,spoj,spoj2,zm,ust,limit,stat,stat2) 
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
def gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10):
    print(*litery, sep='  ')
    print(*gprow1)
    print(*gprow2)
    print(*gprow3)
    print(*gprow4)
    print(*gprow5)
    print(*gprow6)
    print(*gprow7)
    print(*gprow8)
    print(*gprow9)
    print(*gprow10)
def plansza2(litery,sprow1,sprow2,sprow3,sprow4,sprow5,sprow6,sprow7,sprow8,sprow9,sprow10):
    print(*litery, sep='  ')
    print(*sprow1)
    print(*sprow2)
    print(*sprow3)
    print(*sprow4)
    print(*sprow5)
    print(*sprow6)
    print(*sprow7)
    print(*sprow8)
    print(*sprow9)
    print(*sprow10)
def gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10):
    print(*litery, sep='  ')
    print(*gsprow1)
    print(*gsprow2)
    print(*gsprow3)
    print(*gsprow4)
    print(*gsprow5)
    print(*gsprow6)
    print(*gsprow7)
    print(*gsprow8)
    print(*gsprow9)
    print(*gsprow10)
def ukladanie1(statek,spoj,k_litery,l_set,n_set,kol,cnt):
    wait()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("|                                       |")
    print(f"|          {pogrubienie}UKŁADANIE STATKÓW{biały}            |")
    print(f"|               {niebieski}Gracz 1{biały}                 |")
    print("|                                       |")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    time.sleep(3)
    while spoj>0:
        wait()
        plansza1(litery,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10)
        print(f"Pozostało jeszcze: {spoj} statków pojdynczych")
        l_set=str(input("Podaj literę kolumny: "))
        l_set = l_set.upper()
        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
            print(f"{czerwony}Podałeś złą literę!{biały}")
            time.sleep(1)
            plansza1(litery,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10)
            l_set=str(input("Podaj nową literę kolumny: "))
            l_set=l_set.upper()
        n_set=int(input("Podaj numer wiersza: "))
        while n_set<0 or n_set>10:
            print(f"{czerwony}Podałeś zły numer!{biały}")
            time.sleep(1)
            plansza1(litery,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10)
            n_set=int(input("Podaj nowy numer wiersza: "))
        kol=k_litery[l_set]
        kol=kol+1
        a=int
        
        if n_set==1:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if prow1[a]==statek or prow2[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj=spoj+1
                    break
                elif a==kol+1:
                    prow1[kol]=statek
        elif n_set==2:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if prow1[a]==statek or prow2[a]==statek or prow3[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj=spoj+1
                    break
                elif a==kol+1:
                    prow2[kol]=statek
        elif n_set==3:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if prow2[a]==statek or prow3[a]==statek or prow4[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj=spoj+1
                    break
                elif a==kol+1:
                    prow3[kol]=statek
        elif n_set==4:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if prow3[a]==statek or prow4[a]==statek or prow5[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj=spoj+1
                    break
                elif a==kol+1:
                    prow4[kol]=statek          
        elif n_set==5:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if prow4[a]==statek or prow5[a]==statek or prow6[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj=spoj+1
                    break
                elif a==kol+1:
                    prow5[kol]=statek 
        elif n_set==6:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if prow5[a]==statek or prow6[a]==statek or prow7[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj=spoj+1
                    break
                elif a==kol+1:
                    prow6[kol]=statek
        elif n_set==7:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if prow6[a]==statek or prow7[a]==statek or prow8[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj=spoj+1
                    break
                elif a==kol+1:
                    prow7[kol]=statek
        elif n_set==8:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if prow7[a]==statek or prow8[a]==statek or prow9[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj=spoj+1
                    break
                elif a==kol+1:
                    prow8[kol]=statek
        elif n_set==9:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if prow8[a]==statek or prow9[a]==statek or prow10[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj=spoj+1
                    break
                elif a==kol+1:
                    prow9[kol]=statek
        else:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if prow9[a]==statek or prow10[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj=spoj+1
                    break
                elif a==kol+1:
                    prow10[kol]=statek
        spoj=spoj-1
    wait()
    print(f"{zielony}Oto twoja plansza: {biały}")
    plansza1(litery,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10)
    cnt=str(input(f"Jeśli chcesz przejść do układania statków przez 2 gracza wciśnij enter"))    
def ukladanie2(statek,spoj2,k_litery,l_set,n_set,kol,cnt):
    wait()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("|                                       |")
    print(f"|          {pogrubienie}UKŁADANIE STATKÓW{biały}            |")
    print(f"|               {niebieski}Gracz 2{biały}                 |")
    print("|                                       |")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    time.sleep(3)
    while spoj2>0:
        wait()
        plansza2(litery,sprow1,sprow2,sprow3,sprow4,sprow5,sprow6,sprow7,sprow8,sprow9,sprow10)
        print(f"Pozostało jeszcze: {spoj2} statków pojdynczych")
        l_set=str(input("Podaj literę kolumny: "))
        l_set = l_set.upper()
        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
            print(f"{czerwony}Podałeś złą literę!{biały}")
            time.sleep(1)
            plansza2(litery,sprow1,sprow2,sprow3,sprow4,sprow5,sprow6,sprow7,sprow8,sprow9,sprow10)
            l_set=str(input("Podaj nową literę kolumny: "))
            l_set=l_set.upper()
        n_set=int(input("Podaj numer wiersza: "))
        while n_set<0 or n_set>10:
            print(f"{czerwony}Podałeś zły numer!{biały}")
            time.sleep(1)
            plansza2(litery,sprow1,sprow2,sprow3,sprow4,sprow5,sprow6,sprow7,sprow8,sprow9,sprow10)
            n_set=int(input("Podaj nowy numer wiersza: "))
        kol=k_litery[l_set]
        kol=kol+1
        a=int
        
        if n_set==1:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if sprow1[a]==statek or sprow2[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj2=spoj2+1
                    break
                elif a==kol+1:
                    sprow1[kol]=statek
        elif n_set==2:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if sprow1[a]==statek or sprow2[a]==statek or sprow3[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj2=spoj2+1
                    break
                elif a==kol+1:
                    sprow2[kol]=statek
        elif n_set==3:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if sprow2[a]==statek or sprow3[a]==statek or sprow4[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj2=spoj2+1
                    break
                elif a==kol+1:
                    sprow3[kol]=statek
        elif n_set==4:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if sprow3[a]==statek or sprow4[a]==statek or sprow5[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj2=spoj2+1
                    break
                elif a==kol+1:
                    sprow4[kol]=statek          
        elif n_set==5:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if sprow4[a]==statek or sprow5[a]==statek or sprow6[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj2=spoj2+1
                    break
                elif a==kol+1:
                    sprow5[kol]=statek 
        elif n_set==6:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if sprow5[a]==statek or sprow6[a]==statek or sprow7[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj2=spoj2+1
                    break
                elif a==kol+1:
                    sprow6[kol]=statek
        elif n_set==7:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if sprow6[a]==statek or sprow7[a]==statek or sprow8[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj2=spoj2+1
                    break
                elif a==kol+1:
                    sprow7[kol]=statek
        elif n_set==8:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if sprow7[a]==statek or sprow8[a]==statek or sprow9[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj2=spoj2+1
                    break
                elif a==kol+1:
                    sprow8[kol]=statek
        elif n_set==9:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if sprow8[a]==statek or sprow9[a]==statek or sprow10[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj2=spoj2+1
                    break
                elif a==kol+1:
                    sprow9[kol]=statek
        else:
            a=kol-2
            for x in range (0,3):
                a=a+1 
                if sprow9[a]==statek or sprow10[a]==statek:
                    print(f"{czerwony}W tym miejscu nie możesz postawić statku!{biały}")
                    time.sleep(2)
                    spoj2=spoj2+1
                    break
                elif a==kol+1:
                    sprow10[kol]=statek
        spoj2=spoj2-1
    wait()
    print(f"{zielony}Oto twoja plansza: {biały}")
    plansza2(litery,sprow1,sprow2,sprow3,sprow4,sprow5,sprow6,sprow7,sprow8,sprow9,sprow10)
    cnt=str(input(f"Jeśli chcesz przejść do gry wciśnij enter"))
def gra(stat,stat2,n_set,l_set,k_litery,kol,statek,t_woda,spoj):
    while stat!=0 or stat2!=0:
        wait()
        print("=================")
        print("  RUCH GRACZA 1  ")
        print("=================")
        time.sleep(1)
        wait()
        gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
        l_set=str(input("Podaj literę kolumny, na którą chcesz zrzucić bombę: "))
        l_set = l_set.upper()
        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
            print(f"{czerwony}Podałeś złą literę!{biały}")
            time.sleep(1)
            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
            l_set=l_set.upper()
        n_set=int(input("Podaj numer wiersza, na który chcesz zrzucić bombę: "))
        while n_set<0 or n_set>10:
            print(f"{czerwony}Podałeś zły numer!{biały}")
            time.sleep(1)
            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
        kol=k_litery[l_set]
        kol=kol+1
        a=int
        a=1
        if n_set==1:
                while a!=0: 
                    if gsprow1[kol]==t_woda or gsprow1[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow1[kol]==statek:
                            gsprow1[kol]=t_statek
                            wait()
                            if (sprow1[kol-1]==statek and gsprow1[kol-1]!=t_statek) or (sprow1[kol+1]==statek and gsprow1[kol+1]!=t_statek) or (sprow2[kol]==statek and gsprow2[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                # e=kol-1
                                # while sprow1[e]!=woda:
                                #     e=e-1
                                # gsprow1[e]=t_woda
                                # e=kol+1
                                # while sprow1[e]!=woda:
                                #     e=e+1
                                # gsprow1[e]=t_woda
                                # if gsprow1[kol-1]==t_woda and gsprow1[kol+1]==t_woda:
                                #     e=2
                                #     if sprow2[kol]==statek:
                                #         gsprow2[kol-1]=t_woda
                                #         gsprow2[kol+1]=t_woda
                                #         e=3
                                #     if sprow3[kol]==statek:
                                #         gsprow3[kol-1]=t_woda
                                #         gsprow3[kol+1]=t_woda
                                #         e=4
                                #     if sprow4[kol]==statek:
                                #         gsprow4[kol-1]=t_woda
                                #         gsprow4[kol+1]=t_woda
                                #         e=5
                                #     if sprow5[kol]==statek:
                                #         gsprow5[kol-1]=t_woda
                                #         gsprow5[kol+1]=t_woda
                                #         e=6
                                #     if e==2:
                                #        gsprow2[kol]=t_woda
                                #        gsprow2[kol-1]=t_woda
                                #        gsprow2[kol+1]=t_woda
                                #     elif e==3:
                                #         gsprow3[kol]=t_woda
                                #         gsprow3[kol-1]=t_woda
                                #         gsprow3[kol+1]=t_woda
                                #     elif e==4:
                                #         gsprow4[kol]=t_woda
                                #         gsprow4[kol-1]=t_woda
                                #         gsprow4[kol+1]=t_woda
                                #     elif e==4:
                                #         gsprow4[kol]=t_woda
                                #         gsprow4[kol-1]=t_woda
                                #         gsprow4[kol+1]=t_woda
                            time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow1[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
        elif n_set==2:
            while a!=0: 
                    if gsprow2[kol]==t_woda or gsprow2[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow2[kol]==statek:
                            gsprow2[kol]=t_statek
                            wait()
                            if (sprow2[kol-1]==statek and gsprow2[kol-1]!=t_statek) or (sprow2[kol+1]==statek and gsprow2[kol+1]!=t_statek) or (sprow3[kol]==statek and gsprow3[kol]!=t_statek) or (sprow1[kol]==statek and gsprow1[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow2[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
        elif n_set==3:
            while a!=0: 
                    if gsprow3[kol]==t_woda or gsprow3[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow3[kol]==statek:
                            gsprow3[kol]=t_statek
                            wait()
                            if (sprow3[kol-1]==statek and gsprow3[kol-1]!=t_statek) or (sprow3[kol+1]==statek and gsprow3[kol+1]!=t_statek) or (sprow4[kol]==statek and gsprow4[kol]!=t_statek) or (sprow2[kol]==statek and gsprow2[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow3[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
        elif n_set==4:
            while a!=0: 
                    if gsprow4[kol]==t_woda or gsprow4[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow4[kol]==statek:
                            gsprow4[kol]=t_statek
                            wait()
                            if (sprow4[kol-1]==statek and gsprow4[kol-1]!=t_statek) or (sprow4[kol+1]==statek and gsprow4[kol+1]!=t_statek) or (sprow5[kol]==statek and gsprow5[kol]!=t_statek) or (sprow3[kol]==statek and gsprow3[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow4[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0         
        elif n_set==5:
            while a!=0: 
                    if gsprow5[kol]==t_woda or gsprow5[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow5[kol]==statek:
                            gsprow5[kol]=t_statek
                            wait()
                            if (sprow5[kol-1]==statek and gsprow5[kol-1]!=t_statek) or (sprow5[kol+1]==statek and gsprow5[kol+1]!=t_statek) or (sprow6[kol]==statek and gsprow6[kol]!=t_statek) or (sprow4[kol]==statek and gsprow4[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow5[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
        elif n_set==6:
            while a!=0: 
                    if gsprow6[kol]==t_woda or gsprow6[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow6[kol]==statek:
                            gsprow6[kol]=t_statek
                            wait()
                            if (sprow6[kol-1]==statek and gsprow6[kol-1]!=t_statek) or (sprow6[kol+1]==statek and gsprow6[kol+1]!=t_statek) or (sprow7[kol]==statek and gsprow7[kol]!=t_statek) or (sprow5[kol]==statek and gsprow5[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow5[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
        elif n_set==7:
            while a!=0: 
                    if gsprow7[kol]==t_woda or gsprow7[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow7[kol]==statek:
                            gsprow7[kol]=t_statek
                            wait()
                            if (sprow7[kol-1]==statek and gsprow7[kol-1]!=t_statek) or (sprow7[kol+1]==statek and gsprow7[kol+1]!=t_statek) or (sprow8[kol]==statek and gsprow8[kol]!=t_statek) or (sprow6[kol]==statek and gsprow6[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow7[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
        elif n_set==8:
            while a!=0: 
                    if gsprow8[kol]==t_woda or gsprow8[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow8[kol]==statek:
                            gsprow8[kol]=t_statek
                            wait()
                            if (sprow8[kol-1]==statek and gsprow8[kol-1]!=t_statek) or (sprow8[kol+1]==statek and gsprow8[kol+1]!=t_statek) or (sprow9[kol]==statek and gsprow9[kol]!=t_statek) or (sprow7[kol]==statek and gsprow7[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow8[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
        elif n_set==9:
            while a!=0: 
                    if gsprow9[kol]==t_woda or gsprow9[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow9[kol]==statek:
                            gsprow9[kol]=t_statek
                            wait()
                            if (sprow9[kol-1]==statek and gsprow9[kol-1]!=t_statek) or (sprow9[kol+1]==statek and gsprow9[kol+1]!=t_statek) or (sprow10[kol]==statek and gsprow10[kol]!=t_statek) or (sprow8[kol]==statek and gsprow8[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow9[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
        else:
            while a!=0: 
                    if gsprow10[kol]==t_woda or gsprow10[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow10[kol]==statek:
                            gsprow10[kol]=t_statek
                            wait()
                            if (sprow10[kol-1]==statek and gsprow10[kol-1]!=t_statek) or (sprow10[kol+1]==statek and gsprow10[kol+1]!=t_statek) or (sprow9[kol]==statek and gsprow9[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow10[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
                            time.sleep(2)
                            a=0
        wait()
        print("=================")
        print(f"{niebieski}  RUCH GRACZA 2  {biały}")
        print("=================")
        time.sleep(1)
        wait()
        gplansza2(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10)
        l_set=str(input("Podaj literę kolumny, na którą chcesz zrzucić bombę: "))
        l_set = l_set.upper()
        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
            print(f"{czerwony}Podałeś złą literę!{biały}")
            time.sleep(1)
            gplansza1(litery,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10)
            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
            l_set=l_set.upper()
        n_set=int(input("Podaj numer wiersza, na który chcesz zrzucić bombę: "))
        while n_set<0 or n_set>10:
            print(f"{czerwony}Podałeś zły numer!{biały}")
            time.sleep(1)
            plansza1(litery,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10)
            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
        kol=k_litery[l_set]
        kol=kol+1
        a=int
        a=1
        if n_set==1:
                while a!=0: 
                    if gsprow1[kol]==t_woda or gsprow1[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow1[kol]==statek:
                            gsprow1[kol]=t_statek
                            wait()
                            if (sprow1[kol-1]==statek and gsprow1[kol-1]!=t_statek) or (sprow1[kol+1]==statek and gsprow1[kol+1]!=t_statek) or (sprow2[kol]==statek and gsprow2[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                # e=kol-1
                                # while sprow1[e]!=woda:
                                #     e=e-1
                                # gsprow1[e]=t_woda
                                # e=kol+1
                                # while sprow1[e]!=woda:
                                #     e=e+1
                                # gsprow1[e]=t_woda
                                # if gsprow1[kol-1]==t_woda and gsprow1[kol+1]==t_woda:
                                #     e=2
                                #     if sprow2[kol]==statek:
                                #         gsprow2[kol-1]=t_woda
                                #         gsprow2[kol+1]=t_woda
                                #         e=3
                                #     if sprow3[kol]==statek:
                                #         gsprow3[kol-1]=t_woda
                                #         gsprow3[kol+1]=t_woda
                                #         e=4
                                #     if sprow4[kol]==statek:
                                #         gsprow4[kol-1]=t_woda
                                #         gsprow4[kol+1]=t_woda
                                #         e=5
                                #     if sprow5[kol]==statek:
                                #         gsprow5[kol-1]=t_woda
                                #         gsprow5[kol+1]=t_woda
                                #         e=6
                                #     if e==2:
                                #        gsprow2[kol]=t_woda
                                #        gsprow2[kol-1]=t_woda
                                #        gsprow2[kol+1]=t_woda
                                #     elif e==3:
                                #         gsprow3[kol]=t_woda
                                #         gsprow3[kol-1]=t_woda
                                #         gsprow3[kol+1]=t_woda
                                #     elif e==4:
                                #         gsprow4[kol]=t_woda
                                #         gsprow4[kol-1]=t_woda
                                #         gsprow4[kol+1]=t_woda
                                #     elif e==4:
                                #         gsprow4[kol]=t_woda
                                #         gsprow4[kol-1]=t_woda
                                #         gsprow4[kol+1]=t_woda
                            time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow1[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
        elif n_set==2:
            while a!=0: 
                    if gsprow2[kol]==t_woda or gsprow2[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow2[kol]==statek:
                            gsprow2[kol]=t_statek
                            wait()
                            if (sprow2[kol-1]==statek and gsprow2[kol-1]!=t_statek) or (sprow2[kol+1]==statek and gsprow2[kol+1]!=t_statek) or (sprow3[kol]==statek and gsprow3[kol]!=t_statek) or (sprow1[kol]==statek and gsprow1[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow2[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
        elif n_set==3:
            while a!=0: 
                    if gsprow3[kol]==t_woda or gsprow3[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow3[kol]==statek:
                            gsprow3[kol]=t_statek
                            wait()
                            if (sprow3[kol-1]==statek and gsprow3[kol-1]!=t_statek) or (sprow3[kol+1]==statek and gsprow3[kol+1]!=t_statek) or (sprow4[kol]==statek and gsprow4[kol]!=t_statek) or (sprow2[kol]==statek and gsprow2[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow3[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
        elif n_set==4:
            while a!=0: 
                    if gsprow4[kol]==t_woda or gsprow4[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow4[kol]==statek:
                            gsprow4[kol]=t_statek
                            wait()
                            if (sprow4[kol-1]==statek and gsprow4[kol-1]!=t_statek) or (sprow4[kol+1]==statek and gsprow4[kol+1]!=t_statek) or (sprow5[kol]==statek and gsprow5[kol]!=t_statek) or (sprow3[kol]==statek and gsprow3[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow4[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0         
        elif n_set==5:
            while a!=0: 
                    if gsprow5[kol]==t_woda or gsprow5[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow5[kol]==statek:
                            gsprow5[kol]=t_statek
                            wait()
                            if (sprow5[kol-1]==statek and gsprow5[kol-1]!=t_statek) or (sprow5[kol+1]==statek and gsprow5[kol+1]!=t_statek) or (sprow6[kol]==statek and gsprow6[kol]!=t_statek) or (sprow4[kol]==statek and gsprow4[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow5[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
        elif n_set==6:
            while a!=0: 
                    if gsprow6[kol]==t_woda or gsprow6[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow6[kol]==statek:
                            gsprow6[kol]=t_statek
                            wait()
                            if (sprow6[kol-1]==statek and gsprow6[kol-1]!=t_statek) or (sprow6[kol+1]==statek and gsprow6[kol+1]!=t_statek) or (sprow7[kol]==statek and gsprow7[kol]!=t_statek) or (sprow5[kol]==statek and gsprow5[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow5[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
        elif n_set==7:
            while a!=0: 
                    if gsprow7[kol]==t_woda or gsprow7[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if sprow7[kol]==statek:
                            gsprow7[kol]=t_statek
                            wait()
                            if (sprow7[kol-1]==statek and gsprow7[kol-1]!=t_statek) or (sprow7[kol+1]==statek and gsprow7[kol+1]!=t_statek) or (sprow8[kol]==statek and gsprow8[kol]!=t_statek) or (sprow6[kol]==statek and gsprow6[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gsprow7[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
        elif n_set==8:
            while a!=0: 
                    if gprow8[kol]==t_woda or gprow8[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if prow8[kol]==statek:
                            gprow8[kol]=t_statek
                            wait()
                            if (prow8[kol-1]==statek and gprow8[kol-1]!=t_statek) or (prow8[kol+1]==statek and gprow8[kol+1]!=t_statek) or (prow9[kol]==statek and gprow9[kol]!=t_statek) or (prow7[kol]==statek and gprow7[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gprow8[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
        elif n_set==9:
            while a!=0: 
                    if gprow9[kol]==t_woda or gprow9[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if prow9[kol]==statek:
                            gprow9[kol]=t_statek
                            wait()
                            if (prow9[kol-1]==statek and gprow9[kol-1]!=t_statek) or (prow9[kol+1]==statek and gprow9[kol+1]!=t_statek) or (prow10[kol]==statek and gprow10[kol]!=t_statek) or (prow8[kol]==statek and gprow8[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gprow9[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
        else:
            while a!=0: 
                    if gprow10[kol]==t_woda or gprow10[kol]==t_statek:
                        print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                        time.sleep(2)
                        wait()
                        gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                        l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                        l_set = l_set.upper()
                        while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                            wait()
                            print(f"{czerwony}Podałeś złą literę!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                            l_set=l_set.upper()
                        n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                        while n_set<0 or n_set>10:
                            wait()
                            print(f"{czerwony}Podałeś zły numer!{biały}")
                            time.sleep(1)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                        kol=k_litery[l_set]
                        kol=kol+1
                    else:
                        if prow10[kol]==statek:
                            gprow10[kol]=t_statek
                            wait()
                            if (prow10[kol-1]==statek and gprow10[kol-1]!=t_statek) or (prow10[kol+1]==statek and gprow10[kol+1]!=t_statek) or (prow9[kol]==statek and gprow9[kol]!=t_statek):
                                print(f"{zielony}Trafiony!{biały}")
                            else:
                                print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                                stat2=stat2-1
                                time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0
                        else:
                            gprow10[kol]=t_woda
                            wait()
                            print(f"{niebieski}Pudło!{biały}")
                            time.sleep(2)
                            gplansza1(litery,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10)
                            time.sleep(2)
                            a=0


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
prow1=[1,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
prow2=[2,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
prow3=[3,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
prow4=[4,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
prow5=[5,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
prow6=[6,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
prow7=[7,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
prow8=[8,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
prow9=[9,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
prow10=[10,'','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']

gprow1=[1,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gprow2=[2,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gprow3=[3,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gprow4=[4,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gprow5=[5,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gprow6=[6,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gprow7=[7,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gprow8=[8,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gprow9=[9,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gprow10=[10,'','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']

sprow1=[1,' ','□ ','□ ','■ ','■ ','□ ','□ ','□ ','□ ','□ ','□ ','']
sprow2=[2,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
sprow3=[3,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
sprow4=[4,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
sprow5=[5,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
sprow6=[6,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
sprow7=[7,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
sprow8=[8,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
sprow9=[9,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
sprow10=[10,'','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']

gsprow1=[1,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gsprow2=[2,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gsprow3=[3,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gsprow4=[4,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gsprow5=[5,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gsprow6=[6,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gsprow7=[7,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gsprow8=[8,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gsprow9=[9,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
gsprow10=[10,'','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']


w_menu = int
l_set = str
n_set = int
kol = int
cnt=str

spoj=1
spoj2=spoj
stat=spoj
stat2=spoj2
zm=int
ust=int
limit=30
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
menu(w_menu,spoj,spoj2,zm,ust,limit,stat,stat2)

