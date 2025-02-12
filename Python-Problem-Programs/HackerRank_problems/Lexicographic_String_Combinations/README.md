# Lexicographic String Combinations

## Problem Statement  
You are given a string **S**.  

Your task is to print all possible combinations, up to size **k**, of the string in lexicographic sorted order.

## Input Format  
A single line containing the string **S** and integer value **k** separated by a space.

## Constraints  
- 0 < k < len(S)   
- The string contains only **UPPERCASE** characters.

## Output Format  
Print the different combinations of string **S** on separate lines.

## Example  

### Input  
HACK 2

### Processing  
The possible combinations, sorted in lexicographic order, are:  
A, C, H, K, AC, AH, AK, CH, CK, HK.

### Output  
A
C
H
K
AC
AH
AK
CH
CK
HK

## Hint  
- Consider using the `itertools.combinations()` function to generate combinations efficiently.
