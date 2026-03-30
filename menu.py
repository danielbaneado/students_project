import functions as fun
op= True
students= []
courses= ("Cybersecurity", "Data science", "Networking", "Robotic")
id= 0

while op!= 6:
    try:
        op= int(input("Student register\n 1) Register student\n 2) Show students\n 3) Filter student by\n 4) Update student info\n 5) Delete student\n 6) Exit\n >> "))
        if op not in range(0, 7):
            raise ValueError
    except:
        print("Invalid option!")
        continue

    if op== 1:
        id+= 1
        try:
            name= input("Type student name\n >> ").capitalize()
            age= int(input("Student age\n >> "))
            course= input("Course\n >> ").capitalize()
            status= input("Status (active/inactive)\n >> ").capitalize()
            if course not in courses or status!= "Active" and status!= "Inactive":
                raise ValueError
        except:
            print("There was invalid values to register student, please try again.")
            continue
        fun.register_student(students, id, name, age, course, status)

    elif op== 2:
        fun.show_students(students)

    elif op== 3:
        if not students:
            print("There's no students in system!")
            continue
        try:
            filter_by= input("Filter student by\n >> ").capitalize()
            data= input("Data to filter\n >> ").capitalize()
        except:
            print("An error raised, redirecting..")
            continue
        if filter_by== "Id":
            filter_by= filter_by.upper()
        if filter_by== "Age" or filter_by== "ID":
            data= int(data)
        fun.filter_student(students, filter_by, data)

    elif op== 4:
        if not students:
            print("There's no students in system!")
            continue
        try:
            name_to= input("Type student name\n >> ").capitalize()
            to_update= input("Type data to update\n >> ").capitalize()
            data_to= input(f"New {to_update.lower()}\n >> ")
        except:
            print("An error raised, redirecting..")
            continue
        if to_update== "Age" or to_update== "ID":
            data_to= int(data_to)
        elif to_update== "Course" or to_update== "Status":
            data_to= data_to.capitalize()
        fun.update_student(students, name_to, to_update, data_to)

    elif op== 5:
        if not students:
            print("There's no students in system!")
            continue
        to_delete= input("Type student name to delete\n >> ").capitalize()
        fun.delete_student(students, to_delete)

    elif op== 6:
        print("Thanks for use our services!")
