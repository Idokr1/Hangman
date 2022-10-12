def choose_word(file_path, index):
    with open(file_path, 'r') as words:
        list_of_words = words.read().split(' ')
    i = (index - 1) % len(list_of_words)
    return list_of_words[i]

def print_opening_page():
    HANGMAN_ASCII_ART = """ Welcome to the game Hangman
     _    _
    | |  | |
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
    |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_  \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |                      
                        |___/ """

    return HANGMAN_ASCII_ART

def print_hangman(num_of_tries):
    picture_1 = """
    x-------x"""
    picture_2 = """
    x-------x
    |
    |
    |
    |
    |"""
    picture_3 = """
    x-------x
    |       |
    |       0
    |
    |
    |"""
    picture_4 = """
    x-------x
    |       |
    |       0
    |       |
    |
    |""" 
    picture_5 = """
    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |"""
    picture_6 = """
    x-------x
    |       |
    |       0
    |      /|\ 
    |      /
    |"""
    picture_7 = """
    x-------x
    |       |
    |       0
    |      /|\ 
    |      / \ 
    |"""

    HANGMAN_PHOTOS = {"1": picture_1, "2": picture_2, "3": picture_3, "4": picture_4, "5": picture_5, "6": picture_6, "7": picture_7}

    if(num_of_tries == 0):
        print("Your status:")
        print(HANGMAN_PHOTOS["1"])
    elif(num_of_tries == 1):
        print("Your status:")
        print(HANGMAN_PHOTOS["2"])
    elif(num_of_tries == 2):
        print("Your status:")
        print(HANGMAN_PHOTOS["3"])
    elif(num_of_tries == 3):
        print("Your status:")
        print(HANGMAN_PHOTOS["4"])
    elif(num_of_tries == 4):
        print("Your status:")
        print(HANGMAN_PHOTOS["5"])
    elif(num_of_tries == 5):
        print("Your status:")
        print(HANGMAN_PHOTOS["6"])
    elif(num_of_tries == 6):
        print("Your status:")
        print(HANGMAN_PHOTOS["7"])

def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def show_hidden_word(secret_word, old_letters_guessed, current_word_guessed):
    hidden_word = ""
    count = 0
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_word += letter
        else:
            hidden_word += "_"
    if current_word_guessed == hidden_word:
        count = 1
    return hidden_word, count

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if (len(letter_guessed) > 1 or not letter_guessed.isalpha()):
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    else:        
        return True
    
def main():
    HANGMAN_ASCII_ART = print_opening_page()
    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART, "\n", MAX_TRIES)

    word_index = int(input("Please enter a number (index) to choose a word out of the 'words.txt' file: "))
    secret_word = choose_word("words.txt", word_index)
    num_of_tries = 0
    count = 0
    old_letters = []
    current_word_guessed = "_" * len(secret_word)
    print_hangman(num_of_tries)

    while num_of_tries < MAX_TRIES:
        letter_guessed = input("Please guess a character: ")        
        is_valid = try_update_letter_guessed(letter_guessed, old_letters)
        if(is_valid):
            letter_guessed = letter_guessed.lower()
            old_letters += [letter_guessed]
            current_word_guessed, count = show_hidden_word(secret_word, old_letters, current_word_guessed)
            num_of_tries += count
            print(current_word_guessed)
            print_hangman(num_of_tries)            
            is_winner = check_win(secret_word, old_letters)
            if(is_winner):
                print("You won! The word is:", secret_word)
                break
        else:
            print("X")
            old_letters_string = " -> ".join(old_letters)
            print("Letters guessed until now:\n", old_letters_string)

    print("You Lost! The word was:", secret_word)
if __name__ == "__main__":
    main()