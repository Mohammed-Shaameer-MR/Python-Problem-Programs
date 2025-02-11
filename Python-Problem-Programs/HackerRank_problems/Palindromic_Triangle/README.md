# Palindromic Triangle  

## Problem Description  
You are given a positive integer **N**. Your task is to print a palindromic triangle of size **N**.  

For example, a palindromic triangle of size **5** is:  

1  
121  
12321  
1234321  
123454321  

You must complete the given code using exactly **one print statement**.  

## Input Format  
1. A single integer **N**.  

## Constraints  
- 0 < N < 10   
- Using **strings** will result in a score of **0**.  
- Using more than **one for-loop** will result in a score of **0**.  

## Output Format  
Print the palindromic triangle of size **N**.  

## Example  

### **Input:**  
5

### **Processing:**  
1. For each row **i** (from 1 to **N**), generate numbers in increasing order from **1** to **i**.  
2. Append the numbers in decreasing order from **i-1** to **1**.  
3. Print the generated sequence.  

### **Output:**  
1  
121  
12321  
1234321  
123454321  

## Hints  
- Use **mathematical operations** instead of string manipulation.  
- You can form the palindromic number using **multiplication and integer division** leveraging the powers of 10.  
- Consider the pattern: `1, 12, 123, ...` and how it reflects symmetrically.  