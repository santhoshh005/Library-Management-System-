students = []

sid = input("Enter Student ID: ")
name = input("Enter Name: ")
dept = input("Enter Department: ")

students.append([sid, name, dept])

print("Student Registered Successfully")
print("Registered Students:", students)


def login():
    username = "admin0101"
    password = "12344321"

    u = input("Enter username: ")
    p = input("Enter password: ")

    if u == username and p == password:
        print("Login Successful")
    else:
        print("Invalid Username or Password")

login()