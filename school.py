from database import Database
import mysql.connector

class School:
    def __init__(self, name, db_config):
        self.name = name
        self.db = Database(**db_config)
        self.students = []
        self.courses = []

    def add_student(self, student):
        query = "SELECT student_id FROM students WHERE student_id = %s"
        result = self.db.execute(query, (student.id,))
        if not result:
            query = "INSERT INTO students (student_id, name) VALUES (%s, %s)"
            self.db.execute(query, (student.id, student.name))
            self.students.append(student)
        else:
            print(f"Student with ID {student.id} already exists.")

    def add_course(self, course):
        query = "SELECT course_id FROM courses WHERE course_id = %s"
        result = self.db.execute(query, (course.id,))
        if not result:
            query = "INSERT INTO courses (course_id, title) VALUES (%s, %s)"
            self.db.execute(query, (course.id, course.name))
            self.courses.append(course)
        else:
            print(f"Course with ID {course.id} already exists.")

    def get_students(self):
        query = "SELECT student_id, name FROM students"
        return self.db.execute(query)

    def get_courses(self):
        query = "SELECT course_id, title FROM courses"
        return self.db.execute(query)
