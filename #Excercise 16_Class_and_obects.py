#Excercise 16_Class_and_obects
class employee:
    def __init__(self,id_num : int,name_ :str):    
        self.id : int = id_num
        self.name : str = name_
    def display(self):
        try:
            print(self.id)
        except AttributeError:
            print("ID does not exist")
        print(self.name)
if __name__ == "__main__" :
    emp = employee(1,"coder")
    emp.display()
    del emp.id
    emp.display()
    del emp
    try:
        print(emp)
    except NameError:
        print("emp does not exist")
    