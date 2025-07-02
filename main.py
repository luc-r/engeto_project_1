"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lucie Robošová
email: lucka.robosova@gmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

line = "-" * 40

registered = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
}

username = input("username:")
password = input("password:")
print(line)

if username in registered and registered[username] == password:
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print(line)
else:
    print("unregistered user, terminating the program..")

number = int(input("Enter a number btw. 1 and 3 to select: "))
print(line)

selected = TEXTS[number - 1]

words = selected.split()

word_count = len(words)

word_titlecase = 0
for word in words:
    if word.istitle():
        word_titlecase += 1

word_uppercase = 0
for word in words:
    if word.isupper():
        word_uppercase += 1

word_lowercase = 0
for word in words:
    if word.islower():
        word_lowercase += 1

word_numeric = 0
for word in words:
    if word.isnumeric():
        word_numeric += 1


print(f"There are {word_count} words in the selected text.")
print(f"There are {word_titlecase} titlecase words.")
print(f"There are {word_uppercase} uppercase words.")
print(f"There are {word_lowercase} lowercase words.")
print(f"There are {word_numeric} numeric strings.")


# There are 54 words in the selected text.
# There are 11 titlecase words.
# There are 1 uppercase words.
# There are 38 lowercase words.
# There are 4 numeric strings.
# The sum of all the numbers 8540