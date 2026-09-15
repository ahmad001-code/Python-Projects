from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email format")

        self._email = value

    @abstractmethod
    def role_info(self):
        pass

    def __str__(self):
        return f"{self.name} {self.email}"


class Student(Person):

    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id

    def role_info(self):
        return f"Student: {self.student_id}"

    def __str__(self):
        return f"Student: {self.student_id}: {self.name} - {self.email}"


class Lecturer(Person):

    def __init__(self, name, email, lecturer_id):
        super().__init__(name, email)
        self.lecturer_id = lecturer_id

    def role_info(self):
        return f"Lecturer: {self.lecturer_id}"

    def __str__(self):
        return f"Lecturer: {self.lecturer_id}: {self.name} - {self.email}"


class Course:

    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f"Course: {self.course_name}, Students: {len(self.students)}"


student = Student("John", "john@email.com", 1)
student2 = Student("Jane", "jane@gmail.com", 2)
student3 = Student("Ahmad", "ahmad@gmail.com", 3)

lecturer1 = Lecturer("Rohid", "rohid@gmail.com", 1)
lecturer2 = Lecturer("Waseem", "waseem@gmail.com", 2)

course = Course("Programming")

course.add_student(student)
course.add_student(student2)

people = [
    student,
    lecturer2,
    student3
]

for person in people:
    print(person.role_info())

print(student)
print(student2)
print(course)