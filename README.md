📘 README.md

# 🎓 Student Management System (SEN 201 Project)

## 📖 Overview
This project is a simple **Python-based Student Management System** that allows users to **add, view, search, update, and delete** student records.  
It is a console-based program that stores data in a **CSV file**, making it easy to run and manage without requiring a database.

---

## 🧠 Software Development Life Cycle (SDLC) Explanation

### 1️⃣ Planning
The goal of the project is to create a simple system that allows users to manage student information efficiently.  
The system is implemented in Python and uses a CSV file for data storage.

### 2️⃣ Requirement Analysis
**Functional Requirements:**
- Add a new student record  
- View all student records  
- Search for a student by ID  
- Update a student record  
- Delete a student record  

**Non-Functional Requirements:**
- The system should be easy to use (menu-driven interface)  
- Data should be saved persistently (using a CSV file)  

### 3️⃣ Design
The program consists of a single file (`student_management_system.py`) with functions to:
- Add student data  
- Display all student data  
- Search for a student  
- Update student details  
- Delete a student record  

Data is stored in `students.csv` in the format:

Student ID, Name, Age, Course

### 4️⃣ Implementation
The system is implemented using Python’s built-in `csv` module for file handling.  
The main features are organized as separate functions, and users interact through a simple text-based menu.

### 5️⃣ Testing
The program was tested with various inputs to ensure:
- Students can be added, viewed, searched, updated, and deleted successfully.
- The system handles invalid choices and missing files gracefully.

### 6️⃣ Deployment
The project is deployed on **GitHub** as a public repository.  
Users can clone or download the project and run it directly using Python.

### 7️⃣ Maintenance
Future improvements could include:
- Adding data validation  
- Using a database (SQLite or MySQL) for storage  
- Adding a graphical user interface (GUI) with Tkinter or Flask

---

## 💻 How to Run the Project

### **Requirements**
- Python 3.x installed on your system

### **Steps**
1. Download or clone this repository:
   ```bash
   git clone https://github.com/<your-username>/SEN201-Student-Management-System.git

	2.	Open a terminal in the project folder.
	3.	Run the program:

python student_management_system.py


	4.	Follow the on-screen menu options.

⸻

📂 Project Structure

SEN201-Student-Management-System/
│
├── student_management_system.py   # Main program file
├── students.csv                   # Data file (auto-created)
└── README.md                      # Project documentation


⸻

👨‍💻 Author

Name: Apeh Joshua
Course: SEN 201 – Software Engineering
Institution: CALEB UNIVERSITY
Year: 2026

⸻

🏁 Conclusion

This project demonstrates the complete Software Development Life Cycle (SDLC) — from planning and requirement analysis to implementation and deployment — using Python.
It’s a simple yet effective example of software engineering principles in practice.
