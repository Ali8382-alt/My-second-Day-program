class Employee:
    def __init__(self, name, position, department, salary, age, contact, city):
        self.name = name
        self.position = position
        self.department = department
        self.salary = salary
        self.age = age
        self.contact = contact
        self.city = city
    
    def Personal_Details(self):
        print("(personal Details)")
        print("Name:", self.name)
        print("position:", self.position)
        print("Department:", self.department)
        print("Age:", self.age)
        print("Contact:", self.contact)
        print("City:", self.city)

    def Salary_Details(self):
        print("(Salary Details)")
        print("Salary:", self.salary)

E1 = Employee("Mr. Khan", "Manger", "Sales", 85000, 45, +923001234567, "Faisalabad")

E1.Personal_Details()
E1.Salary_Details()
