import os
import time
import random
def wait():
    time.sleep(0.5)
    os.system('cls')
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
def wplansza1(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10,komunikat,km1,m,stat2,ms):
    ms.pop(0)
    print("               TY                                           PRZECIWNIK            ")
    print(*litery,'             ',*litery,'    |','Ostatni ruch przeciwnika:',sep='  ')
    print(*prow1,'             ',*gsprow1,'   |',komunikat[km1],m)
    print(*prow2,'             ',*gsprow2,'   |',' Wcześniej, w tej samej kolejce:',*ms)
    print(*prow3,'             ',*gsprow3,'   |',' Ilość niezatopionych statków:',stat2)
    print(*prow4,'             ',*gsprow4,)
    print(*prow5,'             ',*gsprow5)
    print(*prow6,'             ',*gsprow6)
    print(*prow7,'             ',*gsprow7)
    print(*prow8,'             ',*gsprow8)
    print(*prow9,'             ',*gsprow9)
    print(*prow10,'            ',*gsprow10)
def wplansza2(litery,sprow1,sprow2,sprow3,sprow4,sprow5,sprow6,sprow7,sprow8,sprow9,sprow10,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10,komunikat,km2,m2,stat,ms2):
    ms2.pop(0)
    print("               TY                                                PRZECIWNIK            ")
    print(*litery,'                  ',*litery,'    |','Ostatni ruch przeciwnika:',sep='  ')
    print(*sprow1,'                  ',*gprow1,'   |',komunikat[km2],m2,)
    print(*sprow2,'                  ',*gprow2,'   |',"Wcześniej, w tej samej kolejce:",*ms2)
    print(*sprow3,'                  ',*gprow3,'   |','Ilość niezatopionych statków:',stat)
    print(*sprow4,'                  ',*gprow4)
    print(*sprow5,'                  ',*gprow5)
    print(*sprow6,'                  ',*gprow6)
    print(*sprow7,'                  ',*gprow7)
    print(*sprow8,'                  ',*gprow8)
    print(*sprow9,'                  ',*gprow9)
    print(*sprow10,'                  ',*gprow10)
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
            wait()
            print(f"{czerwony}Podałeś złą literę!{biały}")
            plansza1(litery,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10)
            l_set=str(input("Podaj nową literę kolumny: "))
            l_set=l_set.upper()
        n_set=int(input("Podaj numer wiersza: "))
        while n_set<1 or n_set>10:
            print(f"{czerwony}Podałeś zły numer!{biały}")
            wait()
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
        while n_set<1 or n_set>10:
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
class akcja():
    a=1
    kol=int
    row1_e = list
    row1_p = list
    row2_e = list
    row2_p = list
    row0_e = list
    row0_p = list
    stat_local = 0
    def zrzucanie_g1(self):
        while self.a!=0:
            wait()
            if self.row1_p[self.kol]==t_woda or self.row1_p[self.kol]==t_statek:
                print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                time.sleep(2)
                wait()
                wplansza1(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10,komunikat,km1,m,stat2,ms)
                l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                l_set = l_set.upper()
                while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                    wait()
                    print(f"{czerwony}Podałeś złą literę!{biały}")
                    time.sleep(1)
                    wplansza1(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10,komunikat,km1,m,stat2,ms)
                    l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                    l_set=l_set.upper()
                n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                while n_set<0 or n_set>10:
                    wait()
                    print(f"{czerwony}Podałeś zły numer!{biały}")
                    time.sleep(1)
                    wplansza1(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10,komunikat,km1,m,stat2,ms)
                    n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                self.kol=k_litery[l_set]
                self.kol=self.kol+1
            else:
                if self.row1_e[self.kol]==statek:
                    self.row1_p[self.kol]=t_statek
                    wait()
                    if (self.row1_e[self.kol-1]==statek and self.row1_p[self.kol-1]!=t_statek) or (self.row1_e[self.kol+1]==statek and self.row1_p[self.kol+1]!=t_statek) or (self.row2_e[self.kol]==statek and self.row2_p[self.kol]!=t_statek) or (self.row0_e[self.kol]==statek and self.row0_p[self.kol]!=t_statek):
                        print(f"{zielony}Trafiony!{biały}")
                        self.kom=1
                    else:
                        print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                        self.stat_local+=1
                        self.kom=2
                    self.row1_e[self.kol]=t_statek
                    time.sleep(2)
                    self.a=0
                else:
                    self.row1_p[self.kol]=t_woda
                    wait()
                    print(f"{niebieski}Pudło!{biały}")
                    self.kom=3
                    time.sleep(2)
                    self.row1_e[self.kol]=t_woda
                    self.a=0

    def zrzucanie_g2(self):
        while self.a!=0:
            wait()
            if self.row1_p[self.kol]==t_woda or self.row1_p[self.kol]==t_statek:
                print(f"{czerwony}W tym miejscu nie możesz zrzucić bomby!{biały}")
                time.sleep(2)
                wait()
                wplansza2(litery,sprow1,sprow2,sprow3,sprow4,sprow5,sprow6,sprow7,sprow8,sprow9,sprow10,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10,komunikat,km2,m2,stat,ms2)
                l_set=str(input("Podaj jeszcze raz literę kolumny, na którą chcesz zrzucić bombę: "))
                l_set = l_set.upper()
                while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                    wait()
                    print(f"{czerwony}Podałeś złą literę!{biały}")
                    time.sleep(1)
                    wplansza2(litery,sprow1,sprow2,sprow3,sprow4,sprow5,sprow6,sprow7,sprow8,sprow9,sprow10,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10,komunikat,km2,m2,stat2,ms2)
                    l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                    l_set=l_set.upper()
                n_set=int(input("Podaj jeszcze raz numer wiersza, na który chcesz zrzucić bombę: "))
                while n_set<0 or n_set>10:
                    wait()
                    print(f"{czerwony}Podałeś zły numer!{biały}")
                    time.sleep(1)
                    wplansza2(litery,sprow1,sprow2,sprow3,sprow4,sprow5,sprow6,sprow7,sprow8,sprow9,sprow10,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10,komunikat,km2,m2,stat2,ms2)
                    n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                self.kol=k_litery[l_set]
                self.kol=self.kol+1
            else:
                if self.row1_e[self.kol]==statek:
                    self.row1_p[self.kol]=t_statek
                    wait()
                    if (self.row1_e[self.kol-1]==statek and self.row1_p[self.kol-1]!=t_statek) or (self.row1_e[self.kol+1]==statek and self.row1_p[self.kol+1]!=t_statek) or (self.row2_e[self.kol]==statek and self.row2_p[self.kol]!=t_statek) or (self.row0_e[self.kol]==statek and self.row0_p[self.kol]!=t_statek):
                        print(f"{zielony}Trafiony!{biały}")
                        self.kom=1
                    else:
                        print(f"{zielony}{pogrubienie}Trafiony zatopiony!{biały}")
                        self.stat_local+=1
                        self.kom=2
                    self.row1_e[self.kol]=t_statek
                    time.sleep(2)
                    self.a=0
                else:
                    self.row1_p[self.kol]=t_woda
                    wait()
                    print(f"{niebieski}Pudło!{biały}")
                    self.kom=3
                    time.sleep(2)
                    self.row1_e[self.kol]=t_woda
                    self.a=0
    def zrzucanie_gc(self):
        while self.a!=0:
            if self.row1_p[self.kol]==t_woda or self.row1_p[self.kol]==t_statek:
                self.kol=random.randrange(1,10)
                n_set=random.randange(1,10)
            else:
                if self.row1_e[self.kol]==statek:
                    self.row1_p[self.kol]=t_statek
                    if (self.row1_e[self.kol-1]==statek and self.row1_p[self.kol-1]!=t_statek) or (self.row1_e[self.kol+1]==statek and self.row1_p[self.kol+1]!=t_statek) or (self.row2_e[self.kol]==statek and self.row2_p[self.kol]!=t_statek) or (self.row0_e[self.kol]==statek and self.row0_p[self.kol]!=t_statek):
                        print(f"{zielony}Trafiony!{biały}")
                    else:
                        self.stat_local+=1
                    self.row1_e[self.kol]=t_statek
                    self.a=0
                else:
                    self.row1_p[self.kol]=t_woda
                    self.row1_e[self.kol]=t_woda
                    self.a=0
                    i2=0


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
ms=['0']
ms2=['0']
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

sprow1=[1,' ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','□ ','']
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
kol = int
cnt=str

spoj=2
spoj2=spoj
stat=spoj
stat2=spoj2
a=int
zm=int
ust=int
m=0
limit=30
t=int
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
km1=4
km2=4
n_set=int 
l_set=str
m=''
m2=''

komunikat={
    1: f"{zielony}Przeciwnik trafił w twój statek na polu{biały}",
    2: f"{zielony}Przeciwnik zatopił twój statek na polu{biały}",
    3: f"{niebieski}Twój przeciwnik spudłował w pole{biały}",
    4: "",
}
loading=["Trwa układanie statków przez komputer."]
# print(f"{czerwony}                    UWAGA!                {biały}")
# print("   W programie aktualnie nie znajdują się    ")
# print("    zabezpieczenia przeciwko wprowadzeniu    ")
# print("   w miejsce zm. liczbowej danej tekstowej   ")
# print(f"{czerwony}Użytkowniku, uważaj przy wprowadzaniu danych!{biały}")
# print(" Program może się nieodwracalnie zatrzymać! ")
# print("--")
# r=input("Naciśnij dowolny klawisz aby kontynuować ")
w_menu=0
while w_menu==0:
    wait()
    print(f"{biały}===============================================================")
    print(f"|                         {pogrubienie}GRA w STATKI{biały}                        |")
    print("|                                                /|           |")
    print(f"| {podkreślenie}Wybierz opcje:{biały}                                / |           |")
    print("|    - Gra jednoosobowa  (wciśnij 1)           /  |           |")
    print("|    - Gra dwuosobowa   (wciśnij 2)           /_ _|           |")
    print("|    - Ustawienia       (wciśnij 3)        _ _ _ _|_ _ _      |")
    print("|                                          \ _ _ _ _ _ /      |")
    print("| v.0.2.3                                                     |")
    print("===============================================================")

    w_menu=int(input("Tutaj wpisz liczbę: "))
    if w_menu==1:
        wait()
        # print(f"{niebieski}Gra jednoosobowa jest obecnie niedostępna{biały}")
        # menu(w_menu,spoj,spoj2,zm,ust,limit,stat,stat2)
        ukladanie1(statek,spoj,k_litery,l_set,n_set,kol,cnt)
        wait()
        spoj=spoj2
        print(f"{niebieski}Trwa ustawianie statków przez komputer...{biały}")
        while spoj2!=0:
            n_set=random.randint(1,10)
            kol=random.randint(1,10)+1
            if n_set==1:
                a=kol-2
                for x in range (0,3):
                    a=a+1 
                    if sprow1[a]==statek or sprow2[a]==statek:
                        spoj2=spoj2+1
                        m=1
                    elif a==kol+1 and m!=1:
                        sprow1[kol]=statek
            elif n_set==2:
                a=kol-2
                for x in range (0,3):
                    a=a+1 
                    if sprow1[a]==statek or sprow2[a]==statek or sprow3[a]==statek:
                        spoj2=spoj2+1
                        m=1
                    elif a==kol+1 and m!=1:
                        sprow2[kol]=statek
            elif n_set==3:
                a=kol-2
                for x in range (0,3):
                    a=a+1 
                    if sprow2[a]==statek or sprow3[a]==statek or sprow4[a]==statek:
                        spoj2=spoj2+1
                        m=1
                    elif a==kol+1 and m!=1:
                        sprow3[kol]=statek
            elif n_set==4:
                a=kol-2
                for x in range (0,3):
                    a=a+1 
                    if sprow3[a]==statek or sprow4[a]==statek or sprow5[a]==statek:
                        spoj2=spoj2+1
                        m=1
                    elif a==kol+1 and m!=1:
                        sprow4[kol]=statek          
            elif n_set==5:
                a=kol-2
                for x in range (0,3):
                    a=a+1 
                    if sprow4[a]==statek or sprow5[a]==statek or sprow6[a]==statek:
                        spoj2=spoj2+1
                        m=1
                    elif a==kol+1 and m!=1:
                        sprow5[kol]=statek 
            elif n_set==6:
                a=kol-2
                for x in range (0,3):
                    a=a+1 
                    if sprow5[a]==statek or sprow6[a]==statek or sprow7[a]==statek:
                        spoj2=spoj2+1
                        m=1
                    elif a==kol+1 and m!=1:
                        sprow6[kol]=statek
            elif n_set==7:
                a=kol-2
                for x in range (0,3):
                    a=a+1 
                    if sprow6[a]==statek or sprow7[a]==statek or sprow8[a]==statek:
                        spoj2=spoj2+1
                        m=1
                    elif a==kol+1 and m!=1:
                        sprow7[kol]=statek
            elif n_set==8:
                a=kol-2
                for x in range (0,3):
                    a=a+1 
                    if sprow7[a]==statek or sprow8[a]==statek or sprow9[a]==statek:
                        spoj2=spoj2+1
                        m=1
                    elif a==kol+1 and m!=1:
                        sprow8[kol]=statek
            elif n_set==9:
                a=kol-2
                for x in range (0,3):
                    a=a+1 
                    if sprow8[a]==statek or sprow9[a]==statek or sprow10[a]==statek:
                        spoj2=spoj2+1
                        m=1
                    elif a==kol+1 and m!=1:
                        sprow9[kol]=statek
            else:
                a=kol-2
                for x in range (0,3):
                    a=a+1 
                    if sprow9[a]==statek or sprow10[a]==statek:
                        spoj2=spoj2+1
                        m=1
                    elif a==kol+1 and m!=1:
                        sprow10[kol]=statek   
            spoj2=spoj2-1
            m=0
        time.sleep(2)
        print(f"{zielony}Statki zostały ułożone!{biały}")
        time.sleep(2)
        spoj2=spoj
        wait()
        start=time.time()
        while stat!=0 and stat2!=0:
            i1=1
            i2=1
            while i1!=0 and stat2!=0: #Powtarzanie ruchu po trafieniu nie działa gdy długość statków jest większa od 1
                wait()
                print("=================")
                print(f"  {niebieski}RUCH GRACZA 1{biały}  ")
                print("=================")
                time.sleep(1)
                wait()
                wplansza1(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10)
                l_set=str(input("Podaj literę kolumny, na którą chcesz zrzucić bombę: "))
                l_set = l_set.upper()
                while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                    wait()
                    print(f"{czerwony}Podałeś złą literę!{biały}")
                    time.sleep(1)
                    wplansza1(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10)
                    l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                    l_set=l_set.upper()
                n_set=int(input("Podaj numer wiersza, na który chcesz zrzucić bombę: "))
                while n_set<0 or n_set>10:
                    wait()
                    print(f"{czerwony}Podałeś zły numer!{biały}")
                    time.sleep(1)
                    wplansza1(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10)
                    n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                kol=k_litery[l_set]
                kol=kol+1 
                row1=akcja()
                row1.kol=k_litery[l_set]+1
                row1.row1_p=gsprow1
                row1.row1_e=sprow1
                row1.row0_p=litery
                row1.row0_e=litery
                row1.row2_p=gsprow2
                row1.row2_e=sprow2
                row2=akcja()
                row2.kol=k_litery[l_set]+1
                row2.row1_p=gsprow2
                row2.row1_e=sprow2
                row2.row0_p=gsprow1
                row2.row0_e=sprow1
                row2.row2_p=gsprow3
                row2.row2_e=sprow3
                row3=akcja()
                row3.kol=k_litery[l_set]+1
                row3.row1_p=gsprow3
                row3.row1_e=sprow3
                row3.row0_p=gsprow2
                row3.row0_e=sprow2
                row3.row2_p=gsprow4
                row3.row2_e=sprow4
                row4=akcja()
                row4.kol=k_litery[l_set]+1
                row4.row1_p=gsprow4
                row4.row1_e=sprow4
                row4.row0_p=gsprow3
                row4.row0_e=sprow3
                row4.row2_p=gsprow5
                row4.row2_e=sprow5
                row5=akcja()
                row5.kol=k_litery[l_set]+1
                row5.row1_p=gsprow5
                row5.row1_e=sprow5
                row5.row0_p=gsprow4
                row5.row0_e=sprow4
                row5.row2_p=gsprow6
                row5.row2_e=sprow6
                row6=akcja()
                row6.kol=k_litery[l_set]+1
                row6.row1_p=gsprow6
                row6.row1_e=sprow6
                row6.row0_p=gsprow5
                row6.row0_e=sprow5
                row6.row2_p=gsprow7
                row6.row2_e=sprow7
                row7=akcja()
                row7.kol=k_litery[l_set]+1
                row7.row1_p=gsprow7
                row7.row1_e=sprow7
                row7.row0_p=gsprow6
                row7.row0_e=sprow6
                row7.row2_p=gsprow8
                row7.row2_e=sprow8
                row8=akcja()
                row8.kol=k_litery[l_set]+1
                row8.row1_p=gsprow8
                row8.row1_e=sprow8
                row8.row0_p=gsprow7
                row8.row0_e=sprow7
                row8.row2_p=gsprow9
                row8.row2_e=sprow9
                row9=akcja()
                row9.kol=k_litery[l_set]+1
                row9.row1_p=gsprow9
                row9.row1_e=sprow9
                row9.row0_p=gsprow8
                row9.row0_e=sprow8
                row9.row2_p=gsprow10
                row9.row2_e=sprow10
                row10=akcja()
                row10.kol=k_litery[l_set]+1
                row10.row1_p=gsprow10
                row10.row1_e=sprow10
                row10.row0_p=gsprow9
                row10.row0_e=sprow9
                row10.row2_p=litery
                row10.row2_e=litery
                if n_set==1:
                    row1.zrzucanie_g1()
                    stat2=stat2-row1.stat_local
                    i1=row1.stat_local
                    row1.stat_local=0
                elif n_set==2:
                    row2.zrzucanie_g1()
                    stat2=stat2-row2.stat_local
                    i1=row2.stat_local
                    row2.stat_local=0
                elif n_set==3:
                    row3.zrzucanie_g1()
                    stat2=stat2-row3.stat_local
                    i1=row3.stat_local
                    row3.stat_local=0
                elif n_set==4:
                    row4.zrzucanie_g1()
                    stat2=stat2-row4.stat_local
                    i1=row4.stat_local
                    row4.stat_local=0        
                elif n_set==5:
                    row5.zrzucanie_g1()
                    stat2=stat2-row5.stat_local
                    i1=row5.stat_local
                    row5.stat_local=0
                elif n_set==6:
                    row6.zrzucanie_g1()
                    stat2=stat2-row6.stat_local
                    i1=row6.stat_local
                    row6.stat_local=0
                elif n_set==7:
                    row7.zrzucanie_g1()
                    stat2=stat2-row7.stat_local
                    i1=row7.stat_local
                    row7.stat_local=0
                elif n_set==8:
                    row8.zrzucanie_g1()
                    stat2=stat2-row8.stat_local
                    i1=row8.stat_local
                    row8.stat_local=0
                elif n_set==9:
                    row9.zrzucanie_g1()
                    stat2=stat2-row9.stat_local
                    i1=row9.stat_local
                    row9.stat_local=0
                else:
                    row10.zrzucanie_g1()
                    stat2=stat2-row10.stat_local
                    i1=row10.stat_local
                    row10.stat_local=0
            while i2!=0 and stat!=0:
                wait()
                print("=================")
                print(f"{niebieski} RUCH KOMPUTERA {biały}")
                print("=================")
                time.sleep(1)
                kol=random.randint(1,10)
                n_set=random.randint(1,10)
                kol=kol+1
                row1.kol=k_litery[l_set]+1
                row1.row1_p=gprow1
                row1.row1_e=prow1
                row1.row0_p=litery
                row1.row0_e=litery
                row1.row2_p=gprow2
                row1.row2_e=prow2
                row2.kol=k_litery[l_set]+1
                row2.row1_p=gprow2
                row2.row1_e=prow2
                row2.row0_p=gprow1
                row2.row0_e=prow1
                row2.row2_p=gprow3
                row2.row2_e=prow3
                row3.kol=k_litery[l_set]+1
                row3.row1_p=gprow3
                row3.row1_e=prow3
                row3.row0_p=gprow2
                row3.row0_e=prow2
                row3.row2_p=gprow4
                row3.row2_e=prow4
                row4.kol=k_litery[l_set]+1
                row4.row1_p=gprow4
                row4.row1_e=prow4
                row4.row0_p=gprow3
                row4.row0_e=prow3
                row4.row2_p=gprow5
                row4.row2_e=prow5
                row5.kol=k_litery[l_set]+1
                row5.row1_p=gprow5
                row5.row1_e=prow5
                row5.row0_p=gprow4
                row5.row0_e=prow4
                row5.row2_p=gprow6
                row5.row2_e=prow6
                row6.kol=k_litery[l_set]+1
                row6.row1_p=gprow6
                row6.row1_e=prow6
                row6.row0_p=gprow5
                row6.row0_e=prow5
                row6.row2_p=gprow7
                row6.row2_e=prow7
                row7.kol=k_litery[l_set]+1
                row7.row1_p=gprow7
                row7.row1_e=prow7
                row7.row0_p=gprow6
                row7.row0_e=prow6
                row7.row2_p=gprow8
                row7.row2_e=prow8
                row8.kol=k_litery[l_set]+1
                row8.row1_p=gprow8
                row8.row1_e=prow8
                row8.row0_p=gprow7
                row8.row0_e=prow7
                row8.row2_p=gprow9
                row8.row2_e=prow9
                row9.kol=k_litery[l_set]+1
                row9.row1_p=gprow9
                row9.row1_e=prow9
                row9.row0_p=gprow8
                row9.row0_e=prow8
                row9.row2_p=gsprow10
                row9.row2_e=prow10
                row10.kol=k_litery[l_set]+1
                row10.row1_p=gprow10
                row10.row1_e=prow10
                row10.row0_p=gprow9
                row10.row0_e=prow9
                row10.row2_p=litery
                row10.row2_e=litery
                if n_set==1:
                    row1.zrzucanie_gc()
                    stat=stat-row1.stat_local
                    i2=row1.stat_local
                    row1.stat_local=0
                elif n_set==2:
                    row2.zrzucanie_gc()
                    stat=stat-row2.stat_local
                    i2=row2.stat_local
                    row2.stat_local=0
                elif n_set==3:
                    row3.zrzucanie_gc()
                    stat=stat-row3.stat_local
                    i2=row3.stat_local
                    row3.stat_local=0
                elif n_set==4:
                    row4.zrzucanie_gc()
                    stat=stat-row4.stat_local
                    i2=row4.stat_local
                    row4.stat_local=0        
                elif n_set==5:
                    row5.zrzucanie_gc()
                    stat=stat-row5.stat_local
                    i2=row5.stat_local
                    row5.stat_local=0
                elif n_set==6:
                    row6.zrzucanie_gc()
                    stat=stat-row6.stat_local
                    i2=row6.stat_local
                    row6.stat_local=0
                elif n_set==7:
                    row7.zrzucanie_gc()
                    stat=stat-row7.stat_local
                    i2=row7.stat_local
                    row7.stat_local=0
                elif n_set==8:
                    row8.zrzucanie_gc()
                    stat=stat-row8.stat_local
                    i2=row8.stat_local
                    row8.stat_local=0
                elif n_set==9:
                    row9.zrzucanie_gc()
                    stat=stat-row9.stat_local
                    i2=row9.stat_local
                    row9.stat_local=0
                else:
                    row10.zrzucanie_gc()
                    stat=stat-row10.stat_local
                    i2=row10.stat_local
                    row10.stat_local=0
        end=time.time()
        czas=int(end-start)
        minuta=0
        while czas>=60:
            minuta=minuta+1
            czas=czas-60
        if stat==0:
            winner="komputer"
        else:
            winner="gracz 1"
        wait()
        print("======================================================")
        print(f"|                {zielony}GRA SKOŃCZONA!{biały}                      |")
        print(f"| Zwycięzca: {winner}                                 |")
        if minuta>9 and czas>9:
            print(f"| Czas gry: {minuta}min {czas}s                                |")
        elif minuta>9 and czas<10:
            print(f"| Czas gry: {minuta}min {czas}s                                 |")
        else:
            print(f"| Czas gry: {minuta}min {czas}s                                  |")
        if winner=="gracz 2":
            print(f"| Niezatopione statki: {stat2}                             |")
        else:
            print(f"| Niezatopione statki: {stat}                             |")
        print("|                                                    |")
        # print("| Jeśli chcesz zagrać jeszcze raz, kliknij 1         |")
        print("======================================================")
        # g=int(input())
        # while g!=1:
        #     g=int(input())
        # w_menu=0
    elif w_menu==2:
        wait()
        ukladanie1(statek,spoj,k_litery,l_set,n_set,kol,cnt)
        ukladanie2(statek,spoj2,k_litery,l_set,n_set,kol,cnt)
        start=time.time()
        while stat!=0 and stat2!=0: #Sprawdzanie czy ktoś nie wygrał
            i1=1
            i2=1
            while i1!=0 and stat2!=0: #Powtarzanie ruchu po trafieniu nie działa gdy długość statków jest większa od 1
                wait()
                print("=================")
                print(f"  {niebieski}RUCH GRACZA 1{biały}  ")
                print("=================")
                time.sleep(1)
                wait()
                print(ms)
                wplansza1(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10,komunikat,km1,m,stat2,ms)
                l_set=str(input("Podaj literę kolumny, na którą chcesz zrzucić bombę: "))
                l_set = l_set.upper()
                while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                    wait()
                    print(f"{czerwony}Podałeś złą literę!{biały}")
                    time.sleep(1)
                    wplansza1(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10,komunikat,km1,m,stat2,ms)      
                    l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                    l_set=l_set.upper()
                n_set=int(input("Podaj numer wiersza, na który chcesz zrzucić bombę: "))
                while n_set<0 or n_set>10:
                    wait()
                    print(f"{czerwony}Podałeś zły numer!{biały}")
                    time.sleep(1)
                    wplansza1(litery,gsprow1,gsprow2,gsprow3,gsprow4,gsprow5,gsprow6,gsprow7,gsprow8,gsprow9,gsprow10,prow1,prow2,prow3,prow4,prow5,prow6,prow7,prow8,prow9,prow10,komunikat,km1,m,stat2,ms)
                    n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                kol=k_litery[l_set]
                kol=kol+1 
                row1=akcja()
                row1.kol=k_litery[l_set]+1
                row1.row1_p=gsprow1
                row1.row1_e=sprow1
                row1.row0_p=litery
                row1.row0_e=litery
                row1.row2_p=gsprow2
                row1.row2_e=sprow2
                row2=akcja()
                row2.kol=k_litery[l_set]+1
                row2.row1_p=gsprow2
                row2.row1_e=sprow2
                row2.row0_p=gsprow1
                row2.row0_e=sprow1
                row2.row2_p=gsprow3
                row2.row2_e=sprow3
                row3=akcja()
                row3.kol=k_litery[l_set]+1
                row3.row1_p=gsprow3
                row3.row1_e=sprow3
                row3.row0_p=gsprow2
                row3.row0_e=sprow2
                row3.row2_p=gsprow4
                row3.row2_e=sprow4
                row4=akcja()
                row4.kol=k_litery[l_set]+1
                row4.row1_p=gsprow4
                row4.row1_e=sprow4
                row4.row0_p=gsprow3
                row4.row0_e=sprow3
                row4.row2_p=gsprow5
                row4.row2_e=sprow5
                row5=akcja()
                row5.kol=k_litery[l_set]+1
                row5.row1_p=gsprow5
                row5.row1_e=sprow5
                row5.row0_p=gsprow4
                row5.row0_e=sprow4
                row5.row2_p=gsprow6
                row5.row2_e=sprow6
                row6=akcja()
                row6.kol=k_litery[l_set]+1
                row6.row1_p=gsprow6
                row6.row1_e=sprow6
                row6.row0_p=gsprow5
                row6.row0_e=sprow5
                row6.row2_p=gsprow7
                row6.row2_e=sprow7
                row7=akcja()
                row7.kol=k_litery[l_set]+1
                row7.row1_p=gsprow7
                row7.row1_e=sprow7
                row7.row0_p=gsprow6
                row7.row0_e=sprow6
                row7.row2_p=gsprow8
                row7.row2_e=sprow8
                row8=akcja()
                row8.kol=k_litery[l_set]+1
                row8.row1_p=gsprow8
                row8.row1_e=sprow8
                row8.row0_p=gsprow7
                row8.row0_e=sprow7
                row8.row2_p=gsprow9
                row8.row2_e=sprow9
                row9=akcja()
                row9.kol=k_litery[l_set]+1
                row9.row1_p=gsprow9
                row9.row1_e=sprow9
                row9.row0_p=gsprow8
                row9.row0_e=sprow8
                row9.row2_p=gsprow10
                row9.row2_e=sprow10
                row10=akcja()
                row10.kol=k_litery[l_set]+1
                row10.row1_p=gsprow10
                row10.row1_e=sprow10
                row10.row0_p=gsprow9
                row10.row0_e=sprow9
                row10.row2_p=litery
                row10.row2_e=litery
                if n_set==1:
                    row1.zrzucanie_g1()
                    stat2=stat2-row1.stat_local
                    i1=row1.stat_local
                    row1.stat_local=0
                    km2=row1.kom
                elif n_set==2:
                    row2.zrzucanie_g1()
                    stat2=stat2-row2.stat_local
                    i1=row2.stat_local
                    row2.stat_local=0
                    km2=row2.kom
                elif n_set==3:
                    row3.zrzucanie_g1()
                    stat2=stat2-row3.stat_local
                    i1=row3.stat_local
                    row3.stat_local=0
                    km2=row3.kom
                elif n_set==4:
                    row4.zrzucanie_g1()
                    stat2=stat2-row4.stat_local
                    i1=row4.stat_local
                    row4.stat_local=0
                    km2=row4.kom        
                elif n_set==5:
                    row5.zrzucanie_g1()
                    stat2=stat2-row5.stat_local
                    i1=row5.stat_local
                    row5.stat_local=0
                    km2=row5.kom
                elif n_set==6:
                    row6.zrzucanie_g1()
                    stat2=stat2-row6.stat_local
                    i1=row6.stat_local
                    row6.stat_local=0
                    km2=row6.kom
                elif n_set==7:
                    row7.zrzucanie_g1()
                    stat2=stat2-row7.stat_local
                    i1=row7.stat_local
                    row7.stat_local=0
                    km2=row7.kom
                elif n_set==8:
                    row8.zrzucanie_g1()
                    stat2=stat2-row8.stat_local
                    i1=row8.stat_local
                    row8.stat_local=0
                    km2=row8.kom
                elif n_set==9:
                    row9.zrzucanie_g1()
                    stat2=stat2-row9.stat_local
                    i1=row9.stat_local
                    row9.stat_local=0
                    km2=row9.kom
                else:
                    row10.zrzucanie_g1()
                    stat2=stat2-row10.stat_local
                    i1=row10.stat_local
                    row10.stat_local=0
                    km2=row10.kom
                nr=n_set
                nr=str(nr)
                m2=l_set+nr
                ms2.append(m2)
                ms=[]
            while i2!=0 and stat!=0:
                wait()
                print("=================")
                print(f"{niebieski}  RUCH GRACZA 2  {biały}")
                print("=================")
                time.sleep(1)
                wait()
                wplansza2(litery,sprow1,sprow2,sprow3,sprow4,sprow5,sprow6,sprow7,sprow8,sprow9,sprow10,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10,komunikat,km2,m2,stat,ms2)
                l_set=str(input("Podaj literę kolumny, na którą chcesz zrzucić bombę: "))
                l_set = l_set.upper()
                while l_set!="A"and l_set!="B"and l_set!="C"and l_set!="D"and l_set!="E"and l_set!="F"and l_set!="G"and l_set!="H"and l_set!="I"and l_set!="J":
                    wait()
                    print(f"{czerwony}Podałeś złą literę!{biały}")
                    time.sleep(1)
                    wplansza2(litery,sprow1,sprow2,sprow3,sprow4,sprow5,sprow6,sprow7,sprow8,sprow9,sprow10,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10,komunikat,km2,m2,stat,ms2)
                    l_set=str(input("Podaj nową literę kolumny, na którą chcesz zrzucić bombę: "))
                    l_set=l_set.upper()
                n_set=int(input("Podaj numer wiersza, na który chcesz zrzucić bombę: "))
                while n_set<0 or n_set>10:
                    wait()
                    print(f"{czerwony}Podałeś zły numer!{biały}")
                    time.sleep(1)
                    wplansza2(litery,sprow1,sprow2,sprow3,sprow4,sprow5,sprow6,sprow7,sprow8,sprow9,sprow10,gprow1,gprow2,gprow3,gprow4,gprow5,gprow6,gprow7,gprow8,gprow9,gprow10,komunikat,km2,m2,stat,ms2)
                    n_set=int(input("Podaj nowy numer wiersza, na który chesz zrzucić bombę: "))
                kol=k_litery[l_set]
                kol=kol+1
                row1.kol=k_litery[l_set]+1
                row1.row1_p=gprow1
                row1.row1_e=prow1
                row1.row0_p=litery
                row1.row0_e=litery
                row1.row2_p=gprow2
                row1.row2_e=prow2
                row2.kol=k_litery[l_set]+1
                row2.row1_p=gprow2
                row2.row1_e=prow2
                row2.row0_p=gprow1
                row2.row0_e=prow1
                row2.row2_p=gprow3
                row2.row2_e=prow3
                row3.kol=k_litery[l_set]+1
                row3.row1_p=gprow3
                row3.row1_e=prow3
                row3.row0_p=gprow2
                row3.row0_e=prow2
                row3.row2_p=gprow4
                row3.row2_e=prow4
                row4.kol=k_litery[l_set]+1
                row4.row1_p=gprow4
                row4.row1_e=prow4
                row4.row0_p=gprow3
                row4.row0_e=prow3
                row4.row2_p=gprow5
                row4.row2_e=prow5
                row5.kol=k_litery[l_set]+1
                row5.row1_p=gprow5
                row5.row1_e=prow5
                row5.row0_p=gprow4
                row5.row0_e=prow4
                row5.row2_p=gprow6
                row5.row2_e=prow6
                row6.kol=k_litery[l_set]+1
                row6.row1_p=gprow6
                row6.row1_e=prow6
                row6.row0_p=gprow5
                row6.row0_e=prow5
                row6.row2_p=gprow7
                row6.row2_e=prow7
                row7.kol=k_litery[l_set]+1
                row7.row1_p=gprow7
                row7.row1_e=prow7
                row7.row0_p=gprow6
                row7.row0_e=prow6
                row7.row2_p=gprow8
                row7.row2_e=prow8
                row8.kol=k_litery[l_set]+1
                row8.row1_p=gprow8
                row8.row1_e=prow8
                row8.row0_p=gprow7
                row8.row0_e=prow7
                row8.row2_p=gprow9
                row8.row2_e=prow9
                row9.kol=k_litery[l_set]+1
                row9.row1_p=gprow9
                row9.row1_e=prow9
                row9.row0_p=gprow8
                row9.row0_e=prow8
                row9.row2_p=gsprow10
                row9.row2_e=prow10
                row10.kol=k_litery[l_set]+1
                row10.row1_p=gprow10
                row10.row1_e=prow10
                row10.row0_p=gprow9
                row10.row0_e=prow9
                row10.row2_p=litery
                row10.row2_e=litery
                if n_set==1:
                    row1.zrzucanie_g2()
                    stat=stat-row1.stat_local
                    i2=row1.stat_local
                    row1.stat_local=0
                    km1=row1.kom
                elif n_set==2:
                    row2.zrzucanie_g2()
                    stat=stat-row2.stat_local
                    i2=row2.stat_local
                    row2.stat_local=0
                    km1=row2.kom
                elif n_set==3:
                    row3.zrzucanie_g2()
                    stat=stat-row3.stat_local
                    i2=row3.stat_local
                    row3.stat_local=0
                    km1=row3.kom
                elif n_set==4:
                    row4.zrzucanie_g2()
                    stat=stat-row4.stat_local
                    i2=row4.stat_local
                    row4.stat_local=0
                    km1=row4.kom        
                elif n_set==5:
                    row5.zrzucanie_g2()
                    stat=stat-row5.stat_local
                    i2=row5.stat_local
                    row5.stat_local=0
                    km1=row5.kom
                elif n_set==6:
                    row6.zrzucanie_g2()
                    stat=stat-row6.stat_local
                    i2=row6.stat_local
                    row6.stat_local=0
                    km1=row6.kom
                elif n_set==7:
                    row7.zrzucanie_g2()
                    stat=stat-row7.stat_local
                    i2=row7.stat_local
                    row7.stat_local=0
                    km1=row7.kom
                elif n_set==8:
                    row8.zrzucanie_g2()
                    stat=stat-row8.stat_local
                    i2=row8.stat_local
                    row8.stat_local=0
                    km1=row8.kom
                elif n_set==9:
                    row9.zrzucanie_g2()
                    stat=stat-row9.stat_local
                    i2=row9.stat_local
                    row9.stat_local=0
                    km1=row9.kom
                else:
                    row10.zrzucanie_g2()
                    stat=stat-row10.stat_local
                    i2=row10.stat_local
                    row10.stat_local=0
                    km=row10.kom
                nr=n_set
                nr=str(nr)
                m=l_set+nr
                ms.append(m)
                ms2=[]
        end=time.time()
        czas=int(end-start)
        minuta=0
        while czas>=60:
            minuta=minuta+1
            czas=czas-60
        if stat==0:
            winner="gracz 2"
        else:
            winner="gracz 1"
        wait()
        print("======================================================")
        print(f"|                {zielony}GRA SKOŃCZONA!{biały}                      |")
        print(f"| Zwycięzca: {winner}                                 |")
        if minuta>9 and czas>9:
            print(f"| Czas gry: {minuta}min {czas}s                                |")
        elif minuta>9 and czas<10:
            print(f"| Czas gry: {minuta}min {czas}s                                 |")
        elif minuta<10 and czas>9:
            print(f"| Czas gry: {minuta}min {czas}s                                 |")
        else:
            print(f"| Czas gry: {minuta}min {czas}s                                  |")
        if winner=="gracz 2":
            print(f"| Niezatopione statki: {stat2}                             |")
        else:
            print(f"| Niezatopione statki: {stat}                             |")
        print("|                                                    |")
        # print("| Jeśli chcesz zagrać jeszcze raz, kliknij 1         |")
        print("======================================================")
        # g=int(input())
        # while g!=1:
        #     g=int(input())
        # w_menu=0
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
            print(f"|  {pogrubienie}3 - Dostosuj okno terminalu{biały}                /_ _|           |")
            print("|                                          _ _ _ _|_ _ _      |")
            print("|  0 - Powrót do ekr. startowego           \ _ _ _ _ _ /      |")
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
            elif ust==3:
                zm=1
                while zm!=0:
                    wait()
                    print("∧ <--------------------------------------------------------------------------------------------------->")
                    for t in range (14):
                        print("|")
                    zm=int(input(f"∨   {pogrubienie}{zielony}Dostosuj minimalną wysokość i szerokość terminalu do strzałek. Aby wrócić to ustawień, wciśnij 0: {biały}"))
            elif ust!=0:
                print(f"{czerwony}Podano nieprawidłową liczbę!{biały}")
        w_menu=0         
        # print(f"{niebieski}Ustawienia są obecnie niedostępne{biały}")
        # menu(w_menu)
    else:
        wait()
        print(f"{czerwony}Podano nieprawdiłową liczbę{biały}")
        w_menu=0