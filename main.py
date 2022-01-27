#Step 1 
import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list

word = random.choice(word_list)
length = len(word)

logo = hangman_art.logo
print(logo)

dash_word = []
for n in range(0,length):
    dash_word.append("_")
print(dash_word)
    
array_word = []
for n in range(0,length):
    array_word.append(word[n])

game_over = False

life = 6
stages = hangman_art.stages
print(stages[life])
while not game_over:
    user_letter = input("Enter a letter ").lower()
    if (user_letter in array_word):        
        for n in range(0,length):
            if user_letter == array_word[n]:
                dash_word[n] = array_word[n]
        print(dash_word)
    else:
        life -= 1
        print(stages[life])    
    
    if "_" not in dash_word:
        game_over = True
        print("You Win")
    elif life <= 0:
        game_over = True
        print("You Lose")    
print(f"\t\t\t{array_word}")
input("Press any button to exit....")



