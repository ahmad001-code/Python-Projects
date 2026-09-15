students : dict[int, dict[str, str]]() = {
    101 : {"name": "Ahamd",
           "courses": {"cs200", "cs201"}},
    102 : {"name": "Sharif",
           "courses": {"cs201", "cs202"}},
}
def add_courses(student_id: int, course_code:str) -> None:
    courses = students[student_id]["courses"]
    courses.add(course_code)
    print(
        f"{students[student_id]['name']} registered for {course_code}"
    )
def remove_courses(student_id: int, course_code:str) -> None:
    courses = students[student_id]["courses"]
    courses.discard(course_code)
    print (
        f"{students[student_id]['name']} removed from {course_code}"
    )
def show_student(student_id: int) -> None:
    student = students[student_id]
    print(f"\nStudent ID: {student_id}")
    print(f"Name: {student['name']}")
    print(f"Courses: {student['courses']}")
print("Initial Student Records:")

show_student(101)
show_student(102)
print("\n---adding courses---")
add_courses(101, "cs204")
add_courses(102, "cs205")
print("\n---removing courses---")
remove_courses(101, "cs200")
remove_courses(102, "cs201")
print("\n---showing updated student records---")
show_student(101)
show_student(102)
print("\n---common courses---")
a = students[101]["courses"]
b = students[102]["courses"]
common_courses = a.intersection(b)
print(common_courses)
print("\n---all courses---")
all_courses = students[101]["courses"].union(students[102]["courses"])
print(all_courses)
