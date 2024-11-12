imie = input("Podaj swoje imię: ")
print("Witaj", imie)

wiek = int(input("Podaj swój wiek: "))
print("Twój wiek to:", wiek)

imie, nazwisko = input("Podaj imię i nazwisko: ").split()
inicjaly = imie[0].upper() + "." + nazwisko[0].upper() + "."
print("Inicjały:", inicjaly)

lancuch = input("Podaj łańcuch znaków: ")
print(lancuch * 5)

lancuch1 = input("Podaj pierwszy łańcuch znaków: ")
lancuch2 = input("Podaj drugi łańcuch znaków: ")
lancuch3 = lancuch1 + lancuch2
print("Połączenie tych łańcuchów znaków:", lancuch3)

lancuch1 = input("Podaj pierwszy łańcuch znaków: ")
lancuch2 = input("Podaj drugi łańcuch znaków: ")
lancuch3 = lancuch1 + lancuch2
polowa = len(lancuch3) // 2
pierwsza_polowa = lancuch3[:polowa]
print("Pierwsza część połączonego łańcucha znaków:", pierwsza_polowa)
