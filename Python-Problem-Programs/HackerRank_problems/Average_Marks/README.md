# Average Marks

### Problem Statement  
The provided code stub will read a dictionary containing **key-value pairs** of student names and their respective marks. The task is to **compute and print the average** of the marks for a given student, rounded to **two decimal places**.  

### Function Description  
Implement the function `calculate_average(records, query_name)`, which:  
- Takes a dictionary `records` where the keys are student names, and the values are lists of marks.  
- Takes a string `query_name`, representing the student whose average is to be calculated.  
- Returns the computed average, rounded to **two decimal places**.  

### Input Format  
The input consists of multiple lines:  
1. The first line contains an integer, **n** – the number of student records.  
2. The next **n** lines contain a student's name followed by **three space-separated marks**.  
3. The final line contains **query_name**, the name of the student whose average is to be computed.  

### Constraints  
- `2 ≤ n ≤ 10`  
- `0 ≤ marks[i] < 100`  
- Each student has exactly **3 marks**.  

### Output Format  
- Print one line: The **average marks** of the queried student, rounded to **two decimal places**.  

### Example  
#### Input
3  
Krishna 67 68 69  
Arjun 70 98 63  
Malika 52 56 60  
Malika  
  

#### Processing  
- Marks for **Malika**: `{52, 56, 60}`  
- Compute sum: **168**  
- Count of marks: **3**  
- Compute average: **168 / 3 = 56.00**  

#### Output 
56.00
  

### Hints  
- Use a **dictionary** to store student names as keys and marks as values.  
- Use **sum()** and **len()** to compute the average efficiently.  
- Use Python’s `format()` or `round()` to round the result to **two decimal places**.  
