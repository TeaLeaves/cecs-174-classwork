#givens
brack_tax1 = 9525 * .10
brack_tax2 = 29175 * .12 
brack_tax3 = 43799 * .22
brack_tax4 = 75000 * .24
brack_tax5 = 42499 * .32
brack_tax6 = 300000 * .35
brack_tax7 = 9500000 * .37
#label tax income
tax_income = int(input("Please enter your 2018 taxable income: "))

#code for 10%
if tax_income > 0 and tax_income <= 9525:
    brack_tax = tax_income * .10
    total_tax = brack_tax
    tax_owe = (total_tax / tax_income) * 100
    print("Your tax liability: $", "{0:.2f}".format(total_tax),"for an effective tax rate of ", "{0:.1f}".format(tax_owe), "%")
    
#code for 12%
elif tax_income > 9525 and tax_income <= 38700:
    brack_tax = (tax_income - 9525) * .12
    total_tax = brack_tax + brack_tax1
    tax_owe = (total_tax / tax_income) * 100
    print("Your tax liability: $", "{0:.2f}".format(total_tax),"for an effective tax rate of ", "{0:.1f}".format(tax_owe), "%")
    
#code for 22%
elif tax_income > 38700 and tax_income <= 82500:
    brack_tax = (tax_income - 9525 - 29175) * .22
    total_tax = brack_tax + brack_tax1 + brack_tax2
    tax_owe = (total_tax / tax_income) * 100
    print("Your tax liability: $", "{0:.2f}".format(total_tax), "for an effective tax rate of ", "{0:.1f}".format(tax_owe), "%")

#code for 24%
elif tax_income > 82500 and tax_income <= 157500:
    brack_tax = (tax_income - 9525 - 29175 - 43799) * .24
    total_tax = brack_tax + brack_tax1 + brack_tax2 + brack_tax3
    tax_owe = (total_tax / tax_income) * 100
    print("Your tax liability: $", "{0:.2f}".format(total_tax), "for an effective tax rate of ", "{0:.1f}".format(tax_owe), "%")

#code for 32%
elif tax_income > 157500 and tax_income <= 200000:
    brack_tax = (tax_income - 9525 - 29175 - 43799 - 75000) * .32
    total_tax = brack_tax + brack_tax1 + brack_tax2 + brack_tax3 + brack_tax4
    tax_owe = (total_tax / tax_income) * 100
    print("Your tax liability: $", "{0:.2f}".format(total_tax), "for an effective tax rate of ", "{0:.1f}".format(tax_owe), "%")

#code for 35%
elif tax_income > 200000 and tax_income <= 500000:
    brack_tax = (tax_income - 9525 - 29175 - 43799 - 75000 - 42500) * .35
    total_tax = brack_tax + brack_tax1 + brack_tax2 + brack_tax3 + brack_tax4 + brack_tax5
    tax_owe = (total_tax / tax_income) * 100
    print("Your tax liability: $", "{0:.2f}".format(total_tax), "for an effective tax rate of ", "{0:.1f}".format(tax_owe), "%")

#code for 37%
elif tax_income > 500000 and tax_income <= 10000000:
    brack_tax = (tax_income - 9525 - 29175 - 43799 - 75000 - 42500 - 300000) * .37
    total_tax = brack_tax + brack_tax1 + brack_tax2 + brack_tax3 + brack_tax4 + brack_tax5 + brack_tax6
    tax_owe = (total_tax / tax_income) * 100
    print("Your tax liability: $", "{0:.2f}".format(total_tax), "for an effective tax rate of ", "{0:.1f}".format(tax_owe), "%")
    
#code for 70%
else:
    brack_tax = (tax_income - 9525 - 29175 - 43799 - 75000 - 42500 - 300000 - 9500000) * .7
    total_tax = brack_tax + brack_tax1 + brack_tax2 + brack_tax3 + brack_tax4 + brack_tax5 + brack_tax6 + brack_tax7
    tax_owe = (total_tax / tax_income) * 100
    #code for 37%
    brack_tax37 = (tax_income - 9525 - 29175 - 43799 - 75000 - 42500 - 300000 - 9500000) * .37
    total_tax37 = brack_tax37 + brack_tax1 + brack_tax2 + brack_tax3 + brack_tax4 + brack_tax5 + brack_tax6 + brack_tax7
    tax_owe37 = (total_tax37 / tax_income) * 100
    #output
    print("You tax liability is: $", "{0:.2f}".format(total_tax37))
    print("Your effective tax rate is: ","{0:.1f}".format(tax_owe37))
    print("")
    print("Your tax liability with the new 70% bracket: $", "{0:.2f}".format(total_tax), "for an effective tax rate of ", "{0:.1f}".format(tax_owe), "%")

print("")
print("")
print("Mean (average) salary for a Software Engineer living in the Los Angeles,CA area: $100,614.00")
print("(Approximate) percentage of $10,000,000: 1.006%")
print("In this class of 84 students, how many do you think will ever earn an annual income of more than $10,000,000: 0 or 1")
