# Compress the String

## Problem Description

You are given a string **S**. Suppose a character **c** occurs consecutively **X** times in the string. Replace these consecutive occurrences of the character **c** with **(X, c)** in the string.

To solve this problem efficiently, you can use the `groupby()` function from the `itertools` module in Python, which groups adjacent elements in an iterable.

## Input Format

A single line of input consisting of the string **S**.

## Output Format

A single line of output consisting of the modified string with space.

## Constraints

- All the characters of **S** denote integers between **0** and **9**.
- **1 ≤ |S| ≤ 10⁴**

## Example
### Input:
```
1222311
```

### Processing:
- The character **1** occurs once → **(1, 1)**
- The character **2** occurs three times → **(3, 2)**
- The character **3** occurs once

### Output:
```
(1, 1) (3, 2) (1, 3) (2, 1)
```
