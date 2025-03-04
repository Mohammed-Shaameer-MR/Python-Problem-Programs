# Number Formatting  

### Problem Statement  
Given an integer `n`, print the following values for each integer `i` from `1` to `n`:  
1. **Decimal**  
2. **Octal**  
3. **Hexadecimal (Uppercase)**  
4. **Binary**  

Each value must be **space-padded** to match the width of the **binary representation of `n`**, ensuring proper alignment.  

### Function Description 
def print_formatted(number):
    pass  # Your code here

**Parameters:**  
- `int number`: The maximum value to print.  

**Prints:**  
- The formatted output, with each value space-padded and aligned.  

### Input Format  
A **single integer** `n`.  

### Constraints  
- `1 ≤ n ≤ 99`  

### Output Format  
Each line should contain the four values for `i` in the specified order, properly aligned.  

### Example 

#### Input
```
17
```

#### Processing 
Binary representation of `17` is **`10001`** (5 characters).  
Each number must be right-aligned to **width = 5**.  

#### Output
```
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
```

### Hints  
- Find **binary width** using `len(bin(n)[2:])`.  
- Format each value with `.rjust(width)`.  
- Use `oct(i)[2:]`, `hex(i)[2:].upper()`, `bin(i)[2:]`.  
- Loop through `1` to `n` and print formatted output.  
