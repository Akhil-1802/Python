students = []


class Student :
    def addStudent(self):
        global students
        roll = input("Enter roll no:")
        while(any(s["roll"] == roll for s in students)):
            roll = input("Roll Number already exists! Enter a new Roll Number: ")

        name = input("Enter name:")
        math = int(input("Enter math marks:"))
        english = int(input("Enter english marks:"))
        science = int(input("Enter science marks:"))
        total = math + english + science
        percentage = total / 3
        grade = self.calculate_grade(percentage)
        student = {
                "name":name,
                "roll":roll,
                "marks": {
                    "math":math,
                    "english":english,
                    "science":science
                },
                "total":total,
                "percentage":percentage,
                "grade":grade
            }
        students.append(student)

    def displayStudents(self):
        if(len(students) == 0):
            print("No records found!")
            return
        print("Student Records:")
        for s in students:
            print("Roll:", s["roll"])
            print("Name:", s["name"])
            for subject, marks in s["marks"].items():
                print(f"{subject.capitalize()}: {marks}")
            print("Total:", s["total"])
            print("Percentage:", s["percentage"])
            print("Grade:", s["grade"])
            print("-" * 20)

    def findTopper(self):
        if(len(students) == 0):
            print("No records found!")
            return
        topper = max(students, key=lambda student : student["total"])
        print("Topper:")
        print("Roll:", topper["roll"])
        print("Name:", topper["name"])
        for subject, marks in topper["marks"].items():
            print(f"{subject.capitalize()}: {marks}")
        print("Total:", topper["total"])
        print("Percentage:", topper["percentage"])
        print("Grade:", topper["grade"])
        print("-" * 20)

    def highest_subject_marks(self):
        if(len(students) == 0):
            print("No records found!")
            return
        subjects = ["math", "english", "science"]
        for subject in subjects:
            highest = max(students, key=lambda student : student["marks"][subject])
            print(f"Highest {subject.capitalize()} Marks:")
            print("Roll:", highest["roll"])
            print("Name:", highest["name"])
            print(f"{subject.capitalize()} Marks:", highest["marks"][subject])
            print("-" * 20)


    def students_below_average(self):
        if(len(students) == 0):
            print("No records found!")
            return
        avg = sum(student["percentage"] for student in students) / len(students)
        below_avg_students = [student for student in students if student["percentage"] < avg]
        if(len(below_avg_students) == 0):
            print("No students below average.")
            return
        print("Students Below Average:")
        for s in below_avg_students:
            print("Roll:", s["roll"])
            print("Name:", s["name"])
            for subject, marks in s["marks"].items():
                print(f"{subject.capitalize()}: {marks}")
            print("Total:", s["total"])
            print("Percentage:", s["percentage"])
            print("Grade:", s["grade"])
            print("-" * 20)

    def rank_students(self):
        if(len(students) == 0):
            print("No records found!")
            return
        ranked_students = sorted(students, key=lambda student : student["total"], reverse=True)
        print("Ranked Students:")
        for rank, s in enumerate(ranked_students, start=1):
            print(f"Rank {rank}:")
            print("Roll:", s["roll"])
            print("Name:", s["name"])
            for subject, marks in s["marks"].items():
                print(f"{subject.capitalize()}: {marks}")
            print("Total:", s["total"])
            print("Percentage:", s["percentage"])
            print("Grade:", s["grade"])
            print("-" * 20)
    
    def calculate_grade(self, percentage):
        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 70:
            return "C"
        elif percentage >= 60:
            return "D"
        else:
            return "F"
    def menu(self):
        while True:
            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. Display All Students")
            print("3. Find Topper")
            print("4. Highest Subject Marks")
            print("5. Students Below Average")
            print("6. Rank Students")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.addStudent()
            elif choice == "2":
                self.displayStudents()
            elif choice == "3":
                self.findTopper()
            elif choice == "4":
                self.highest_subject_marks()
            elif choice == "5":
                self.students_below_average()
            elif choice == "6":
                self.rank_students()
            elif choice == "7":
                break
            else:
                print("Invalid Choice! Please try again.")


if(__name__ == "__main__"):
    student = Student()
    student.menu()

