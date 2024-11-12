Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
print("Początkowa lista:", Moja_lista)

Moja_lista.append(42)
print("Dodano 42:", Moja_lista)

Moja_lista.insert(3, 99)
print("Wstawiono 99 na indeksie 3:", Moja_lista)

Moja_lista.extend([7, 8, 9])
print("Rozszerzono o [7, 8, 9]:", Moja_lista)

Moja_lista.remove(3)
print("Usunięto pierwsze 3:", Moja_lista)

usunięty = Moja_lista.pop(4)
print(f"Usunięto element z indeksu 4 ({usunięty}):", Moja_lista)

Moja_lista.clear()
print("Wyczyszczono listę:", Moja_lista)

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
print("Element o indeksie 2:", Moja_lista[2])
print("Podlista od indeksu 1 do 5 co 2 elementy:", Moja_lista[1:6:2])

Moja_lista.sort()
print("Posortowana lista:", Moja_lista)

Moja_lista.reverse()
print("Odwrócona lista:", Moja_lista)