class Course:
  def __init__(self, course_name, course_code):
    self.course_name = course_name
    self.course_code = course_code

  def Course_info(self):
    print("Course_Name:",self.course_name)
    print("Course_Code:",self.course_code)

class Teacher(Course):
  def __init__(self, name, Id, course_name, course_code):
    Course.__init__(self,course_name, course_code)
    
    self.name = name
    self.Id = Id
    
  def Teacher_info(self):
        print("Teacher_Name:", self.name)
        print("Teacher_ID:", self.Id)
        self.Course_info()
        print()
    
t1 = Teacher("Usman Khan", 501, ("Python Programming","Data Bases"), ("CS142","CS150") )
t2 = Teacher("Umer Khan", 508, ("Computer Networking","Data Manipulation"), ("CS505","CS508") )
t3 = Teacher("Ali Ahmed", 509, ("Data Structures","Data Collection"), ("CS303","CS408") )
t4 = Teacher("Sara Malik", 510, ("Web Development","Artification Intelligence"), ("CS404","CS406") )

t1.Teacher_info()
t2.Teacher_info()
t3.Teacher_info()
t4.Teacher_info()