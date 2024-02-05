#include <iostream>
#include <string>
using namespace std;

struct Course {
    string course_code;
    string course_name;
};

struct Grade {
    int mark;
    char the_grade;
};

struct Student {
    string registration_number;
    string name;
    int age;
    Course course;
    Grade grades[10]; // Assuming a student can have at most 10 grades
    int num_grades = 0; // Number of grades added so far
};

Student students[40]; // Array to store up to 40 students
int num_students = 0; // Number of students added so far

char calculateGrade(int mark) {
    if (mark > 69) return 'A';
    else if (mark > 59) return 'B';
    else if (mark > 49) return 'C';
    else if (mark > 39) return 'D';
    else return 'E';
}

void addStudent(string registration_number, string name, int age, Course course) {
    if (num_students >= 40) {
        cout << "Cannot add more students." << endl;
        return;
    }
    students[num_students].registration_number = registration_number;
    students[num_students].name = name;
    students[num_students].age = age;
    students[num_students].course = course;
    num_students++;
}

void editStudentDetails(int index, string registration_number, string name, int age, Course course) {
    if (index < 0 || index >= num_students) {
        cout << "Invalid student index." << endl;
        return;
    }
    students[index].registration_number = registration_number;
    students[index].name = name;
    students[index].age = age;
    students[index].course = course;
}

void addMark(int student_index, int mark) {
    if (student_index < 0 || student_index >= num_students) {
        cout << "Invalid student index." << endl;
        return;
    }
    if (students[student_index].num_grades >= 10) {
        cout << "Cannot add more grades for this student." << endl;
        return;
    }
    students[student_index].grades[students[student_index].num_grades].mark = mark;
    students[student_index].grades[students[student_index].num_grades].the_grade = calculateGrade(mark);
    students[student_index].num_grades++;
}

int main() {
    // Add students, edit details, and add marks here
    return 0;
}
