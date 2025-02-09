# Prompt for number of students
n = int(input("Enter the number of students: "))

student_marks = {}

# Loop to enter student names and their scores
for _ in range(n):
    print("Enter student name and scores as space-separated values:")
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

# Prompt for the student whose average score is to be calculated
query_name = input("Enter the name of the student to get the average score: ")

# Calculate the average score of the specified student
result = sum(student_marks[query_name]) / len(student_marks[query_name])

# Display the result rounded to two decimal places
print(f"{query_name} : {result:.2f}")