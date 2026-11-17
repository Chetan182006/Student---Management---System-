
from model import Student
from dao import StudentDAO


class StudentController:

    def __init__(self):

        self.dao = StudentDAO()

    # Add Student

    def add_student(self, name, age, course, email, phone):

        student_obj = Student(
            None,
            name,
            age,
            course,
            email,
            phone
        )

        return self.dao.insert_student(student_obj)

    # Display Students

    def display_students(self):

        return self.dao.get_all_students()

    # Search Student

    def search_student(self, student_id):

        return self.dao.search_student(student_id)

    # Update Student

    def update_student(self, student_id, name, age, course, email, phone):

        student_obj = Student(
            student_id,
            name,
            age,
            course,
            email,
            phone
        )

        return self.dao.update_student(student_obj)

    # Delete Student

    def delete_student(self, student_id):

        return self.dao.delete_student(student_id)
