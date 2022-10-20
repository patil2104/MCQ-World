class Student:
    """
    properties:
    id, name, age, marks for maths, science, english, total, percentage, status, grade.
    Functions:
    1. setData()- to set the data for students (id, name,age, marks for maths, science, english)
    2. calculateAcademicData()- to calculate total marks, percentage, status and grade.
    """
    
    def addData(self):
        """
        Asking user for id, name, age and marks
        """
        id: int=-1
        while id < 0:
            inp: str = input("Enter student id:\t\t")
            if not inp.isnumeric(): continue
            id = int(inp)
            
        name: str = ""
        while name.__len__()<2:
            inp: str=input("Enter student name:\t\t")
            if inp.__len__()<2:
                print("Student name must be in 2 or more characters.")
                continue
            name=inp 
            
        age: int=-1
        while age < 0:
            inp: str = input("Enter student age:\t\t")
            if not inp.isnumeric(): continue
            age = int(inp)
            
        maths_marks: int=-1
        while maths_marks < 0 or maths_marks > 100:
            inp: str = input("Enter marks for Maths:\t\t")
            if not inp.isnumeric(): continue
            maths_marks = int(inp)
            
        science_marks: int=-1
        while science_marks < 0 or science_marks > 100:
            inp: str = input("Enter marks for Science:\t\t")
            if not inp.isnumeric(): continue
            science_marks = int(inp)
            
        english_marks: int=-1
        while english_marks < 0 or english_marks > 100:
            inp: str = input("Enter marks for English:\t\t")
            if not inp.isnumeric(): continue
            english_marks = int(inp)
            
        marks: map={
            "maths_marks": maths_marks,
            "science_marks": science_marks,
            "english_marks": english_marks
        }
        
        self.setData(id=id, name=name, age=age, marks=marks)
        
        
    def setData(self, id: int, name: str, age: int, marks: map):
        self.id: int =  id
        self.name: str =  name
        self.age: int =  age
        self.marks: map =  marks
        
    def calculateAcademicData(self):
        marks: map = self.marks
        
        self.total: int = marks["maths_marks"] + marks["science_marks"] + marks["english_marks"]
        self.percentage: float = (self.total * 100) / 300
        self.status: str = "PASS"
        for _, mark in marks.items():
            if mark <= 50: self.status = "FAIL"
            
        self.grade: str = "No"
        if self.percentage >= 75:
            self.grade = "A"
        elif 60 <= self.percentage < 75:
            self.grade = "B"
        elif 50 <= self.percentage < 60:
            self.grade = "C"
            
    def getData(self) -> map:
        data: map = {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "marks": self.marks,
            "total": self.total,
            "percentage": self.percentage,
            "status": self.status,
            "grade": self.grade
        }
        return data
    
    def showData(self):
        data: map = self.getData()
        
        print("\nID:\t\t", data["id"])
        print("Name:\t\t", data["name"])
        print("Age:\t\t", data["age"])
        print("Maths Marks:\t", data["marks"]["maths_marks"])
        print("Science Marks:\t", data["marks"]["science_marks"])
        print("English Marks:\t", data["marks"]["english_marks"])
        print("Total:\t\t", data["total"])
        print("Percentage:\t", data["percentage"])
        print("Status:\t\t", data["status"])
        print("Grade:\t\t", data["grade"])
        
student: Student = Student()
student.addData()
student.calculateAcademicData()
student.showData()


        
        
