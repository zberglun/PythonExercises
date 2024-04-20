#Exercises for Raise, Exception, and Finally
#1

class AdultException(Exception):
    pass

class Person():
    def __init__(self,name: str ,age: int) -> None:
        self.name: str = name
        self.age: int = age
    
    def get_minor_age(self) -> int:
        """
        This function will return the person's age if they are a minor. If they are not,
        it will instead throw an error and return the actual age
        :return: age
        """
        
        if self.age >= 18:
            raise AdultException
        else:
            return self.age
        

    def display_person(self) -> None:
        try:
            print(f"age ->  {self.get_minor_age()}")
        except AdultException:
            print("This person is an adult")
        finally:
            print(f"Name -> {self.name}")
if __name__ == "__main__":
    bob = Person("Bob", 21)
    bob.display_person()
    hector = Person("Hector", 16)
    hector.display_person()
