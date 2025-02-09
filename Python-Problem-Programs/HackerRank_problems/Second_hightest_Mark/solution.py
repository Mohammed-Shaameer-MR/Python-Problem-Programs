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
