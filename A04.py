def magia(tekst):
    linie = tekst.split('\n')
    cenzura = []
    for indeks, linia in enumerate(linie):
        if (indeks + 1) % 3 == 0:
            cenzura.append('*****')
        elif 'kocham' in linia.lower():
            cenzura.append('*****')
        else:
            cenzura.append(linia)
    return '\n'.join(cenzura)

with open('wejscie.txt', 'r') as plik_wejsciowy:
    tekst = plik_wejsciowy.read()

nowy = magia(tekst)

with open('nowe.txt', 'w') as plik_wyjsciowy:
    plik_wyjsciowy.write(nowy)

