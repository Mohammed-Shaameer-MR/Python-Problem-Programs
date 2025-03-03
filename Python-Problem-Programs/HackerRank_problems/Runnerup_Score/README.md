# Find the Runner-Up Score  

### Problem Statement: Identify the Second-Highest Score  

Given a list of **n** scores from a sports event, determine the **runner-up score** (the second-highest unique value).  

### Function Description  
Implement a function that:  
- Accepts an integer `n` (number of scores).  
- Accepts a list of `n` integers representing scores.  
- Finds and prints the second-highest unique score.  

### Input Format  
1. An integer **n**, the number of scores.  
2. A space-separated list of **n** integers.  

### Constraints  
- `2 ≤ n ≤ 10`  
- `-100 ≤ A[i] < 100`  

### Output Format  
- Print the **runner-up score** as a single integer.  

### Example  

#### Input  
```
5  
2 3 6 6 5  
```

#### Processing  
1. The given scores are `[2, 3, 6, 6, 5]`.  
2. The maximum score is `6`.  
3. The second-highest (runner-up) score is `5`.  

#### Output  
```
5  
```

### Hints  
- Convert the list to a **set** to remove duplicates, then find the second-largest value.  
- Use the **sorted list** approach to determine the second-highest score efficiently.  
