count = 0

with open("dracula.txt", "r") as foo:
    for line in foo:
        if "vampire" in line.lower():
            count += 1
            print(line)
print('There are:', count, 'lines.')
