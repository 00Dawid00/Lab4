lista_zakupow = {
    "chleb": 3.50,
    "mleko": 2.80,
    "jajka": 5.20,
    "masło": 4.00,
    "ser": 6.50
}

print("Lista zakupów:")
for artykul, kwota in lista_zakupow.items():
    print(f"{artykul}: {kwota} zł")

suma_wydatkow = sum(lista_zakupow.values())
print(f"\nSuma wydatków: {suma_wydatkow} zł")
