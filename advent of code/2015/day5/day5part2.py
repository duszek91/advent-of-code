from day5 import load


def look_for_doubles(string):
    duplicates = []
    for x in range(len(string) - 1):
        if string[x] == string[x + 1]:
            if string[x] == string[x - 1]:
                continue
            duplicates.append(string[x] + string[x + 1])
        else:
            duplicates.append(string[x] + string[x + 1])
    if len(duplicates) != len(set(duplicates)):
        return True
    else:
        return False


def look_for_secound(string):
    for x in range(len(string) - 2):
        if string[x] == string[x + 2]:
            return True
    return False


dane = load("day5")
counter = 0

for x in dane:

    if look_for_doubles(x) and look_for_secound(x):
        counter += 1
print(counter)
