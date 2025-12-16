print("Welcome to My Tip Calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10 12 15"))
people = int(input("how many people are there?"))

tipAsPercent = tip / 100
totalTipAmount = bill * tipAsPercent
totalBill = bill + totalTipAmount
billPerPerson = totalBill / people
finalAmount = round(billPerPerson,2)

print(f"Each person must be pay ${finalAmount}")
