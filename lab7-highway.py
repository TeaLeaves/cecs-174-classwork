#recieve interstate number
def get_interstate_number():
    highway_num = int(input("Please enter a highway number: "))
    #if negitive or no number, repeat question
    while highway_num <= 0 or highway_num >= 1000:
        highway_num = int(input("Please enter a highway number: "))

    return highway_num


#2 digit = primary, 3 digit = auxiliary
def is_primary(number):
    if number <= 99:
        #primary interstate
        return True
    else:
        #auxiliary interstate
        return False

#orientaion of highway
def compass_orientation(number):
    #even number
    if number%2 == 0:
        return 'east-west'
    #odd number
    elif number%2 == 1:
        return 'north-south'


#long distance or nah
def is_arterial(number):
    if number%5 == 0:
        #long-distance arterial highway
        return True
    else:
        #short-distance arterial highway?
        return False


#find aux type of the highway
def auxiliary_type(number):
    first_number = number//100
    odd_or_even = first_number % 2
    #even
    if odd_or_even == 0:
        return 'radial'
    elif odd_or_even == 1:
        return 'spur'


#parent highway is last 2 number
def parent_highway(number):
    last_two_number = number%100

    return last_two_number


def menu():
    #recieve interstate number
    number = get_interstate_number()
    #primary or auxiliary
    interstate_number = is_primary(number)
    
    #output interstate number
    print('Interstate', number, 'is', end='')
    
    #primary highway
    if interstate_number == True:
        orientation = compass_orientation(number)
        distance = is_arterial(number)
        #output interstate number is long distance, if it is
        if distance == True:
            print(' a long-distance arterial highway', end='')

        #output orientation
        print(' oriented', orientation, end='.')
    
    #auxiliary highway
    elif interstate_number == False:
        #type of aux highway
        aux_type = auxiliary_type(number)
        #get parent highway
        parent = parent_highway(number)
        print(' a', aux_type, 'highway of', end='')
        print(' Interstate', parent, end='.')

menu()


#1)Dwight D Eisenhower
#2)405-S
#3)Bellingham, Washington
#Unlikely bc Washington is far from S. California
