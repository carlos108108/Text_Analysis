'''
author = Karel Novák aka carlos108108
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

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
ODD = "-" * 40
MATCH = {
 "bob" :    "123",
 "ann" :  "pass123",
 "mike" : "password123",
 "liz"  : "pass123",
}
print(ODD)
print("Welcome to the app. Please log in:")
x = 3
while x:
    username = input("USERNAME: ")
    password = input("PASSWORD: ")
    if MATCH.get(username) == password:
        break
    x -= 1
    print(f"You have only {x} attempt(s)")
    if not x:
        print("Sorry, next time")
        exit()

print(ODD)
print(f"We have {len(TEXTS)} text to be analysed.")

x = 10
while x:
    choice = input(f"Enter the number between 1 and {len(TEXTS)} to select: ")
    if choice.isnumeric() and int(choice) in range(1,len(TEXTS)+1): #nehlásí chybu když zadáno písmeno, znak
        choice = int(choice)
        break
    print(f"You have to enter the number between 1 and {len(TEXTS)}")
    x -= 1
    if not x:
        print("Sorry, next time")
        exit()
print(ODD)
text = TEXTS[choice - 1]
text1 = text.split()

print(f"There are {len(text1)} words in the selected text.")

counter_title = 0
counter_upper = 0
counter_lower = 0
counter_numeric = 0
numbers = 0

for i in range(len(text1)):

    if text1[i].istitle():
        counter_title += 1

    if text1[i].isupper():
        counter_upper += 1

    if text1[i].islower():
        counter_lower += 1

    if text1[i].isnumeric():
        counter_numeric += 1
        numbers += float(text1[i])

print(f"There are {counter_title} titlecase words.")
print(f"There are {counter_upper} uppercase words.")
print(f"There are {counter_lower} lowercase words.")
print(f"There are {counter_numeric} numeric strings.")
print(ODD)

amount = {}
while text1:
    word = text1.pop().strip(",.")
    amount[len(word)] = amount.get(len(word),0) + 1

l = list()
for i in range(len(amount)):
    x = amount.popitem()
    l.append(x)

for i in range(len(l)):
    z = (min(l))                                    #zjištění tuple s nejmenší hodnotou-podle první hodnoty v tuple
    print(z[0], "\t", "*" * z[1], z[1])             #"naformátování" grafu
    l.remove(z)                                     #odstranění nejmenšího tuple
print(ODD)

print(f"If we summed all the numbers in this text we would get: {numbers}")
print()