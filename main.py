from school import School
from student import Student
from course import Course

def main():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Pass@123',  # replace with your MySQL password
        'database': 'school_management'
    }

    # Create a school
    my_school = School("Springfield High School", db_config)

    # Create some students
    student1 = Student(1, "John Doe")
    student2 = Student(2, "Jane Smith")

    # Create some courses
    course1 = Course(101, "Mathematics", db_config)
    course2 = Course(102, "Science", db_config)

    # Add students to the school
    my_school.add_student(student1)
    my_school.add_student(student2)

    # Add courses to the school
    my_school.add_course(course1)
    my_school.add_course(course2)

    # Enroll students in courses
    student1.enroll(course1)
    student1.enroll(course2)
    student2.enroll(course1)

    # Display school information
    print(f"School: {my_school.name}")
    print("\nStudents:")
    for student in my_school.get_students():
        print(f"{student[0]}: {student[1]}")

    print("\nCourses:")
    for course_id, course_name in my_school.get_courses():
        print(f"{course_id}: {course_name}")
        course = Course(course_id, course_name, db_config)  # Instantiate a Course object
        print("Enrolled students:")
        for student in course.get_students():
            print(f" - {student[1]}")

if __name__ == "__main__":
    main()
