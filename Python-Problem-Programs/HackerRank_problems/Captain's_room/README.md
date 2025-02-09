# Captain's room

### Problem Statement  
Mr. Anant Asankhya manages the **INFINITE** hotel, which has **unlimited rooms**. One day, a group of tourists arrives, consisting of:  
- A **single Captain**, who gets a **separate room**.  
- Several **families**, each having **exactly k members** (where `k > 1`).  

Each **family** is assigned a **single** room, which appears exactly **k times** in the list, while the **Captain's room appears only once**.  

The manager receives a **list of room numbers** (unordered) and must determine the **Captain’s room number**.  

### Function Description  
Implement the function `find_captains_room(k, room_numbers)`, which:  
- Takes an integer `k` (family size).  
- Takes a **list of room numbers** representing room assignments.  
- Returns the **Captain’s room number** (the unique number appearing **only once**).  

### Input Format  
The input consists of **two lines**:  
1. An integer **k** representing the number of members in each family.  
2. A space-separated list of room numbers.  

### Constraints  
- `2 ≤ k < 1000`  
- Room numbers are **positive integers**.  

### Output Format  
- Print a **single integer**, which is the **Captain's room number**.  

### Example  
#### Input
3  
1 2 3 6 2 3 1 1 2 3  


#### Processing  
- Each **family room** appears **3 times**.  
- The **Captain's room** appears **once**.  
- The unique room number is **6**.  

#### Output 
6
 

### Hints  
- Use Python’s **collections.Counter** or **set operations**.  
- The sum of unique elements times `k` minus the total sum gives the **Captain’s room**.  
