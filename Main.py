#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Tip Calulator")
bill=round(int(input("What is your bill : ")))
num_people=round(int(input("How Many people are you splitting with : ")))
percent_tip=round(int(input("What tip would you like to leave 10%, 12%,15%: ")))

tip=round((bill*(percent_tip/100)/num_people))
print("Your portion of the bill is : "+str(tip))
