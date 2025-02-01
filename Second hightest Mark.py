'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]] The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. There are two students with that score: ["beta", "alpha"]. Ordered alphabetically, the names are printed as:

alpha beta

Input Format

The first line contains an integer, N, the number of students.

The 2N subsequent lines describe each student over 2 lines.

- The first line contains a student's name.

The second line contains their grade.

Constraints

• 2<N<5

• There will always be one or more students having the second lowest grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input O

5

Harry

37.21

Berry

37.21

Tina

37.2

Akriti

41

Harsh

39

Sample Output O

Berry Harry

Explanation O

There are 5 students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
'''

#Code:-

lname, lscore = [], []

# Prompt for number of students
n = int(input("Enter the number of students: "))

for _ in range(n):
    name = input("Enter student name: ")
    score = float(input(f"Enter score for {name}: "))
    lname.append(name)
    lscore.append(score)

# Getting the second lowest score
lsscore = list(set(lscore))
lsscore.sort()
seclow = lsscore[1]

# Joining them into one nested list
records = [[x, y] for x, y in zip(lname, lscore)]
result = []

# Finding the names of second-lowest scores
for i in range(len(records)):
    if records[i][1] == seclow:
        result.append(records[i][0])

# Sorting names alphabetically
result.sort()

# Display names of students with the second-lowest score
print("\nStudents with the second-lowest score:")
for i in result:
    print(i)

lname, lscore = [], []

# Prompt for number of students
n = int(input("Enter the number of students: "))

print("\nEnter the details of the students here:-")
for _ in range(n):
    name = input("Enter student name: ")
    score = float(input(f"Enter score for {name}: "))
    lname.append(name)
    lscore.append(score)

# Getting the second lowest score
lsscore = list(set(lscore))
lsscore.sort()
seclow = lsscore[1]

# Joining them into one nested list
records = [[x, y] for x, y in zip(lname, lscore)]
result = []

# Finding the names of second-lowest scores
for i in range(len(records)):
    if records[i][1] == seclow:
        result.append(records[i][0])

# Sorting names alphabetically
result.sort()

# Display names of students with the second-lowest score
print("\nStudents with the second-lowest score:")
for i in result:
    print(i)
