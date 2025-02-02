'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

• Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)

• The design should have 'WELCOME' written in the center.

• The design pattern should only use .. and - characters.

Input Format

A single line containing the space separated values of N and M.

Constraints

• 5 < N < 101

• 15 < M < 303

Output Format

Output the design pattern.

Sample Input

9 27

Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''

#Code:-

line=input().strip().split(' ')
n,m=tuple(int(l) for l in line)

welcome='WELCOME'

#Upper part
for i in range(n//2):
    print(('.|.'*(2*i+1)).center(m,'-')) #Repeating '.|.' for odd no of times per each iteration
        
#Middle Part
print(welcome.center(m,'-'))

#Lower part
for i in range(n//2,0,-1):
    print(('.|.'*(2*i-1)).center(m,'-'))
    