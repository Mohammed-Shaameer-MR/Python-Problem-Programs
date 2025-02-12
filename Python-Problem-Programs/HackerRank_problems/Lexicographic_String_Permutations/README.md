# Lexicographic String Permutations

## Problem Statement  
You are given a string **S**.  
Your task is to print all possible permutations of size **k** of the string in lexicographic sorted order.

## Input Format  
A single line containing the space-separated string **S** and the integer value **k**.

## Constraints  
- 0 < k < len(S)  
- The string contains only **UPPERCASE** characters.

## Output Format  
Print the permutations of the string **S** on separate lines.

## Example  

### Input  
HACK 2

### Processing  
The possible size **2** permutations of the string "HACK" in lexicographic order are:

AC, AH, AK, CA, CH, CK, HA, HC, HK, KA, KC, KH.

### Output  
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

## Hint  
- Consider using the `itertools.permutations()` function to generate permutations efficiently.

