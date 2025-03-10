print("\033[1;34NmReport Card Generator\033[0m")


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.total = sum(marks.values())
        self.percentage = self.total / len(marks)
        self.grade = self.assign_grade()

    def assign_grade(self):
        if self.percentage >= 80:
            return 'A+'
        elif self.percentage >= 70:
            return 'A'
        elif self.percentage >= 60:
            return 'B'
        elif self.percentage >= 50: 
            return 'C'
        elif self.percentage >= 40:
            return 'D'
        else:
            return 'Fail'
            
    def display_report(self):
        print("\n-----------------------")
        print(f"Report Card For {self.name} (Roll No: {self.roll_no})")
        print("-----------------------")
        for subject, score in self.marks.items():
            print(f"{subject}: {score}")
        print(f"Total Marks: {self.total}")
        print(f"Percentage: {self.percentage:.2f}%")
        print(f"Grade: {self.grade}")
        print("-----------------------\n")

def get_marks():
    subjects = ["Math", "Physics", "Urdu", "English", "Computer"]
    marks = {}
    for subject in subjects:
        while True:
            try:
                score = float(input(f"Enter marks for {subject}: "))
                if 0 <= score <= 100:
                    marks[subject] = score
                    break
                else:
                    print("Marks should be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")
    return marks

students = []
while True:
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")
    marks = get_marks()
    
    student = Student(name, roll_no, marks)
    students.append(student)
    print(f"\033[1;31mRecord of {name} inserted successfully.\033[0m")


    
    more = input("Do you want to insert more? Press 'Y' for Yes or 'N' for No: ").strip().lower()
    if more != 'y':
        break

print("\nGenerating Report Cards...")
for student in students:
    student.display_report()
