
class TooManyStudentsError(Exception):
    pass

class ClassRoom:
    def __init__(self, teacher, students, course_title):
        self.teacher = teacher
        self.students = students
        self.course_title = course_title
        
    def add_student(self, student):
        if len(self.students) >= 20:
            raise TooManyStudentsError("Classroom is full")
        else:
            self.students.append(student)            
            
    def remove_student(self, student_to_remove):
        self.students = [student for student in self.students if student.name != student_to_remove.name]
            
    def change_teacher(self, new_teacher):
        self.teacher = new_teacher
        
class Person:
    def __init__(self, name):
        self.name = name
        
class Teacher(Person):
    pass

class Student(Person):
    pass
