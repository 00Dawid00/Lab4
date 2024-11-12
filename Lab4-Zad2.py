imiona = ["Anna", "Krzysztof", "Beata", "Marek"]
print("Początkowa lista:", imiona)

imiona.sort()
print("Posortowana alfabetycznie:", imiona)

imiona.extend(["Tomasz", "Zofia"])
print("Po dodaniu dwóch osób:", imiona)

imiona.pop()
print("Po usunięciu ostatniej osoby:", imiona)

imiona.insert(3, "Ewa")
print("Po dodaniu osoby na pozycji 3:", imiona)

imiona.reverse()
imiona *= 2
print("Odwrócona i zdublowana lista:", imiona)
