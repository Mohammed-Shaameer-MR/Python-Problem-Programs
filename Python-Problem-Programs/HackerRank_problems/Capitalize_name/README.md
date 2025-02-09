# Capitalize Names 

### Problem Statement  
You are given a **full name** where the first and last names may be in lowercase. The task is to **capitalize** the first letter of each word while keeping the rest of the characters unchanged.  

For example:  
- **Input:** `alison heck`  
- **Output:** `Alison Heck`  

### Function Description  
Implement the function `capitalize_name(S)`, which:  
- Takes a **string** `S` containing a full name.  
- Returns the **properly capitalized** name.  

### Input Format  
- A **single line** containing the full name **S**.  

### Constraints  
- `0 < len(S) < 1000`  
- The string consists of **alphanumeric characters** and **spaces**.  
- If a word starts with a number (e.g., `12abc`), it remains **unchanged** after capitalization.  

### Output Format  
- Print the capitalized string **S**.  

### Example  
#### Input  
chris alan  


#### Processing  
- Convert each word's **first letter** to uppercase.  
- Keep other characters **unchanged**.  

#### Output  
Chris Alan
 

### Hints  
- Use Python’s **`.title()`** or **`.capitalize()`** methods.  
- Handle **words that start with numbers** carefully.  
