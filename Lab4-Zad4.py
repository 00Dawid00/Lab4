zdanie = input("Podaj zdanie: ").lower()
litery_w_zdaniu = sorted(set(char for char in zdanie if char.isalpha()))
brakujące_litery = sorted(set("abcdefghijklmnopqrstuvwxyz") - set(litery_w_zdaniu))

print("Litery w zdaniu (alfabetycznie):", " ".join(litery_w_zdaniu))
print("Brakujące litery:", " ".join(brakujące_litery))
