#display menu
print("Main menu: ")
print("1. Warp Speed")
print("2. Cost of Launch")
print("3. Time Dilation")
print("4. Exit")

#choose from menu
choice = int(input())



#Constants
WARP = 1
SPEED_OF_LIGHT = 299_792_458

#Warp speed
if choice == 1:
    #validate usable input
    WARP = int(input("Please enter a warp factor: "))
    while WARP <= 0:
        #Gain warp factor
        WARP = int(input("Please enter a warp factor: "))
    #output
    else:
        v = (WARP**(10/3))*SPEED_OF_LIGHT
        print("Warp", WARP, ",engage!")
        print("You are now traveling at", "{0:,.2f}".format(v), "meters per second")


#Cost of Launch
if choice == 2:
    #constants
    ULA_COST_PER_KG = 14_830
    SPACEX_COST_PER_KG = 2720
    #validate usable input
    mass = float(input("Please enter the satellite's mass: "))
    while mass <= 0:
        #gain mass
        mass = float(input("Please enter the satellite's mass: "))

    #validate usable input
    cost = float(input("Please enter satellite cost in dollar: "))
    while cost <= 0:
        #gain cost
        cost = float(input("Please enter satellite cost in dollar: "))

    #output
    else:
        ula = mass * ULA_COST_PER_KG
        spacex = (mass * SPACEX_COST_PER_KG) + (cost * 0.3)
        if ula > spacex:
            final= (ula - spacex)
            name = 'Spacex'
        else:
            final= (spacex - ula)
            name = 'United Launch Alliance'
        
        print(name, "will save you","$","{0:,.2f}".format(final), "on this launch.")



#Time Dilation
        #WARNING: I asked for the VELOCITY(speed) first THEN the DISTANCE so the order is different than in the example!!!
if choice == 3:
    #constants
    SOL_TO_METER = 9_460_730_472_580_800
    SEC_TO_DAY = 86_400
    DAY_IN_YR = 365
    #validate usable input
    speed = float(input("Please enter a speed between 0.0 and 1.0: "))
    while (speed <= 0.0) or (speed >= 1.0):
        #gain speed
        speed = float(input("Please enter a speed between 0.0 and 1.0: "))

    #validate usable input
    distance = float(input("Please enter distance in light years: "))
    while distance <= 0:
        #gain distance
        distance = float(input("Please enter distance in light years: "))

    #output
    else:
        #convert speed
        speed = speed * SPEED_OF_LIGHT
        #find number of time that was traveled
        time_travel = ( (distance*SOL_TO_METER) / speed )
        
        #convert ^ to total days
        day_travel = time_travel / SEC_TO_DAY
        
        #number of years from total
        years = day_travel // DAY_IN_YR
        #number of days from total
        days_leftover = day_travel % DAY_IN_YR

        #how much time pass(during the trip)
        dilation = (  (1 -(  (speed**2)/(SPEED_OF_LIGHT**2)  ))**(1/2)  )
        
        #convert time pass to number of days
        time_pass = (dilation * time_travel) / SEC_TO_DAY
        
        print('An observer on Earth ages', "{0:.0f}".format(years) ,'year(s),', "{0:.0f}".format(days_leftover),'day(s) during the trip.')
        print('A passenger on the ship ages', "{0:.0f}".format(time_pass) ,'day(s) during the trip.')



#Quit
if choice == 4:
    print()

while choice < 1 or choice >4:
    #display menu
    print("Main menu: ")
    print("1. Warp Speed")
    print("2. Cost of Launch")
    print("3. Time Dilation")
    print("4. Exit")

    #choose from menu
    choice = int(input())
