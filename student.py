students = [
 ("Abel", 45),
 ("Sara", 80),
 ("John", 66),
 ("Mahi", 30),
 ("Helen", 90)
]

average_score = sum(score for _, score in students) / len(students)
highest_score = max(score for _, score in students)
lowest_score = min(score for _, score in students)
passed_students = [name for name, score in students if score >= 50]
failed_students = [name for name, score in students if score < 50]
bonus_marks = (map(lambda x: (x[0], x[1] + 5), students))
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print(f"Average Score: {average_score}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed Students: {passed_students}")
print(f"Failed Students: {failed_students}")
print(f"Bonus Marks: {list(bonus_marks)}")
print(f"Sorted Students: {sorted_students}")