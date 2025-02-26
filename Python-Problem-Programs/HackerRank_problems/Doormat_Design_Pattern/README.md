# Doormat Design Pattern

### Problem Statement  
Mr. Vincent works in a **door mat manufacturing company**. One day, he designed a new **door mat** with the following specifications:  
- The **mat size** must be **N × M**, where:  
  - **N** is an **odd natural number**.  
  - **M = 3 × N**.  
- The design should have **'WELCOME'** written at the center.  
- The design pattern should only use **`.|.`** and **`-`** characters.  

### Function Description  
Implement the function `print_door_mat(n, m)`, which:  
- Takes two integers **N** (height) and **M** (width).  
- Prints the **door mat pattern** based on the given conditions.  

### Input Format  
A single line containing two **space-separated** integers, **N** and **M**.  

### Constraints  
- `5 < N < 101` (N must be **odd**)  
- `15 < M < 303` (`M = 3 × N`)  

### Output Format  
Print the **door mat pattern**.  

### Example  
#### Input
9 27
 

#### Output
```
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
```
 

### Hints  
- Use `str.center(width, '-')` for **alignment**.  
- The top half has **increasing** `.|.` patterns, while the bottom half is a **mirror** of the top.  
- The **middle row** contains `"WELCOME"`.  
