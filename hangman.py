#Author: Elias Meshesha
#Date: 10/22/20
#Description: Hangman but not qyite, unofficial version
import random                                           # Importing random for later
import time


print("Welcome!!! This has been a grueling game to make!!!")
print("If the comments do not make sense, feel free to ask in slack")
print("Only one rule: This code will only take a character per submit")
print("Ready!!!")
print("Begin!!!")

a = "cat", "dog", "monkey"
b = "eragon", "harry potter", "gandalf"
c = "overwatch", "call of duty", "magic the gathering"
d = "computer science", "electrical engineering", "computer engineering"
e = "bird is the word", "somewhere over the rainbow", "sandstorm"
WordBank = a + b + c + d + e             #word bank
word = random.choice(WordBank)           #Random string is taken from the wordbank

if word in a:
    print("type of animal")
if word in b:
    print("movie character")
if word in c:
    print("type of game")
if word in d:
    print("type of major")
if word in e:
    print("what is this song title")
w = ""
c_1 = 0                               #To get total number of characters in word
for letter in word:
    if letter == " ":                 #To take care of those pesky words separated by a space
        w += " "                      #Later on, we are going to give the user " " for free.
    else:
        w += "_"
    c_1 += 1
w_1 = []                              #Since strings are immutable, in order to manipulate them, we need to turn the string
w_2 = []                              #into a set. This is the starting procedure
for num in range(0,c_1):
    w_1.append("_")                   #From that empty set, we add "_" for every character in word, so we are recreating w.
    w_2.append(word[num])             #We turn the word into a set here .
print(w)                              #Will tell the user how many characters are in the word
count = 0
x = True
while x:
    user_input = input("Guess a letter:")
    user_input = user_input.lower()                 #turns input to lowercase
    y = 0                                           #initialized inside the while loop so it is always reset to 0
    for elements in w_2:                            #I do this because of the case where the first element in w_2
        if user_input != elements:                  #might not be equal to user_input, but the second one is
            y += 0
        else:
            y += 1                                 #if the element in the word is equal to user_input then we add 1 to y.

    if y >= 1:                                      #Unnessary but whatever, if we are in here, we know that there is a
        for letter in word:                         #letter in word that matches user_input
            for num in range(0,c_1):                #it should go from 0 to c_1, becuase c[0] represents the first letter in c
                if word[num] == user_input:
                    w_1[num] = user_input           #Because w_1 is a set, we can manipulate it by this line, and it just takes
                if word[num] == " ":                #that specific section and changes that to user_input = letter
                    w_1[num] = " "                  #Giving space away for free


    w = ""
    for num in range (0,c_1):
        w += w_1[num]                               #We are going back from a set to a string through this section
    if w == word:
        print(w)
        print("You win")
        break                                      #To get out of the loop; Poor man's break line

    if y != 0:                                    #Adding this so output looks nice for the case where you initially guessed it right
        print(w)                                  #and then wrong afterwards, resulting in w being ouputted twice

    if y == 0:                                    #For the case when the user_input does not equal any of the letters in word
        if count == 0:
            print("    |  ")                      #hangman is starting to take form
            print(w)
            count += 1                            #adding 1 to the count because I don't want it to draw this part again
        elif count == 1:                          #so whenever y = 0, we check the condition what is the count we are on, and then we draw
            print("    |  ")
            print("   /  ")
            print(w)
            count += 1
        elif count == 2:
            print("    |  ")
            print("  0/  ")
            print(w)
            count += 1
        elif count == 3:
            print("    |  ")
            print("  O/  ")
            print("  | ")
            print(w)
            count += 1
        elif count == 4:
            print("    |  ")
            print("  O/  ")
            print("/ | ")
            print(w)
            count += 1
        elif count == 5:
            print("    |  ")
            print("  O/  ")
            print("/ | \\")
            print(w)
            count += 1
        elif count == 6:
            print("    |  ")
            print("  O/  ")
            print("/ | \\")
            print(" / ")
            print(w)
            count += 1
        elif count == 7:
            print("    |  ")
            print("  O/  ")
            print("/ | \\")
            print(" / \\")
            print("YOU LOSE")                # then you lose
            x = False                        #To get out of the loop; This is the thinking man's break line.


print("Play again, resetting!!!")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("JK, I am too lazy to figure all of that out")


