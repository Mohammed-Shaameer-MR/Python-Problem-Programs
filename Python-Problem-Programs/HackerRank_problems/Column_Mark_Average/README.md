# Column Average Marks

## Problem Description

Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class, and names. Your task is to help Dr. Wesley calculate the average marks of the students.

**Formula:**  
Average = Sum of all marks / Total Students

**Note:**
- Columns can be in any order. IDs, marks, class, and names can be written in any order in the spreadsheet.
- Column names are `ID`, `MARKS`, `CLASS`, and `NAME`. (The spelling and case type of these names won't change.)
- **Can you solve this challenge in 4 lines of code or less?**  
  There is no penalty for solutions that are correct but have more than 4 lines.

## Input Format
1. The first line contains an integer `N`, the total number of students.
2. The second line contains the names of the columns in any order.
3. The next `N` lines contain the marks, IDs, name, and class under their respective column names.

## Constraints
- 0 < `N` < 100

## Output Format
Print the average marks of the list corrected to 2 decimal places.

## Example

### TESTCASE 01

**Input:**
5
ID MARKS NAME     CLASS
1  97    Raymond  7
2  50    Steven   4
3  91    Adrian   9
4  72    Stewart  5
5  80    Peter    6

**Output:**
78.00

**Explanation:**
Average = (97 + 50 + 91 + 72 + 80) / 5 = 390 / 5 = 78.00

### TESTCASE 02

**Input:**
5
MARKS CLASS NAME   ID
92     2    Calum  1
82     5    Scott  2
94     2    Jason  3
55     8    Glenn  4
82     2    Fergus 5

**Output:**
81.00

**Explanation:**
Average = (92 + 82 + 94 + 55 + 82) / 5 = 405 / 5 = 81.00