#Exercises for 5_lists
#1
Expenses = [2200,2350,2600,2130,2190]
print(f'I spent {Expenses[1]-Expenses[0]} dollars more in febuary than in january')
print(f'I spent {sum(Expenses[0:3])} in the first three months')
spent2000 = 2000 in Expenses 
print("Did i spend 2000 dollars exactly in any month?: ",spent2000)
Expenses.append(1980)
Expenses[3]=Expenses[3]-200
#2
heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
len(heroes)
heroes.append('black panther')
print(heroes)
heroes.remove('black panther')
heroes.insert(3,'black panther')
print(heroes)
heroes[1:3] = ['doctor strange']
print(heroes)
heroes.sort()
print(heroes)