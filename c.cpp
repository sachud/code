// Programming Language: C++
// Code Functionality: Menu-Driven Student Record Management System
/*
This program allows you to:

Add student records
View all students
Search for a student
Exit the program

It uses only C++ basics: variables, arrays, loops, functions, conditionals, and input/output.
*/

// Complete Beginner-Friendly C++ Code (Type Daily)

#include <iostream>
#include <string>
using namespace std;

// Maximum number of students allowed
const int MAX_STUDENTS = 50;

// Arrays to store student data
string studentNames[MAX_STUDENTS];
int studentAges[MAX_STUDENTS];
int studentCount = 0;

// Function to add a student
void addStudent() {
    if (studentCount >= MAX_STUDENTS) {
        cout << "Student limit reached!\n";
        return;
    }

    cout << "Enter student name: ";
    cin.ignore();              // Clear input buffer
    getline(cin, studentNames[studentCount]);

    cout << "Enter student age: ";
    cin >> studentAges[studentCount];

    studentCount++;             // Increase student count
    cout << "Student added successfully!\n\n";
}

// Function to display all students
void viewStudents() {
    if (studentCount == 0) {
        cout << "No students available.\n\n";
        return;
    }

    cout << "\nStudent List:\n";
    for (int i = 0; i < studentCount; i++) {
        cout << i + 1 << ". "
             << studentNames[i]
             << " (Age: " << studentAges[i] << ")\n";
    }
    cout << endl;
}

// Function to search for a student by name
void searchStudent() {
    if (studentCount == 0) {
        cout << "No students to search.\n\n";
        return;
    }

    string searchName;
    cout << "Enter student name to search: ";
    cin.ignore();
    getline(cin, searchName);

    bool found = false;

    for (int i = 0; i < studentCount; i++) {
        if (studentNames[i] == searchName) {
            cout << "Student found!\n";
            cout << "Name: " << studentNames[i] << endl;
            cout << "Age: " << studentAges[i] << endl << endl;
            found = true;
            break;
        }
    }

    if (!found) {
        cout << "Student not found.\n\n";
    }
}

// Function to display menu
void showMenu() {
    cout << "===== STUDENT MANAGEMENT MENU =====\n";
    cout << "1. Add Student\n";
    cout << "2. View Students\n";
    cout << "3. Search Student\n";
    cout << "4. Exit\n";
    cout << "Enter your choice: ";
}

// Main function
int main() {
    int choice;

    while (true) {
        showMenu();
        cin >> choice;
        cout << endl;

        if (choice == 1) {
            addStudent();
        }
        else if (choice == 2) {
            viewStudents();
        }
        else if (choice == 3) {
            searchStudent();
        }
        else if (choice == 4) {
            cout << "Exiting program. Goodbye! 🚀\n";
            break;
        }
        else {
            cout << "Invalid choice. Try again.\n\n";
        }
    }

    return 0;
}

/*
How to Practice This Code Daily

Type the entire code manually
Compile & run:
    g++ program.cpp -o program
    ./program
Change variable names
Add extra cout statements to understand flow

Features You Can Add (Step-by-Step Growth)
🟢 Beginner Enhancements

Add student ID
Display total number of students
Prevent duplicate student names

🟡 Intermediate Enhancements

Delete a student record
Update student details
Store data in a file (file handling)

🔵 Advanced Enhancements (Later)

Use structures (struct)
Use classes & objects (OOP)
Use vectors instead of arrays
Add password-protected admin access
*/

