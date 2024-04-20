#Exercises for 22 List_det_dict comprehensions
#1 create the below
integer_ex = [0, 1, 2, 3, 4]
binary_ex = ["0", "1", "10", "11", "100"]
binary_dict_ex = {0:"0", 1:"1", 2:"10", 3: "11", 4:"100"}

ints = range(11)
binary = [bin(x) for x in ints] #Use list comprehension to convert the list into binary
binary_dict = { k:v for k,v in zip(ints, binary)} #Not sure if the zip object is needed or not
print(binary_dict)
print(binary)
print(ints)

#2 create a list such that a+i = 0, where i is an index of a given list and a is the output index 
list = range(10)
inverse_list = [a*-1 for a in list ]
print(inverse_list)

#3 create a set which only contains squares from a given list


list_2 = range(10)
squareset = { x*x for x in list_2}
print(squareset)