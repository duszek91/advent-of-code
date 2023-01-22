def wczytaj(plik):
    with open(f"{plik}.txt") as file:
        dane = file.readlines()
        return dane
def dodaj_do_listy(znak):
    obecna = list(COORDINATES[-2])
    if znak == "^":
        obecna[1] += 1
    elif znak == "v":
        obecna[1] -= 1
    elif znak == "<":
        obecna[0] -= 1
    else:
        obecna[0] += 1

    COORDINATES.append(tuple(obecna))


COORDINATES = [(0,0),(0,0)]
dane = wczytaj("day3")
for x in range(len(dane[0])):
    dodaj_do_listy(dane[0][x])
print(len(set(COORDINATES)))
