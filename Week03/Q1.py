#Q1: Create a program that manages student grades:

#Grade list
grades = [85, 92, 78, 95, 88]

grades.append(90)
grades.sort()
print(f"Sorted grade: {grades}")
print("Sorted grade:", grades)
print(f"Highest grade: {grades[-1]}")
print(f"Lowest grade: {grades[0]}")
print(f"Total number of grades: {len(grades)}")
