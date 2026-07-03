from functools import reduce

students = []
subjects = ("Math", "Science", "English")


class StudentManagementSystem:

    def validate_name(self, name):
        return name.replace(" ", "").isalpha()

    def calculate_grade(self, percentage):
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        return "F"

    def add_student(self):
        global students
        try:
            roll = int(input("Enter Roll Number: "))
            while (any(s["roll"] == roll for s in students)):
                roll = int(input("Roll Number already exists! Enter a new Roll Number: "))
            

            name = input("Enter Name: ").strip()
            while not self.validate_name(name):
                name = input("Invalid Name! Enter Name: ").strip()

            city = input("Enter City: ")

            marks = []
            for sub in subjects:
                m = float(input(f"Enter {sub} Marks: "))
                marks.append(m)

            total = sum(marks)
            percentage = total / len(subjects)
            grade = self.calculate_grade(percentage)

            student = {
                "roll": roll,
                "name": name,
                "city": city,
                "marks": marks,
                "total": total,
                "percentage": percentage,
                "grade": grade
            }

            students.append(student)
            print("Student Added Successfully!")

        except ValueError:
            print("Invalid Input!")
        finally:
            print("-" * 40)

    def display_students(self):
        if not students:
            print("No Records Found!")
            return

        for s in students:
            print("=" * 40)
            print(f"Roll       : {s['roll']}")
            print(f"Name       : {s['name']}")
            print(f"City       : {s['city']}")
            for i, sub in enumerate(subjects):
                print(f"{sub:<10}: {s['marks'][i]}")
            print(f"Total      : {s['total']}")
            print(f"Percentage : {s['percentage']:.2f}")
            print(f"Grade      : {s['grade']}")

    def search_student(self):
        try:
            roll = int(input("Enter Roll Number: "))
            for s in students:
                if s["roll"] == roll:
                    print("=" * 40)
                    print(f"Roll       : {s['roll']}")
                    print(f"Name       : {s['name']}")
                    print(f"City       : {s['city']}")
                    for i, sub in enumerate(subjects):
                        print(f"{sub:<10}: {s['marks'][i]}")
                    print(f"Total      : {s['total']}")
                    print(f"Percentage : {s['percentage']:.2f}")
                    print(f"Grade      : {s['grade']}")
                    return
            print("Student Not Found")
        except ValueError:
            print("Invalid Roll Number")

    def update_student(self):
        try:
            roll = int(input("Enter Roll Number: "))
            for s in students:
                if s["roll"] == roll:
                    name = input("Enter New Name: ").strip()
                    if self.validate_name(name):
                        s["name"] = name
                    s["city"] = input("Enter New City: ")

                    marks = []
                    for sub in subjects:
                        marks.append(float(input(f"Enter New {sub} Marks: ")))

                    s["marks"] = marks
                    s["total"] = sum(marks)
                    s["percentage"] = s["total"] / len(subjects)
                    s["grade"] = self.calculate_grade(s["percentage"])
                    print("Updated Successfully!")
                    return

            print("Student Not Found")
        except Exception as e:
            print("Error:", e)

    def delete_student(self):
        try:
            roll = int(input("Enter Roll Number: "))
            global students
            students = [s for s in students if s["roll"] != roll]
            print("Deleted Successfully (if roll existed)")
        except ValueError:
            print("Invalid Roll Number")

    def display_passed_students(self):
        passed = list(filter(lambda x: x["percentage"] >= 50, students))
        if not passed:
            print("No Passed Students")
            return
        print("Passed Students:")
        for s in passed:
            print(s["roll"], s["name"], s["percentage"])

    def sort_students(self):
        if not students:
            print("No Records")
            return
        sorted_students = sorted(students, key=lambda x: x["total"], reverse=True)
        print("Students Sorted by Total Marks:")
        for s in sorted_students:
            print(s["roll"], s["name"], s["total"])

    def show_class_average(self):
        if not students:
            print("No Records")
            return
        totals = list(map(lambda x: x["total"], students))
        class_total = reduce(lambda a, b: a + b, totals)
        print("Total Marks of Class:", class_total)
        
        percentage_sum = reduce(lambda a, b: a + b, map(lambda x: x["percentage"], students))
        avg = percentage_sum / len(students)
        print("Class Average:", round(avg, 2))

        

    def show_unique_cities(self):
        cities = set(map(lambda x: x["city"], students))
        print("Unique Cities:")
        for city in cities:
            print(city)

    def menu(self):
        while True:
            print("\n= STUDENT MANAGEMENT SYSTEM =")
            print("1. Add Student")
            print("2. Display All Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Display Passed Students")
            print("7. Sort Students by Total Marks")
            print("8. Show Class Average")
            print("9. Show Unique Cities")
            print("10. Exit")

            try:
                choice = int(input("Enter Choice(1-10): "))

                if choice == 1:
                    self.add_student()
                elif choice == 2:
                    self.display_students()
                elif choice == 3:
                    self.search_student()
                elif choice == 4:
                    self.update_student()
                elif choice == 5:
                    self.delete_student()
                elif choice == 6:
                    self.display_passed_students()
                elif choice == 7:
                    self.sort_students()
                elif choice == 8:
                    self.show_class_average()
                elif choice == 9:
                    self.show_unique_cities()
                elif choice == 10:
                    print("Thank You!")
                    break
                else:
                    print("Invalid Choice")

            except ValueError:
                print("Please enter a valid number.")


if __name__ == "__main__":
    student_obj = StudentManagementSystem()
    student_obj.menu()