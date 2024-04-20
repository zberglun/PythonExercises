#Exercises for 9_For_Loops
#1
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for x in result:
    if x == "heads":
        count += 1
#2
print([x**2 for x in range(10) if x%2 != 0 ])
#not quite for loop but more compact and legible
#3
month_list = ["January", "Febuary", "March" , "April" , "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
foundexpense = False
exp_amount = int(input("Please enter an expense amount to lookup: "))
for i in range(len(expense_list)):
    if exp_amount == expense_list[i]:
        foundexpense = True
        month = month_list[i]
if foundexpense:
    print(f'The expense {exp_amount} was found as the month of {month}')
else:
    print(f'Unfortunately the amount of {exp_amount} was not found as an expense')

#4
for km in range(5):
    tired = input("Are you tired yet? yes/no:")
    if tired == "yes":
        print("You didn't finish the race")
        break
    elif km == 4:
        print("Congrats!!! You finished the race")
#5
for star in range(5):
    s = ""
    for temp in range(star):
        s+= "*"
    print(s)

    
        
