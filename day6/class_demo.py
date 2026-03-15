class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)


print(p1.name)
print(p1.age)

p1.greet()

class Student(Person):
    pass

p2 = Student("Lisa", 26)
print(p2.name)

