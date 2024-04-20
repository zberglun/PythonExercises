#Excercises for 10_Functiond
#1
def tri_area(base,height):
    return 0.5*base*height
print(tri_area(4,10))

#2
def shape_area( l, w, shape_type = "triangle", ):
    if shape_type == "triangle":
        return tri_area(l,w)
    elif shape_type == "rectangle":
        return l*w
    else:
        print("Unfortunately I do not recognize that shape type")
        return ""
print(shape_area( 5,10, "rectangle"))
print(shape_area(5,10,"triangle"))
print(shape_area(5,10,"rhombus"))
print(shape_area(10,5))
#3
def print_pattern(num):
    for x in range(num+1):
        s = ""
        for i in range(x):
            s += "*"
        print(s)
print_pattern(4)
