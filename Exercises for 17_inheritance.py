# Exercises for 17_inheritance
class Animal:
    def __init__(self, home: str ) -> None:
        self.habitat = home
    def displayHabitat(self) -> None:
        print(self.habitat)
    def sound(self) -> None:
        print("Some animal sound")


class Dog(Animal):
    def __init__(self) -> None:
        super().__init__("kennel")
    def sound(self) -> None:
        print("Woof, Woof")
    
if __name__ == "__main__":
    x = Dog()
    x.displayHabitat()
    x.sound()
    y = Animal("Caves")
    y.sound()