#Exercises for 8_If_Statements
#1
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
cityname = input("Which city would you like to look up the country for?: ")
if cityname in india:
    print(f'The city {cityname} is in India.')
elif cityname in pakistan:
    print(f'The city {cityname} is in Pakistan')
elif cityname in bangladesh:
    print(f'The city {cityname} is in Bangladesh')
else:
    print(f'Unfortunately i do not know where {cityname} is located, try again without whitespaces or other characters if you believe i should know where it is located')

cityname1 = input("What is the first city you would like to check is in the same country?: ")
cityname2 = input("What is the second city you would like to check is in the same country?: ")
if cityname1 in india and cityname2 in india :
    print("Both cities are in India")
elif cityname1 in pakistan and cityname2 in pakistan:
    print("Both cities are in India")
elif cityname1 in bangladesh and cityname2 in bangladesh:
    print("Both cities are in Bangladesh")
else:
    print("They don't belong to the same country")


#2
sugar_level= input("Please enter your fasting sugar level: ")
sugar_level = float(sugar_level)

if sugar_level < 80:
    print("Your sugar level is low")
elif sugar_level >100:
    print("Your sugar level is too high")
else:
    print("Your sugar is normal") 
    