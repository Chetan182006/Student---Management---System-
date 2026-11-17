
import tkinter as tk
from tkinter import ttk, messagebox

from controller import StudentController


class StudentView:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1000x650")
        self.root.resizable(False, False)

        self.controller = StudentController()

        self.selected_id = None

        self.create_widgets()
        self.display_students()

    # Create GUI

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="STUDENT MANAGEMENT SYSTEM",
            font=("Arial", 22, "bold"),
            bg="#022FD0",
            fg="white",
            pady=15
        )

        title.pack(fill="x")

        main_frame = tk.Frame(
            self.root,
            padx=20,
            pady=15
        )

        main_frame.pack(fill="both", expand=True)

        # Form Frame

        form_frame = tk.LabelFrame(
            main_frame,
            text="Student Details",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=15
        )

        form_frame.pack(fill="x")

        # Variables

        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.course_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.search_var = tk.StringVar()

        # Name

        tk.Label(form_frame, text="Name").grid(
            row=0, column=0, padx=10, pady=10
        )

        tk.Entry(
            form_frame,
            textvariable=self.name_var,
            width=30
        ).grid(row=0, column=1, padx=10, pady=10)

        # Age

        tk.Label(form_frame, text="Age").grid(
            row=0, column=2, padx=10, pady=10
        )

        tk.Entry(
            form_frame,
            textvariable=self.age_var,
            width=30
        ).grid(row=0, column=3, padx=10, pady=10)

        # Course

        tk.Label(form_frame, text="Course").grid(
            row=1, column=0, padx=10, pady=10
        )

        tk.Entry(
            form_frame,
            textvariable=self.course_var,
            width=30
        ).grid(row=1, column=1, padx=10, pady=10)

        # Email

        tk.Label(form_frame, text="Email").grid(
            row=1, column=2, padx=10, pady=10
        )

        tk.Entry(
            form_frame,
            textvariable=self.email_var,
            width=30
        ).grid(row=1, column=3, padx=10, pady=10)

        # Phone

        tk.Label(form_frame, text="Phone").grid(
            row=2, column=0, padx=10, pady=10
        )

        tk.Entry(
            form_frame,
            textvariable=self.phone_var,
            width=30
        ).grid(row=2, column=1, padx=10, pady=10)

        # Buttons Frame

        button_frame = tk.Frame(main_frame, pady=15)

        button_frame.pack(fill="x")

        tk.Button(
            button_frame,
            text="Add Student",
            width=15,
            bg="green",
            fg="white",
            command=self.add_student
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="Update Student",
            width=15,
            bg="blue",
            fg="white",
            command=self.update_student
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="Delete Student",
            width=15,
            bg="red",
            fg="white",
            command=self.delete_student
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="Clear",
            width=12,
            command=self.clear_fields
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="Refresh",
            width=12,
            command=self.display_students
        ).pack(side="left", padx=5)

        # Search Frame

        search_frame = tk.Frame(
            main_frame,
            pady=10
        )

        search_frame.pack(fill="x")

        tk.Label(
            search_frame,
            text="Search Student ID:",
            font=("Arial", 11)
        ).pack(side="left", padx=5)

        tk.Entry(
            search_frame,
            textvariable=self.search_var,
            width=20
        ).pack(side="left", padx=5)

        tk.Button(
            search_frame,
            text="Search",
            command=self.search_student
        ).pack(side="left", padx=5)

        # Table Frame

        table_frame = tk.LabelFrame(
            main_frame,
            text="Student Records",
            font=("Arial", 12, "bold")
        )

        table_frame.pack(fill="both", expand=True)

        columns = (
            "id",
            "name",
            "age",
            "course",
            "email",
            "phone"
        )

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=12
        )

        self.table.heading("id", text="ID")
        self.table.heading("name", text="Name")
        self.table.heading("age", text="Age")
        self.table.heading("course", text="Course")
        self.table.heading("email", text="Email")
        self.table.heading("phone", text="Phone")

        self.table.column("id", width=50)
        self.table.column("name", width=140)
        self.table.column("age", width=70)
        self.table.column("course", width=140)
        self.table.column("email", width=220)
        self.table.column("phone", width=130)

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.table.yview
        )

        self.table.configure(
            yscrollcommand=scrollbar.set
        )

        self.table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # Table Selection Event

        self.table.bind(
            "<<TreeviewSelect>>",
            self.select_student
        )

    # Get Form Data

    def get_form_data(self):

        name = self.name_var.get().strip()
        age = self.age_var.get().strip()
        course = self.course_var.get().strip()
        email = self.email_var.get().strip()
        phone = self.phone_var.get().strip()

        if not all([name, age, course, email, phone]):

            messagebox.showwarning(
                "Validation",
                "Please fill all fields!"
            )

            return None

        try:

            age = int(age)

            if age <= 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Invalid Age",
                "Please enter a valid positive age!"
            )

            return None

        return name, age, course, email, phone

    # Add Student

    def add_student(self):

        data = self.get_form_data()

        if data is None:
            return

        try:

            result = self.controller.add_student(*data)

            if result:

                messagebox.showinfo(
                    "Success",
                    "Student Added Successfully!"
                )

                self.clear_fields()
                self.display_students()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # Display Students

    def display_students(self):

        try:

            records = self.controller.display_students()

            for item in self.table.get_children():
                self.table.delete(item)

            for record in records:

                self.table.insert(
                    "",
                    "end",
                    values=record
                )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # Search Student

    def search_student(self):

        try:

            student_id = int(self.search_var.get())

            if student_id <= 0:
                raise ValueError

            record = self.controller.search_student(student_id)

            if record:

                # Find existing row in table

                for item in self.table.get_children():

                    values = self.table.item(item, "values")

                    if int(values[0]) == student_id:

                        self.table.selection_set(item)
                        self.table.focus(item)
                        self.table.see(item)

                        return

                # If row is not present, refresh table

                self.display_students()

                for item in self.table.get_children():

                    values = self.table.item(item, "values")

                    if int(values[0]) == student_id:

                        self.table.selection_set(item)
                        self.table.focus(item)
                        self.table.see(item)

                        return

            else:

                messagebox.showwarning(
                    "Not Found",
                    "Student Not Found!"
                )

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Enter a valid Student ID!"
            )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # Select Student

    def select_student(self, event):

        selected = self.table.selection()

        if selected:

            record = self.table.item(
                selected[0],
                "values"
            )

            self.selected_id = int(record[0])

            self.name_var.set(record[1])
            self.age_var.set(record[2])
            self.course_var.set(record[3])
            self.email_var.set(record[4])
            self.phone_var.set(record[5])

    # Update Student

    def update_student(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Selection",
                "Please select a student from the table!"
            )

            return

        data = self.get_form_data()

        if data is None:
            return

        try:

            result = self.controller.update_student(
                self.selected_id,
                *data
            )

            if result:

                messagebox.showinfo(
                    "Success",
                    "Student Updated Successfully!"
                )

                self.clear_fields()
                self.display_students()

            else:

                messagebox.showwarning(
                    "Not Found",
                    "Student Not Found!"
                )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # Delete Student

    def delete_student(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Selection",
                "Please select a student!"
            )

            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this student?"
        )

        if confirm:

            try:

                result = self.controller.delete_student(
                    self.selected_id
                )

                if result:

                    messagebox.showinfo(
                        "Success",
                        "Student Deleted Successfully!"
                    )

                    self.clear_fields()
                    self.display_students()

                else:

                    messagebox.showwarning(
                        "Not Found",
                        "Student Not Found!"
                    )

            except Exception as e:

                messagebox.showerror(
                    "Database Error",
                    str(e)
                )

    # Clear Fields

    def clear_fields(self):

        self.name_var.set("")
        self.age_var.set("")
        self.course_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.search_var.set("")

        self.selected_id = None

        for item in self.table.selection():
            self.table.selection_remove(item)
