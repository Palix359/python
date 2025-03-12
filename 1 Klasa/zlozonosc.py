import time

lista=[1,2,3,4,5,6,7,8,9,10]
for i in lista:
    print(i)




n=int(input("Podaj liczbę całkowitą: "))
start=time.time()
for i in range(n):
    for j in range(n):
        print("#", end='')
    print()

end=time.time()
print(end-start)