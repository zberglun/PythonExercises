#Exercises for 4_Strings
#1
Street, City, Country  = "Main St., ", "Springfield, ", "USA"
address = Street +'\n'+ City+'\n' + Country
print("Address using + is: ",address)
address2 = f'{Street}\n{City}\n{Country}'
print("Address using f notation is: ", address2)
#2
fact = "Earth revolves around the sun"
print(fact[6:14])
print(fact[-3:])
#3
num_veg = 2
num_fruit = 3
print(f'I eat {num_veg} veggies and {num_fruit} fruits daily')
s= 'maine 200 banana khaye'
s= s.replace("200", "10").replace("banana", "samosa")
print("Using one line to replace:", s)