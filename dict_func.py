student_grades = {'Ram': 85, 'Sham': 92, 'Ojas’': 88, 'Anay': 79}
student_grades['Eve']=95
print(student_grades)
print("Sorted student grades are: ", sorted(student_grades))
import math
def f():
    val = student_grades.values()
    high = max(val)
    print(f"Student with highest grade is {high} ")
f()


