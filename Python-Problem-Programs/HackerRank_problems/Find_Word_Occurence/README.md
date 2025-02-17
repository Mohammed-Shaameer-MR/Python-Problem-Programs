# Find Word Occurrence  

## Problem Description  
You will be given two integers, **n** and **m**. There are **n** words in **Group A**, which might contain duplicates. There are **m** words in **Group B**.  

For each word in **Group B**, check whether the word appears in **Group A**. If it appears, print the **1-indexed positions** of each occurrence in **Group A**. If it does not appear, print **-1**.  

## Input Format  
1. The first line contains two integers, **n** and **m**, separated by a space.  
2. The next **n** lines contain words belonging to **Group A**.  
3. The next **m** lines contain words belonging to **Group B**.  

## Constraints  
- **1 ≤ n ≤ 10,000**  
- **1 < m < 100**  
- **1 ≤ length of each word ≤ 100**  

## Output Format  
- Print **m** lines.  
- The **i-th** line should contain the **1-indexed positions** of occurrences of the **i-th** word from **Group B**, separated by spaces.  
- If the word does not appear in **Group A**, print **-1**.  

## Example  

### Input
5 2  
a  
a  
b  
a  
b  
b  
a  

### Processing  
- **'a'** appears at positions **1, 2, and 4** in **Group A**.  
- **'b'** appears at positions **3 and 5** in **Group A**.  

### Output  
1 2 4  
3 5    

## Explanation  
- The first word in **Group B**, **'a'**, appears **three times** at positions **1, 2, and 4** in **Group A**.  
- The second word in **Group B**, **'b'**, appears **two times** at positions **3 and 5** in **Group A**.  
- If a word in **Group B** does **not** appear in **Group A**, output **-1**.