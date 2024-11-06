#!/usr/bin/env python3

def main():

marvelchars= {
    "Starlord":
    {"real name": "peter quill",
    "powers": "dance moves",
    "archenemy": "Thanos"},

    "Mystique":
    {"real name": "raven darkholme",
    "powers": "shape shifter",
    "archenemy": "Professor X"},

    "Hulk":
    {"real name": "bruce banner",
    "powers": "super strength",
    "archenemy": "adrenaline"}
                }

print("Which character do you want to know about?" marvel chars)
    char_name = input("Starlord", "Mystique", "Hulk")

print("What statistic do you want to know about? (real name, powers, archenemy)")
    char_stat = input()

print(char_name "'s" char_stat is: marvelchars.get('char_name )

main()
