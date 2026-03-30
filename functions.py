def register_student(students, id, name, age, course, status):
    students.append({"ID": id, "Name": name, "Age": age, "Course": course, "Status": status})
    print(name, "registered successfully")

def show_students(students):
    if not students:
        print("There's no students in system!")
        return
    print("Students list")
    print("-" * 30)
    for student in students:
        for k, v in student.items():
            print(k, "->", v)
        print("-" * 30)

def filter_student(students, filter_by, data):
    print(f"Students with {data} as {filter_by.lower()}")
    print("-" * 30)
    for student in students:
        for k, v in student.items():
            if v!= data:
                continue
            for k, v in student.items():
                if k!= filter_by:
                    print(k, "->", v)
            print("-" * 30)

def update_student(students, name_to, to_update, data_to):
    for student in students:
        if student["Name"]!= name_to:
            continue
        for k, v in student.items():
            if k== to_update:
                student[to_update]= data_to
    print("Info successfully updated!")

def delete_student(students, to_delete):
    for student in students:
        if student["Name"]== to_delete:
            students.remove(student)
            print(to_delete, "succesfully deleted")

