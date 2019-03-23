
#input for price
CAR_PRICE = float(input("Enter the original price of the automobile: "))
#validate price
while CAR_PRICE <= 0:
    CAR_PRICE = float(input("Enter the original price of the automobile: "))



#input for years
NUM_YRS = int(input("Enter number of years: "))
#validate years
while NUM_YRS <= 0:
    NUM_YRS = int(input("Enter number of years: "))

#Starting yr(global val)
YEAR = 0
#formulas
for YEAR in range(YEAR+1,NUM_YRS+1):
    CAR_PRICE = CAR_PRICE - (CAR_PRICE * 0.18)
    print('Year', YEAR, 'value: ', '$','{0:,.2f}'.format(CAR_PRICE))
    YEAR+=1


print('')
print('')
print('')
print('')
print('')


print('Research Question:')
print('If my new car is worth $40,619')
print('In 1 year my car would be worth: 40619 - (40619*0.8) = $33,307.58')
print('In 2 years my car would be worth: 33307.58 - (33307.58*0.8) = $27,312.22')
print('In 3 years my car would be worth: 27312.22 - (27312.22*0.8) = $22,396.02')
print('In 4 years my car would be worth: 220396.02 - (220396.02*0.8) = $18.365,74')
print('So in 4 years my car would be worth less than half of its inital worth.')
print('')
print('ps: half of $40,619 is $20,309.50')
