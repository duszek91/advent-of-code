def load(file):
    with open(f"{file}.txt") as data:
        dane = data.readlines()
        dane = [x.strip() for x in dane]
        return dane

def look_for_doubles(string):
    for x in range(len(string)-1):
        if string[x] == string[x+1]:
            return True
    else:
        return False
def check_forbiden(string):
    for x in range(len(string)-1):
        if (string[x] == "a" and string[x+1] == "b") or (string[x] == "c" and string[x+1] == "d") or \
                (string[x] == "p" and string[x+1] == "q") or (string[x] == "x" and string[x+1] == "y"):
            return False
    return True

def enough_vowels(string):
    vowels = 0
    samogloski="aeiou"
    for y in string:
        if y in samogloski:
            vowels+=1
    if vowels >=3:
        return True
    else:
        return False
dane = load("day5")
counter = 0

for x in dane:
    if look_for_doubles(x) and check_forbiden(x) and enough_vowels(x):
        counter+=1
# print(counter)
