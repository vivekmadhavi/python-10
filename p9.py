#wapp to class student + exception handle


class Student:
	def __init__(self,roll,name,marks):
		self.roll=roll
		self.name=name
		self.marks=marks
	def show(self):
		print("roll",self.roll)
		print("name",self.name)
		print("marks",self.marks)


try:
	r=int(input("enter the roll number"))
	if r <= 0:
		raise Exception("enter positive number only")
		
	f=input("enter the first name")
	if not f.isalpha():
		raise Exception("enter the name only")
	l=input("enter the last name")
	if not l.isalpha():
		raise Exception("enter the name only")
	n= f +" "+ l
	m=int(input("enter the marks"))
	if m < 0 or m > 100:
		raise Exception("marks should be between 0 to 100")


	s=Student(r,n,m)
	s.show()
except ValueError:
	print("enter interger only")

except Exception as e:
	print(e)