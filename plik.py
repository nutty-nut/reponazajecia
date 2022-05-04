# ZADANIE11
print("Wybierz: papier, kamień, nożyce\n(1)papier\n(2)kamień\n(3)nożyce")
czlowiek = int(input())
komp = random.randint(1,3)
if komp == 1:
    print("wybór komputera - papier")
elif komp == 2:
    print("wybór komputera - kamień")
elif komp == 3:
    print("wybór komputera - nożyce")
if komp == czlowiek: print("rowno, remisy")
elif czlowiek==1 and komp==2 or czlowiek==2 and komp==3 or czlowiek==3 and komp==1: print("WYGRYWASZ TY")
else: print("WYGRYWA KOMPUTER, haha przegrałeś")

# ZADANIE12
print("Odliczanie od podanej liczby sekund do zera")
liczba=int(input())
print()
for i in range(liczba,0,-1):
    print(i)
    time.sleep(1)
print("O\nKONIEC")
print("Niespodzianka")
