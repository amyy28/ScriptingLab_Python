class Student:
	def __init__(self, name, age, marks):
		self.name = name
		self.age = age
		self.marks = marks

	def display(self):
		print("My name is", self.name)
		print("My age is", self.age)
		print("My marks are", self.marks)

p1 = Student("Aman",20,[100, 99, 100])
p1.display()
print("Enter your custom values")
def accept():
	name = input("Enter your name")
	age = input("Enter your age")
	marks = input("Enter your marks")
	p2 = Student(name, age, marks)
	p2.display()
accept()
