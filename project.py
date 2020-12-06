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
MATCH = {                                       #vytvoření slovníku uživatelů s hesly
 "bob" :    "123",
 "ann" :  "pass123",
 "mike" : "password123",
 "liz"  : "pass123",
}
print(ODD)
print("Welcome to the app. Please log in:")
x = 3                                           #na zadání správné kombinace jsou 3 pokusy, pak se program ukončí
while x:                                        #použit cyklus WHILE
    username = input("USERNAME: ")
    password = input("PASSWORD: ")
    if MATCH.get(username) == password:
        break
    x = x - 1
    print(f"You have only {x} attempt(s)")
    if x == 0:
        print("Sorry, next time")
        exit()

print(ODD)
print("We have 3 text to be analysed.")
                                                     #10 pokusů na to zadat správnou volbu
for i in range(10):                                  #použita smyčka FOR
    choice = int(input("Enter the number between 1 and 3 to select: "))
    if choice == 1 or choice == 2 or choice == 3:
        break
    else:
        print("You have to enter number between 1 and 3")
    if i == 9:
        print("Sorry, next time")
        exit()
print(ODD)
text = TEXTS[choice - 1]

print(f"There are {len(text.split())} words in the selected text.") #pocet slov v textu

text1 = text.split()                                                #není to vůbec elegantní, ale nic jiného
text1 = tuple(text1)                                                #mě nenapadlo
x = 0
for i in range(0,len(text1)):
    if text1[i].istitle():
        x = x + 1
print(f"There are {x} titlecase words.")


x = 0                                                               #opět stejný postup (proměnná text1 už je tuple)
for i in range(len(text1)):
    if text1[i].isupper():
        x = x + 1
print(f"There are {x} uppercase words.")

for i in range(len(text1)):
    if text1[i].islower():
        x = x + 1
print(f"There are {x} lowercase words.")

x = 0
for i in range(len(text1)):
    if text1[i].isnumeric():
        x = x + 1
print(f"There are {x} numeric strings.")
print(ODD)
