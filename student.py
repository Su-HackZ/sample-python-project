class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)
