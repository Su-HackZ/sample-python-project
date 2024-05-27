from database import Database

class Course:
    def __init__(self, course_id, name, db_config):
        self.id = course_id
        self.name = name
        self.db = Database(**db_config)
        self.students = []

    def add_student(self, student):
        query = "SELECT * FROM enrollments WHERE student_id = %s AND course_id = %s"
        result = self.db.execute(query, (student.id, self.id))
        if not result:
            query = "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)"
            self.db.execute(query, (student.id, self.id))
            self.students.append(student)
        else:
            print(f"Student with ID {student.id} is already enrolled in course {self.id}.")

    def get_students(self):
        query = """
        SELECT s.student_id, s.name
        FROM students s
        JOIN enrollments e ON s.student_id = e.student_id
        WHERE e.course_id = %s
        """
        return self.db.execute(query, (self.id,))
