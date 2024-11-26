# class Vehicle:
# 	def __init__(self, name, mileage, capacity):
# 		self.name = name
# 		self.mileage = mileage
# 		self.capacity = capacity


# 	def fare(self):
# 		return self.capacity * 10


# class Taxi(Vehicle):
# 	def fare(self):
# 		amount = super().fare()
# 		amount += amount * 10 / 100
# 		return amount

# Taxi_car = Taxi("BMW", 12, 50)
# print("Total fare is: ", Taxi_car.fare())


# class People():
# 	def __init__(self, name):
# 		self.name = name

# 	def namePrint(self):
# 		print(self.name)


# person1 = People("Marvin")
# person2 = People("Rachel")
# person1.namePrint()




# class Student:
# 	def __init__(self, student_id, student_name, student_class):
# 		self.student_id = student_id
# 		self.student_name = student_name
# 		self.student_class = student_class

# 	def display(self):
# 		return f"Student ID: {self.student_id} | Student Name: {self.student_name} | Class: {self.student_class}"

# wilson_median = Student('S122', 'wilson Median', 'VI')
# print(wilson_median.display())



class py_solution:
	def int_to_Roman(self, num):
		val = [
		1000, 900, 500, 400,
		100, 90, 50, 40, 
		10, 9, 5, 4,
		1
		]

		syb = [
		"M", "CM", "D", "CD",
		"C", "XC", "L", "XL",
		"X", "IX", "V", "IV",
		"I"
		]

		roman_num = ""
		i = 0
		while num > 0:
			for _ in range(num // val[i]):
				roman_num += syb[i]
				num -= val[i]
			i += 1
		return roman_num

print(py_solution().int_to_Roman(1))

print(py_solution().int_to_Roman(4000))






# class Cat:
# 	def sleep(self):
# 		return "*sleeping*"

# 	def speak(self):
# 		return "Meow!"

# 	def eat(self):
# 		return "*hunting*"

# 	def hunt(self):
# 		return "*hunting*"


# class Persian(Cat):
# 	def talk(self):
# 		return super().speak()

# kitty = Persian()
# print(kitty.talk())



# class People():
# 	def __init__(self, name):
# 		self.name = name

# 	def namePrint(self):
# 		print(self.name)


# person1 = People("Marvin")
# person2 = People("Rachel")
# person1.namePrint()
# person2.namePrint()



# class Dog:
# 	def walk(self):
# 		return "*walking*"

# 	def speak(self):
# 		return "wolf!"


# class Jackrussel(Dog):
# 	def speak(self):
# 		return "Arff!"

# bobo = Jackrussel()
# print(bobo.walk())




# def student(id, name, cluss):
# 	return f"student ID: {id}\nname:{name}\nClass:{cluss}"


# print(student('s122', 'wilson', 'vi'))




# class SoftwareEngineer:
# 	alia = "Keyboard Magic"


# def _init_(self, name, age, level, salary);