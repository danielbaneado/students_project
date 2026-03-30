Student register ✅

This is a modular Student Management System built in Python that allows users to perform basic CRUD operations (Create, Read, Update, Delete) on student records.

The application is designed with separation of concerns:

app.py → Handles user interaction, menu flow, and input validation
functions.py → Contains the core logic and operations on the data

This structure improves maintainability, scalability, and readability.

⚙️ Features
✅ Register new students
📋 Display all students
🔍 Filter students by specific fields (ID, Name, Age, Course, Status)
✏️ Update student information
❌ Delete students from the system
🛡️ Input validation and error handling
🧱 Project Structure
project/
│
├── app.py          # Main application (menu + input handling)
├── functions.py    # Core logic (CRUD operations)
└── README.md       # Project documentation
🧠 Data Model

Each student is stored as a dictionary with the following structure:

{
    "ID": int,
    "Name": str,
    "Age": int,
    "Course": str,
    "Status": str
}

All students are stored in a list:

students = []
🚀 How to Run
Make sure you have Python installed (Python 3.x recommended)
Clone or download this repository
Run the application:
python app.py
🕹️ Usage

When running the program, you will see a menu:

1) Register student
2) Show students
3) Filter student by
4) Update student info
5) Delete student
6) Exit

Follow the prompts to interact with the system.

⚠️ Validations
Course must be one of:
Cybersecurity
Data Science
Networking
Robotic
Status must be:
Active
Inactive
Age and ID must be integers
