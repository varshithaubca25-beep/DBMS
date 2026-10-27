import tkinter as tk
from tkinter import messagebox
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Varshi@123",
        database="student_db"
    )

def add_student():
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO students (name, email, course, semester) VALUES (%s,%s,%s,%s)",
            (name.get(), email.get(), course.get(), semester.get())
        )
        con.commit()
        messagebox.showinfo("Success", "Student added!")
        con.close()
        view_students()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def view_students():
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        output.delete("1.0", tk.END)
        for row in rows:
            output.insert(tk.END, str(row) + "\n")
        con.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_student():
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute(
            "UPDATE students SET name=%s, email=%s, course=%s, semester=%s WHERE student_id=%s",
            (name.get(), email.get(), course.get(), semester.get(), student_id.get())
        )
        con.commit()
        messagebox.showinfo("Success", "Student updated!")
        con.close()
        view_students()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_student():
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute(
            "DELETE FROM students WHERE student_id=%s",
            (student_id.get(),)
        )
        con.commit()
        messagebox.showinfo("Success", "Student deleted!")
        con.close()
        view_students()
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Student Record Management System")
root.geometry("600x600")

student_id = tk.StringVar()
name = tk.StringVar()
email = tk.StringVar()
course = tk.StringVar()
semester = tk.StringVar()

for label, variable in [
    ("Student ID (for update/delete)", student_id),
    ("Student Name", name),
    ("Email", email),
    ("Course", course),
    ("Semester", semester)
]:
    tk.Label(root, text=label).pack()
    tk.Entry(root, textvariable=variable).pack()

tk.Button(root, text="Add Student", command=add_student).pack(pady=4)
tk.Button(root, text="View Students", command=view_students).pack(pady=4)
tk.Button(root, text="Update Student", command=update_student).pack(pady=4)
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=4)

output = tk.Text(root, height=12, width=70)
output.pack(pady=10)

root.mainloop()