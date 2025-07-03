"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lucie Robošová
email: lucka.robosova@gmail.com

"""


# ----------------------------------------------------------------------
# vstupní data

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


# ----------------------------------------------------------------------
# ověření jména + hesla a přihlášení do programu

username = input("username:")
password = input("password:")

if username in registered and registered[username] == password:
    print(line)
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print(line)
else:
    print("unregistered user, terminating the program..")
    quit()


# ----------------------------------------------------------------------
# výběr textu

text_number_str = input("Enter a number btw. 1 and 3 to select: ")

if not text_number_str.isdigit():
    print("Invalid input. Please enter a number. Terminating the program..")
    quit()

text_number_int = int(text_number_str)

if text_number_int < 1 or text_number_int > 3:
    print("Invalid value. Please enter a number between 1 and 3. Terminating the program..")
    quit()

print(line)

selected = TEXTS[text_number_int - 1]


# ----------------------------------------------------------------------
# analýza počtů slov a součtu číslic v textu

words = selected.split()

word_count = len(words)

word_titlecase = 0
word_uppercase = 0
word_lowercase = 0
word_numeric = 0
word_numeric_sum = 0

for word in words:
    if word.istitle():
        word_titlecase += 1
    if word.isupper():
        word_uppercase += 1
    if word.islower():
        word_lowercase += 1
    if word.isnumeric():
        word_numeric += 1
    if word.isdigit():
        word_numeric_sum += int(word)

print(f"""
There are {word_count} words in the selected text.
There are {word_titlecase} titlecase words.
There are {word_uppercase} uppercase words.
There are {word_lowercase} lowercase words.
There are {word_numeric} numeric strings.
The sum of all the numbers {word_numeric_sum}
""".strip())


