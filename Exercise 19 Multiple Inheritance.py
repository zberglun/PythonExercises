#Exercise 19 Multiple Inheritance
#1
class Teacher:
    def teacherAction(self)-> None:
        print("I teach")
class Student:
    def studentAction(self) -> None:
        print("I learn")
class Youtuber:
    def youtuberAction(self) -> None:
        print("I make videos")

class Person(Teacher, Student, Youtuber):
    pass

if __name__ == "__main__":
    X = Person()
    X.studentAction()
    X.teacherAction()
    X.youtuberAction()