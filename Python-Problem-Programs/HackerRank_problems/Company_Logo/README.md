# Company Logo  

## Problem Description  
A newly opened multinational brand has decided to base its company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition.  

Given a string **S**, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.  

### Conditions:  
- Print the three most common characters along with their occurrence count.  
- Sort in descending order of occurrence count.  
- If the occurrence count is the same, sort the characters in alphabetical order.  

For example, according to the conditions described above, **"GOOGLE"** would have its logo with the letters **"G,O,E"**.  

## Input Format  
- A single line of input containing the string **S**.  

## Constraints  
1. $$3 < \text{len}(S) \leq 10^6$$  
2. **S** has at least **3 distinct characters**.  

## Output Format  
- Print the three most common characters along with their occurrence count, each on a separate line.  
- The output should be sorted in **descending order of occurrence count**.  
- If multiple characters have the same occurrence count, sort them **alphabetically**.  

## Example  

### **Input**  
```
aabbbccde
```

### **Output**  
```
b 3
a 2
c 2
```

## **Explanation**  
In **"aabbbccde"**:  
- **'b'** occurs **3 times**, so it is printed first.  
- **'a'** and **'c'** both occur **2 times**. Since **'a'** comes before **'c'** alphabetically, it is printed first.