scores = [80, 85, 83, 55, 77, 93, 65, 44, 87, 50]
print(scores)
max_score = max(scores)
min_score = min(scores)
avg_score = sum(scores)/len(scores)
print(max_score, min_score, avg_score)
passing_scores = [score for score in scores if score >= 60]
print(passing_scores)
score_set=set(scores)
print(score_set)
students = {
    1 : "Ahmad",
    2 : "Sahil",
    3 : "Hameed",
    4: "Amir",
    5: "Haseeb",
    6: "Nimat",
    7: "Sediq",
    8: "Jawad",
    9: "Naweed",
    10: "Ali",
}
print(students)
student_id = 5
if student_id in students:
    print(students[student_id])
else:
    print("Student ID not found")
student_records = [
    ("Ahmad", 85),
    ("Sahil", 50),
    ("Amir", 93),
    ("Haseeb", 44),
    ("Ali", 55),
    ("Hameed", 87),
    ("Nimat", 83),
    ("Sediq", 80),
    ("Naweed", 77),
    ("Jawad", 65),

]
sorted_student_records = sorted(student_records, key=lambda student: student[1])
print("Sorted Recordes")
for student in sorted_student_records:
    print(student)

