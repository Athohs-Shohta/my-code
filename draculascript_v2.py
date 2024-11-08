f = open("vampytime.txt", "a")


with open("dracula.txt", "r") as foo:
    for line in foo:
        if "vampire" in line.lower():
            print(line)
            f.write(line)
f.close()
