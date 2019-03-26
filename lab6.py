#get a word
def get_word():
    word = input("Please enter a word: ").strip().lower()
    return word


#initialize
LETTER = 'a'
#clarify if a letter in the word is a vowel or nah
def is_vowel(LETTER):
    #return true when letter is vowel
    if LETTER == 'a' or LETTER == 'e' or LETTER == 'i' or LETTER == 'o' or LETTER == 'u':
        return True
    #return false when letter is not vowel
    else:
        return False


#calculate how many time 'VC' appears
def calculate_measure(word):
    #initialization
    MEASURE = 0
    #going through each letter
    for i in range(len(word) - 1):
        #ex)is first letter[i] in word True and second letter[i+1] in word False
        if is_vowel(word[i]) == True and is_vowel(word[i+1])== False:
            #if true add one to measure
            MEASURE +=1
            
    return MEASURE

#run all of the functions
def main():
    word = get_word()
    measurement = calculate_measure(word)

    #output the word and the measurement of the word
    print(word, 'has a measure of', measurement)

main()
