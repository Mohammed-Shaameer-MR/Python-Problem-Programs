# Numerical Triangle  

## Problem Description  
You are given a positive integer **N**. Your task is to print a numerical triangle of height **N - 1**.  

For example, if **N = 5**, the output should be:  

1  
22  
333  
4444  

You must complete the given code using exactly **one print statement**.  

## Input Format  
1. A single integer **N**.  

## Constraints  
- 1 < N < 10 
- Using **strings** will result in a score of **0**.  
- Using more than **one for-loop** will result in a score of **0**.  

## Output Format  
Print **N-1** lines as explained above.  

## Example  

### Input:
5

### Processing:  
1. For each number **i** (from **1** to **N-1**), generate a number that consists of **i** repeated **i** times.  
2. Print the generated number.  

### Output:
1  
22  
333  
4444  

## Hints  
- Use **mathematical operations** instead of string manipulation.  
- Notice the pattern in how numbers grow, not just in length but in value.  
- Think about how repeating a digit multiple times forms a number.  