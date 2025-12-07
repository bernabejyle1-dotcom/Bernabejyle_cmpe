
student1_name = "luffy"
student1_grade = "80"
student1_subject = ["filipino", "english"]


student2_name = "zoro"
student2_grade = "85"
student2_subject = ["math", "science"]



student3_name = "nami san"
student3_grade = "90"
student3_subject = ["chem", "physics"]


def print_student_info(name, height, sport):
    print(f"{name} grade: {grade}: subject: {subject}")


if __name__ == "__manin__":
    print_student_info(student1_name, student1_grade, student1_subject)
    print_student_info(student2_name, student2_grade, student2_subeject)
    print_student_info(student3_name, student3_grade, student3_subject)


class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def print_student_info(self):
        print(f"Name: {self.name} | Grade: {self.grade} | Subjects: {self.subject}")

    @staticmethod
    def is_grade_passing(grade):
        return grade >= 75

if __name__ == "__main__":

    # Student 1
    student1 = Student(name="Luffy", grade=80, subject=["Filipino", "English"])
    student1.print_student_info()
    if Student.is_grade_passing(student1.grade):
        print("PASS")
    else:
        print("FAIL")
    print()

    # Student 2
    student2 = Student(name="Zoro", grade=74, subject=["Math", "Science"])
    student2.print_student_info()
    if Student.is_grade_passing(student2.grade):
        print("PASS")
    else:
        print("FAIL")
    print()

    # Student 3
    student3 = Student(name="Nami San", grade=70, subject=["Chem", "Physics"])
    student3.print_student_info()
    if Student.is_grade_passing(student3.grade):
        print("PASS")
    else:
        print("FAIL")
    print()

    #all method are function but not all function is method - it means all method are functions