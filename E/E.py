def load_polimorf_dict(filename):
    # Funkcja do wczytania słownika PoliMorf z pliku
    with open(filename, 'r', encoding='utf-8') as file:
        dictionary = set(line.strip() for line in file)
    return dictionary

def max_match(sentence, dictionary):
    words = []  # Lista, w której przechowamy rozdzielone słowa

    while sentence:
        # Rozpocznij od maksymalnej długości słowa (długość słowa w języku polskim jest zazwyczaj dość ograniczona)
        max_length = len(sentence)

        while max_length > 0:
            # Sprawdź, czy fragment zdania o długości max_length znajduje się w słowniku
            word = sentence[:max_length]
            if word in dictionary:
                words.append(word)  # Jeśli tak, dodaj je do listy słów
                sentence = sentence[max_length:]  # Skróć zdanie o znalezione słowo
                break
            max_length -= 1

        # Jeśli nie znaleziono pasującego słowa, zacznij od ostatniego znaku i usuń go z zdania
        if max_length == 0:
            words.append(sentence[-1])
            sentence = sentence[:-1]

    return words

if __name__ == "__main__":
    dictionary = load_polimorf_dict("PoliMorf.txt")

    while True:
        sentence = input("Podaj zdanie do segmentacji (lub wpisz 'exit' aby zakończyć): ")
        if sentence.lower() == "exit":
            break
        segmented = max_match(sentence, dictionary)
        print("Segmentacja:", " ".join(segmented))
