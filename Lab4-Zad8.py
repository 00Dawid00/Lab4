stopnie = ("Szeregowy", "Kapral", "Sierżancie", "Porucznik", "Kapitan", "Major", "Pułkownik",)

ilość_stopni = len(stopnie)

Major_index = stopnie.index("Major")

Pułkownik_występowanie = "Tak" if "Pułkownik" in stopnie else "Nie"

print(f"Liczba wszystkich stopni wojskowych: {ilość_stopni}")
print(f"Indeks krotki dla elementu 'Major': {Major_index}")
print(f"Czy 'Pułkownik' znajduje się w krotce stopnie: {Pułkownik_występowanie}")
