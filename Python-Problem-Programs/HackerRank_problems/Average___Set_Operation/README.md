# Average Set Operation

### Problem Statement: Compute the Average Height of Distinct Plants  

Ms. Gabriel Williams, a botany professor at District College, asked her student Mickey to compute the **average height of all distinct plants** in her greenhouse. The goal is to determine the average by considering only the **unique** plant heights.  

The formula used for this calculation is:  

Average = (Sum of Distinct Heights) / (Total Number of Distinct Heights)

### Function Description  
Implement the function `average(arr)`, which:  
- Takes a list of integers, `arr`, representing plant heights.  
- Returns the computed average as a floating-point value rounded to **three decimal places**.  

### Input Format  
The input consists of two lines:  
1. The first line contains an integer, **N** – the number of elements in the list.  
2. The second line contains **N** space-separated integers representing plant heights.  

### Constraints  
- `0 < N < 100`  

### Output Format  
- Print the computed **average height** rounded to **three decimal places**.  

### Example  
#### Input 
10  
161 182 161 154 176 170 167 171 170 174  
 

#### Processing 
- Extract distinct heights: `{154, 161, 167, 170, 171, 174, 176, 182}`  
- Compute sum: 1355  
- Count of distinct heights: 8  
- Compute average: 1355 / 8 = 169.375 

#### Output    
169.375  


### Hints  
- Use Python's `set()` function to extract unique heights.  
- Use `sum()` and `len()` to compute the average efficiently.  

