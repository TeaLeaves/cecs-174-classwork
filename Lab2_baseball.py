#get name
name = input("Hello. What is your name? Please input your full name:  ")

#get info
plate_app = int(input("How many Plate Appearances have you made?  "))
bats = int(input("How many At Bats?  "))
walks = int(input("How many Walks? "))
#get info bout bases/runs
singles = int(input("How many Singles?  "))
doubles = int(input("How many Doubles?  "))
triples = int(input("How many Triples?  "))
home_runs = int(input("How many Home Runs?  "))

#space just to be clean
print("")
#end of recieving info
print("Thank you for the information.")

#calculate info
num_hits = singles + doubles + triples + home_runs
bat_avg = num_hits / bats
slugg = ( (singles)+(doubles*2)+(triples*3)+(home_runs*4) ) / (bats)
on_base = (num_hits + walks) / plate_app
ops = on_base + slugg



#double space just to be clean
print("")
print("")

#output info
print(name, "had: ")
print(num_hits, "hits")
print("{0:.3f}".format(bat_avg), "batting AVG")
print("{0:.3f}".format(slugg), "SLG")
print("{0:.3f}".format(ops), "OPS")

#spaces to be clean
print("")
print("")

#research questions
print("What baseball player has the all-time, highest career OPS statistic? Babe Ruth")
print("What baseball player has the highest career OPS statistic among active players? Mike Trout")
print("For more info go to: https://www.baseball-reference.com/leaders/onbase_plus_slugging_career.shtml")
