# Merge the tools

### Problem Statement: Extract Unique Characters from Substrings  

Given a string **s** of length **n**, where **n** is a multiple of **k**, split **s** into contiguous substrings of size **k**. For each substring, construct a new string by removing duplicate characters while maintaining their first occurrence order.  

The goal is to print **n/k** lines, each containing a processed substring.  

The transformation follows these rules:  
- **Split** `s` into `n/k` substrings of size `k`.  
- **Remove duplicate characters** from each substring while preserving order.  
- **Print each transformed substring** on a new line.  

### Function Description  
Implement `merge_the_tools(s, k)`, which:  
- Accepts a string `s` and an integer `k`.  
- Prints the transformed substrings.  

### Input Format  
The input consists of:  
1. A string **s**.  
2. An integer **k**, the length of each substring.  

### Constraints  
- `1 ≤ n ≤ 10⁴` (length of `s`).  
- `1 ≤ k ≤ n`.  
- `n` is guaranteed to be a multiple of `k`.  

### Output Format  
- Print each unique-character substring on a **new line**.  

### Example  

#### Input  
AABCAAADA  
3  
  

#### Processing  
1. Split `s` into substrings: `["AAB", "CAA", "ADA"]`.  
2. Remove duplicate characters while maintaining order:  
   - `"AAB"` → `"AB"`  
   - `"CAA"` → `"CA"`  
   - `"ADA"` → `"AD"`  

#### Output  
AB  
CA  
AD  
  

### Hints  
- Use slicing to extract substrings.  
- Utilize an ordered set or `dict.fromkeys()` to remove duplicates while preserving order.  
