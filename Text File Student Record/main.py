def add_student(filename: str, sid: int, name: str ) -> None:
    with open("student.txt", 'a', encoding="utf-8" ) as file:
        file.write(f"{sid} | {name}\n")
def list_students(filename: str) -> None:
    with open("student.txt", 'r', encoding="utf-8") as file:
        for line in file:
            print(line.rstrip())
add_student("student.txt", 1, "Ahmad")
add_student("student.txt", 2, "Amir")
add_student("student.txt", 3, "Sharif")
add_student("student.txt", 4, "rahim")
add_student("student.txt", 5, "Noor")
list_students("student.txt")
