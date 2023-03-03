grades = []

students = int(input("How many students are in your class?"))
student_num = 0

for i in range(students):
  student_num += 1
  #print("Input a grade for student # ")
  print("Input a grade for student # ", student_num)
  student_grade = int(input())

  grades.append(student_grade)
print(grades)
#gradesum=int()
gradesum = sum(grades)
average = (gradesum / student_num)
print("Your class average is: ", average, "%")
#print(str("The average is: ", average))