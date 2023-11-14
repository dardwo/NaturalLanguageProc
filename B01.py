import re

imie = None
nazwisko = None
telefon = None
kod_pocztowy = None
miasto = None

while True:
    imie = input("Imię: ")
    if re.match("^[A-Z][a-z]*$", imie):
        break
    else:
        print("Imię powinno zaczynać się wielką literą i skladac tylko z liter.")

while True:
    nazwisko = input("Nazwisko: ")
    if re.match("^[A-Z][a-z]*$", nazwisko):
        break
    else:
        print("Nazwisko powinno zaczynać się wielką literą.")

while True:
    telefon = input("Telefon w formacie: (np. (61) 222-45-56): ")
    if re.match("^\(\d{2}\) \d{3}-\d{2}-\d{2}$", telefon):
        break
    else:
        print("Niepoprawny format telefonu. Wprowadź go w formacie (xx) xxx-xx-xx.")

while True:
    kod_pocztowy = input("Kod pocztowy w formacie: (np. 11-111): ")
    if re.match("^\d{2}-\d{3}$", kod_pocztowy):
        break
    else:
        print("Niepoprawny format kodu pocztowego. Wprowadź go w formacie xx-xxx.")

while True:
    miasto = input("Miasto: ")
    if re.match("^[A-Z][a-z]*$", miasto):
        break
    else:
        print("Miasto powinno zaczynać się wielką literą.")

print(imie)
print(nazwisko)
print(telefon)
print(kod_pocztowy)
print(miasto)
