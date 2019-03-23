import EnglishDictionary

#options menu
def print_menu():
    print("1 - Check a palindrome")
    print("2 - Check a crossword square")
    print("3 - Quit")


#recieve choice
def get_menu_choice():
    function_choice = int(input('Choose a function: '))
    #if the choice is not 1,2, or 3 ask the user again
    while function_choice <= 0 or function_choice >= 4:
        function_choice = int(input('Choose a function: '))

    #give back user's choice
    return function_choice


#recieve a phrase for menu option 1
def get_phrase():
    phrase = input('Enter a phrase: ')
    #length of the phrase
    phrase_len = len(phrase)
    #if the length of the phrase is less than or equal to 0
    #there is no word so continue to ask for input again
    while phrase_len <= 0:
        phrase = input('Enter a phrase: ')
        phrase_len = len(phrase)

    #give back user's phrase
    return phrase


#return true or false
def is_palindrome(phrase):
    #lower case the phrase
    phrase_low = phrase.lower()
    i = 0                             #begining of phrase
    j = len(phrase_low)-1                 #ending of phrase
    
    #i and j have not cross
    while i<j:
        #character is not a letter, skip to next char.
        if not phrase_low[i].isalpha():
            i+=1
        #character is not letter, skip to next char.
        elif not phrase_low[j].isalpha():
            j-=1
        #concluded that both i and j are letters
        elif phrase_low[i].isalpha() and phrase_low[j].isalpha():   
            #conclude char. i and char. j are the same letter
            if phrase_low[i] == phrase_low[j]:
                i+=1                   #go to next i
                j-=1                   #go to next j
            #if char. i and char. j are not same letter, end
            else:
                return False

    #by end, all characters are the same letters, give true
    return True


#MENU OPTION 1
def menu_check_palindrome():
    #get users phrase
    phrase = get_phrase()
    #clarify if phrase is a palindrome, recieve True or False
    boolean = is_palindrome(phrase)
    #if True then it is a palindrome
    if boolean == True:
        print(phrase, "is a palindrome!")
    #if false it is not a palindrome
    else:
        print(phrase, "is not a palindrome.")


#recieve multiple words to create a crossword square
def get_crossword_square():
    #get first word
    first_line = input('Enter the first line of the crossword square: ')
    crossword_len = len(first_line)
    concatenated_string = first_line
    #get same amount of words as the length of the first word
    for i in range(crossword_len-1):
        next_line = input('Enter the next line of the crossword square: ')
        next_line_len = len(next_line)
        #ask again if word recieve is not same length as the first word
        while next_line_len != crossword_len:
            next_line = input('Enter the next line of the crossword square: ')
            next_line_len = len(next_line)

        #add the word into the string
        concatenated_string += next_line

    #give back a string with all of the words            
    return concatenated_string                


#check if the words in the crossword square are real or nah
def check_crossword_square(square):
    #lower case the string of words
    square_low = square.lower()
    #find length of the string of words
    square_len = len(square_low)
    #find order of square represented by n
    n = int(square_len**(1/2))

    i=0                  #starting letter
    j=1                  #multiple for next ending, n
    #start of string to end of string, skipping by order of squares n
    for i in range(0,square_len,n):
        #recieve one word
        #start of word(i) to end of word(n), then n*j for next word ending
        one_word = square_low[i:n*j]
        #check to see if it is a real word, give True or False
        boolean = EnglishDictionary.is_word(one_word)
        #it is a real word, go to next word
        if boolean == True:
            i+=n        #starting of next word
            j+=1        #ending of next word
        #not a real word, end task and give value False
        else:
            return False
            break

    #ask checking all of horizonal words are real words
    #now check if vertical words are real words

    s = 1               #starting letter
    for s in range(0,square_len,n):
        #get vertical word
        one_word = square_low[s::n]
        #check if vertical word is real
        boolean = EnglishDictionary.is_word(one_word)
        #if it is real continue to next vertical word
        if boolean == True:
            s+=1        #starting of next letter
        else:
            return False
            break

    return True


#MENU OPTION 2
def menu_check_crossword_square():
    #recieve users crosswords
    square = get_crossword_square()
    #length of the crossword
    square_len = len(square)
    #order of squares
    n = int(square_len**(1/2))
    #check if crossword are real words    
    boolean = check_crossword_square(square)

    #how to print out the crossword
    i=0                   #first letter
    j = 1                 #second number, multiple
    for i in range(0, square_len, n):
        print(square[i:n*j])      #first letter of word -> last letter of word
        j+=1              #next number to * n to get next word last letter
        i+=n              #start of next letter

    #output whether is or is not a crossword square
    if boolean == True:
        print("is a crossword square!")
    else:
        print("is not a crossword square.")


def main():
    function_choice = 0 #global varible, NOT Magic number
    #loop menu and choices until user enter 3
    while function_choice != 3:
        #output menu
        print_menu()
        #recieve choice from menu
        function_choice = get_menu_choice()
        #depending on choice
        #if 1 go to palindrome
        if function_choice == 1:
            menu_check_palindrome()
        #if 2 go to crossword
        elif function_choice == 2:
            menu_check_crossword_square()

        #if 3 exit
        if function_choice == 3:
            break
        
        

main()
