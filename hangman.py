import random
import re
#put the list countaining a lot of words
hangman_list = open('wordlist.txt').read().splitlines() # reads the file "wordlist.txt" and put it as a list
shuffled_word = random.choice(hangman_list) # take at random a word from the list
shuffled_word = shuffled_word.lower()
hidden_word = ''
for x in shuffled_word:
    hidden_word = hidden_word + '_'
hidden_word = list(hidden_word)

word_lenght = len(shuffled_word) # counts the lenght of the word which has been picked at random

tries = 0 # the number of total guesses from the user, starting at 0

print("\n\nThe word you are looking for is",word_lenght, "characters long\n")


def ask():
    global tries
    global hidden_word
    while(tries < 7 ):
        i = 0
        wrongLetters = []
        for x in shuffled_word:
            print('you have', 7-tries, 'remaining tries')
            ask_letter = str(input("Enter a letter : ")) # asking the user to guess a leter
            ask_letter = ask_letter.lower()
            regex = re.findall("[a-z]", ask_letter)
            if(len(ask_letter) == 1 and regex):
                if(ask_letter in shuffled_word):
                    letterLength = 0
                    for x in shuffled_word:
                        if(x==ask_letter):
                            hidden_word[shuffled_word.find(ask_letter, letterLength)] = ask_letter
                            letterLength = shuffled_word.find(ask_letter, letterLength) +1
                else:
                    wrongLetters.append(ask_letter+ ',')
                    print("you're gay")
                    tries += 1
                    if(tries == 7):
                        lose()
                i += 1
                print("".join(hidden_word))
                print('wrong letters list :',"".join(wrongLetters))
                if('_' not in "".join(hidden_word)):
                    print('you won, now kill yourself')
                    exit()
            else:
                lose()
    else:
        print('you dumb as fuck')

def lose():
    print('u lose kill youself')
    print('the word was', shuffled_word)
    exit()

ask()
