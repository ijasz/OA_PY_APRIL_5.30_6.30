class University:
    univName= "pondy university"
    def getUniversityDetails(self):
        print("univName", self.univerName)

class Course(University):
    courseName = "CSE"
    def getUniversityDetails(self):
        print("courseName", self.courseName)

class Batch(Course):
    batchName = 2023
    def getUniversityDetails(self):
        print("batchName", self.batchName)

class Department(Course, University):
    departmentName = "Computer Science"
    def getUniversityDetails(self):
        print("departmentName", self.departmentName)

    

obj = Department()
obj1 = Batch()

obj.getUniversityDetails()



