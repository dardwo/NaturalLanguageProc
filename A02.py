kwadraty = [x**2 for x in range(51)]
print(kwadraty)

szesciany = [x**3 for x in range(20, 31)]
print(szesciany)

funkcja = [3*x - 2 for x in range(-5, 6)]
print(funkcja)

parki= [(x, y) for x in range(10, 21) for y in range(5, 11)]
print(parki)

iksy = range(4, 8)
igreki = ["jabłko", "gruszka", "komputer"]

pary = [(x, y) for x in iksy for y in igreki]
print(pary)
