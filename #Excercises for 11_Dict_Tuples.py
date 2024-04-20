import statistics as stats
import math
#Excercises for 11_Dict_Tuples
#1
def printData(dict):
    for i in range(len(dict.values())):
        print( f'{list(dict.keys())[i]}==>{list(dict.values())[i]}')

exit = False
country_pop = {"China" : 143 , "India" : 136, "USA" : 32, "Pakistan" : 21}
while not exit: 
    
    action = input("Please select an action: 'print' , 'add' , 'remove' , 'query' : ")
    if action == "print":
        printData(country_pop)
    if action == "add":
        countryname =input("Please enter a country you'd like to add: ")
        if countryname not in country_pop.keys():
            popadd = input("Please enter the population for that county: ")
            country_pop.update({countryname:popadd})
            printData(country_pop)
        else:
            print("This country already exists, please try again")
    if action == "remove":
        countryname =input("Please enter a country you'd like to remove: ")
        if countryname in country_pop.keys():
            country_pop.pop(countryname)
            printData(country_pop)
        else:
            print("That country doesn't exist")
    if action == "query":
        countryname =input("Please enter a country you'd like to lookup: ")
        if countryname in country_pop.keys():
            print(country_pop[countryname])
        else:
            print("That country doesn't exist")

    exit = input("Would you like to exit? y/n :")
    if exit == "y":
        exit = True
    else:
        exit = False


#2

exit = False
Stocks = {"info": [600,630,800] , "ril" : [1430,1490,1567], "mtl" :[234,180,160]}
def printData2(dict):
    for i in range(len(dict.values())):
        print( f'{list(dict.keys())[i]}==>{list(dict.values())[i]} ==> avg: {stats.mean(list(dict.values())[i])}')

while not exit:
    action = input("Please select an action: 'print' , 'add': ")
    if action == "print":
        printData2(Stocks)
    elif action == "add":
        newStockname = input("Please enter the name of the stock: ")
        if newStockname in Stocks.keys():
            flag_add = input("That stock already exists, you like to add a price? y/n:")
            if flag_add == "y":
                newPrice = int(input("Please enter the price to add: "))
                Stocks[newStockname].append(newPrice)
        else:
            newPrice = input("Please enter the prices to add with a comma between them:")
            prices = newPrice.split(",")
            prices = [int(x) for x in prices ]
            Stocks.update({newStockname : prices} )
    exit = input("Would you like to exit? y/n :")
    if exit == "y":
        exit = True
    else:
        exit = False 

#3
def circle_calc(radius):
    diameter = radius * 2
    area = math.pi * radius**2
    circumfrence = math.pi * diameter
    return area, circumfrence, diameter



a, c, d = circle_calc(int(input("Please enter the radius of the circle: ")))
print(f'The area is {a}, the circumfrence is {c}, and the diameter is {d}')


