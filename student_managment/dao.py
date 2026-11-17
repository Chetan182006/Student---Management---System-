
import mysql.connector

from model import Student


class StudentDAO:

    def connect(self):

        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Chetan@9352",
            database="student_db"
        )

    # Add Student

    def insert_student(self, student):

        con = self.connect()
        cursor = con.cursor()

        try:

            query = """
                INSERT INTO students
                (name, age, course, email, phone)
                VALUES (%s, %s, %s, %s, %s)
            """

            values = (
                student.get_name(),
                student.get_age(),
                student.get_course(),
                student.get_email(),
                student.get_phone()
            )

            cursor.execute(query, values)
            con.commit()

            return True

        except Exception:
            con.rollback()
            raise

        finally:
            cursor.close()
            con.close()

    # Display All Students

    def get_all_students(self):

        con = self.connect()
        cursor = con.cursor()

        try:

            query = "SELECT * FROM students ORDER BY id"

            cursor.execute(query)

            records = cursor.fetchall()

            return records

        finally:
            cursor.close()
            con.close()

    # Search Student

    def search_student(self, student_id):

        con = self.connect()
        cursor = con.cursor()

        try:

            query = "SELECT * FROM students WHERE id = %s"

            cursor.execute(query, (student_id,))

            record = cursor.fetchone()

            return record

        finally:
            cursor.close()
            con.close()

    # Update Student

    def update_student(self, student):

        con = self.connect()
        cursor = con.cursor()

        try:

            query = """
                UPDATE students
                SET name = %s,
                    age = %s,
                    course = %s,
                    email = %s,
                    phone = %s
                WHERE id = %s
            """

            values = (
                student.get_name(),
                student.get_age(),
                student.get_course(),
                student.get_email(),
                student.get_phone(),
                student.get_id()
            )

            cursor.execute(query, values)

            con.commit()

            return cursor.rowcount > 0

        except Exception:
            con.rollback()
            raise

        finally:
            cursor.close()
            con.close()

    # Delete Student

    def delete_student(self, student_id):

        con = self.connect()
        cursor = con.cursor()

        try:

            query = "DELETE FROM students WHERE id = %s"

            cursor.execute(query, (student_id,))

            con.commit()

            return cursor.rowcount > 0

        except Exception:
            con.rollback()
            raise

        finally:
            cursor.close()
            con.close()
