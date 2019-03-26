#getting the megnitudes
def get_magnitude(num):
    #Asking for input of earthquake
    MAGNITUDE = float(input("Please enter magnitude {0} of "
                            "earthquake: ".format(num)))
    #Validating it's a real value
    while MAGNITUDE <= 0:
        MAGNITUDE = float(input("Please enter magnitude {0} of "
                                "earthquake: ".format(num)))
    #sending input of magnitude1 and magnitude2
    return MAGNITUDE


#calculating difference
def compare_magnitude(MAGNITUDE1,MAGNITUDE2):
    f = 10**(1.5*(MAGNITUDE1 - MAGNITUDE2))
    return f


#play again??
def run_again():
    REPEAT = int(input("Enter 1 to Play: "))

    if REPEAT == 1:
        return True


#main function
def main():
    
    #initialize
    again = True
    #LOOP OR NAH
    while again == True:
        #getting the magnitude
        MAGNITUDE1 = get_magnitude(1)
        MAGNITUDE2 = get_magnitude(2)

        #which magnitude is greater
        if MAGNITUDE1 > MAGNITUDE2:
            f = compare_magnitude(MAGNITUDE1,MAGNITUDE2)
            #printing answer
            print('An earthquake of magnitude {0} is {1:.1f} times greater than an '
                  'earthquake of magnitude {2}'.format(MAGNITUDE1, f, MAGNITUDE2))

        #which magnitude is greater
        else:
            f = compare_magnitude(MAGNITUDE2,MAGNITUDE1)
            #printing answer
            print('An earthquake of magnitude {0} is {1:.1f} times greater than an '
                  'earthquake of magnitude {2}'.format(MAGNITUDE2, f, MAGNITUDE1))
        #VALUE THAT DECIDE IF LOOP OR NAH 
        again = run_again()

main()

#RESEARCH QUEST

    #MAGNITUDES:
    #1a) 2011 Tohoku earthquake, Japan: 9.0
    #1b) 1989 Loma Prieta earthquake, San Francisco, USA: 6.9
    #1c) 2010 Haiti earthquake: 7.0

    #2) 1000
    #DEATH
    #3) 2011 Tohoku earthquake, Japan: 13,000
    #   2010 Haiti earthquake: 230,000
    #   Yes, this gives me an appreciation of how modern technology
    #   and government building code could help warn people before distasters
    #    strikes to reduce deaths
