import tkinter as tk  # Importing Tkinter for GUI
from tkinter import messagebox  # Importing messagebox for popup messages
from tkinter import ttk  # Importing ttk for the Treeview table

class StudentGradeSystem:
    def __init__(self, root):
        """Initialize the main GUI window."""
        self.root = root
        self.root.title("Student Grade Management System")  # Window title
        self.root.geometry("500x400")  # Window size (width x height)

        # Dictionary to store student data (student_id: {"name": name, "grade": grade})
        self.students = {}

        # Labels and Entry Fields for Student Data Input
        tk.Label(root, text="Student ID:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_id = tk.Entry(root)  # Entry field for Student ID
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(root)  # Entry field for Student Name
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Grade:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_grade = tk.Entry(root)  # Entry field for Student Grade
        self.entry_grade.grid(row=2, column=1, padx=10, pady=5)

        # Buttons for different operations
        tk.Button(root, text="Add Student", command=self.add_student).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Button(root, text="Update Student", command=self.update_student).grid(row=4, column=0, columnspan=2, pady=5)
        tk.Button(root, text="Delete Student", command=self.delete_student).grid(row=5, column=0, columnspan=2, pady=5)
        tk.Button(root, text="View Students", command=self.view_students).grid(row=6, column=0, columnspan=2, pady=5)

        # Creating a Treeview table to display student records
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Grade"), show="headings")
        self.tree.heading("ID", text="ID")  # Setting column headers
        self.tree.heading("Name", text="Name")
        self.tree.heading("Grade", text="Grade")
        self.tree.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

    def add_student(self):
        """Function to add a student record."""
        student_id = self.entry_id.get()  # Getting Student ID from entry field
        name = self.entry_name.get()  # Getting Student Name
        grade = self.entry_grade.get()  # Getting Student Grade

        if student_id and name and grade:  # Checking if all fields are filled
            if student_id in self.students:
                messagebox.showerror("Error", "Student ID already exists!")  # Show error if ID already exists
            else:
                self.students[student_id] = {"name": name, "grade": grade}  # Add student to dictionary
                self.refresh_table()  # Refresh the table to show updated data
                messagebox.showinfo("Success", "Student added successfully.")  # Success message
        else:
            messagebox.showerror("Error", "Please enter all details.")  # Error message if fields are empty

    def update_student(self):
        """Function to update an existing student's details."""
        student_id = self.entry_id.get()
        name = self.entry_name.get()
        grade = self.entry_grade.get()

        if student_id in self.students:  # Check if student exists
            if name:
                self.students[student_id]["name"] = name  # Update name if provided
            if grade:
                self.students[student_id]["grade"] = grade  # Update grade if provided
            self.refresh_table()  # Refresh the displayed data
            messagebox.showinfo("Success", "Student updated successfully.")
        else:
            messagebox.showerror("Error", "Student ID not found!")  # Error if student ID does not exist

    def delete_student(self):
        """Function to delete a student record."""
        student_id = self.entry_id.get()

        if student_id in self.students:  # Check if student exists
            del self.students[student_id]  # Delete student from dictionary
            self.refresh_table()  # Refresh the table
            messagebox.showinfo("Success", "Student deleted successfully.")
        else:
            messagebox.showerror("Error", "Student ID not found!")  # Error message

    def view_students(self):
        """Function to view all student records."""
        if not self.students:
            messagebox.showinfo("Info", "No students in the system.")  # Show message if no students exist
        else:
            self.refresh_table()  # Refresh the displayed table

    def refresh_table(self):
        """Function to refresh the Treeview table to show updated data."""
        for row in self.tree.get_children():
            self.tree.delete(row)  # Clear existing rows

        for student_id, details in self.students.items():  # Add updated data to table
            self.tree.insert("", "end", values=(student_id, details["name"], details["grade"]))

# Main Application Execution
if __name__ == "__main__":
    root = tk.Tk()  # Create the main Tkinter window
    app = StudentGradeSystem(root)  # Initialize the StudentGradeSystem class
    root.mainloop()  # Run the Tkinter event loop
