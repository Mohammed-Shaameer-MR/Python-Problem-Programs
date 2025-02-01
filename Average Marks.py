'''
The provided code stub will read in a dictionary containing key/value pairs of name: [marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example

marks key:value pairs are

'alpha': [20, 30, 40]

'beta': [30, 50, 70]

query_name = 'beta'

The query_name is 'beta'. beta's average score is (30+50+70)/3 = 50.0.

Input Format

The first line contains the integer n, the number of students' records. The next n lines contain the names and marks obtained by a student, each value separated by a space.

The final line contains query_name, the name of a student to query.

Constraints

• 2 ≤ n ≤ 10

• 0 ≤ marks[i] < 100

• length of marks arrays = 3

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input O

3

Krishna 67 68 69

Arjun 70 98 63

Malika 52 56 60

Malika

Sample Output O

56.00

Explanation O

Marks for Malika are {52, 56, 60} whose average is 52+56+60 3 56

Sample Input 1

2

Harsh 25 26.5 28

Anurag

26

28

Harsh

30

Sample Output 1

26.50
'''

#Code:-

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