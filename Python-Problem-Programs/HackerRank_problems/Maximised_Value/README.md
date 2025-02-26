# Maximizing S Value

## Problem Description

You are given **K** lists, each containing some integers. You must pick **one element** from each list, square the chosen numbers, sum them up, and take the result modulo **M**. Your goal is to **maximize** this final value.

### Notes:
- You must select **exactly one number** from each list.
- The numbers chosen **do not have to be the largest** in their respective lists.
- The result should be taken **modulo M**.

## Input Format

1. The first line contains two space-separated integers:  
   - **K**, the number of lists  
   - **M**, the modulo value  
2. The next **K** lines each contain:  
   - An integer **Nᵢ**, which represents the number of elements in that list.  
   - **Nᵢ** space-separated integers, representing the elements in the list.  

## Constraints

- 1 ≤ K ≤ 7  
- 1 ≤ M ≤ 1000  
- 1 ≤ Nᵢ ≤ 7  
- The magnitude of elements in the list is less than 10⁹  

## Output Format

Output a single integer representing the maximum possible value after applying the given conditions.

## Example

### Input
```
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
```

### Processing
Choose 5 from the first list, 9 from the second list, and 10 from the third list.  

- 5² = 25  
- 9² = 81  
- 10² = 100  
- Sum = 25 + 81 + 100 = 206  
- 206 mod 1000 = 206  

### Output
206
