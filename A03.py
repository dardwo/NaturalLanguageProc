slownik = {
    "jabłko": "apple",
    "samochód": "car",
    "pies": "dog",
    "kot": "cat",
    "książka": "book",
    "komputer": "computer",
    "dom": "house",
    "długopis": "pen",
    "telefon": "phone",
    "stół": "table",
}


def slownik(slowo, slownik):
    if slowo in slownik:
        return slownik[slowo]
    else:
        return "Tłumaczenie dla danego słowa nie istnieje: " + slowo


while True:
    slowo = input("Podaj słowo (wpisz wyjscie aby wyjść): ").lower()
    if slowo == "wyjscie":
        break
    tłumaczenie = slownik(slowo, slownik)
    print(f"Przetłumaczone słowo: {tłumaczenie}")
