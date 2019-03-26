#Input must be in one of these 4 formats (XYZ representing numbers):
#Interstate XYZ
#I-XYZ
#IXYZ
#XYZ

#Casing matters
#Must ask again if:
#it is not one of the 4 formats, input is 0, input is a negitive number, or over 3 digit



#interstate number
def get_interstate_number():
    #global value
    n = 1
    j = 1
    
    #recieve interstate number
    interstate_num = input("Please enter a highway number: ")

    #make sure input is one of the four formats
    while j != 0:
        #if interstate number input are only numbers
        highway_num = interstate_num.isdigit()
        if highway_num == True:
            highway_num = int(interstate_num)
            #if the number is negitive or over 3 digit, ask again
            while highway_num <= 0 or highway_num >= 1000:
                interstate_num = input("Please enter a highway number: ")
                highway_num = int(interstate_num)
            
            return highway_num
            break
    
        #if interstate number start with I - mean: .startwith()
        elif interstate_num.startswith('I'):
            #if format is 'Interstate XYZ' - mean: .find()
            if interstate_num.find('Interstate') == 0:
                j *= 0
            #if format is 'I-XYZ' - mean: .find()
            elif interstate_num.find('I-') == 0:
                j *= 0
            #if format is 'IXYZ', 'I' appears at start only - mean: .count()
                
            elif interstate_num.count('I') == 1:
                j *= 0
            else:
                j += 1
                interstate_num = input("Please enter a highway number: ")

        #then it is one of the four format
        elif highway_num == False:
            j += 1
            interstate_num = input("Please enter a highway number: ")
            
        elif not(interstate_num.startswith('I')):
            j += 1
            interstate_num = input("Please enter a highway number: ")
            
            
    #find out the interstate number of input        
    while n != 0:
        #extract interstate number - mean: slicing[]
        highway_num_three = interstate_num[-3:]
        highway_num_two = interstate_num[-2:]
        highway_num_one = interstate_num[-1:]
        #if it's a number - mean: isdigit()
        if highway_num_three.isdigit() == True:
            highway_num = int(highway_num_three)
            n*=0
        elif highway_num_two.isdigit() == True:
            highway_num = int(highway_num_two)
            n*=0
        elif highway_num_one.isdigit() == True:
            highway_num = int(highway_num_one)
            n*=0
        else:
            interstate_num = input("Please enter a highway number: ")
            n+=1


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
