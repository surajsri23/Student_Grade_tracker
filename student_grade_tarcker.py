class StudentGradeTracker:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average(self):
        total_grades = 0
        total_subjects = 0
        for subject, grades in self.grades.items():
            total_grades += sum(grades)
            total_subjects += len(grades)
        return total_grades / total_subjects if total_subjects != 0 else 0

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def get_gpa(self, average):
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    def display_grades(self):
        print("Grades:")
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")
        average = self.calculate_average()
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {self.get_letter_grade(average)}")
        print(f"GPA: {self.get_gpa(average):.2f}")

def main():
    tracker = StudentGradeTracker()
    while True:
        print("\nOptions:")
        print("1. Add Grade")
        print("2. Display Grades")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            tracker.add_grade(subject, grade)
        elif choice == '2':
            tracker.display_grades()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
