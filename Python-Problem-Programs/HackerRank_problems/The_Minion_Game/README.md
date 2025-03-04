# The Minion Game

### Problem Statement  
Kevin and Stuart play a game with a string `S`:  

- **Kevin** scores by making words that start with **vowels** (`A, E, I, O, U`).  
- **Stuart** scores by making words that start with **consonants**.  
- Each **occurrence** of a substring in `S` adds to the player's score.  
- The game ends when all possible substrings are counted.  

### Scoring Example  
Given `S = BANANA`:  
- Kevin's words (starting with vowels): `ANA`, `ANANA`, etc.  
  - `ANA` appears **twice**, so Kevin gets **2 points**.  
- Stuart's words (starting with consonants): `BANA`, `BAN`, etc.  

### Function Definition python
def minion_game(string):
    pass  # Your code here

**Parameters:**  
- `string`: A string `S` (only uppercase letters).  

**Prints:**  
- `"Winner Score"` (e.g., `"Stuart 12"`) or `"Draw"` if tied.  

### Input Format  
A **single string** `S`.  

### Constraints  
- `0 < len(S) < 10^6`  

### Example  

#### Input
```
BANANA
```

#### Processing  
- **Kevin (Vowels: A)** → Possible substrings: `"A", "AN", "ANA", "ANAN", "ANANA", ...`  
- **Stuart (Consonants: B, N)** → Possible substrings: `"B", "BA", "BAN", ...`  

#### Output
```
Stuart 12
```

### Hints 
- **Count occurrences efficiently** instead of generating all substrings.  
- **Each letter contributes based on its position**:
  - `"B"` at index `0` appears in `6` substrings (`BANANA, BANAN, BANA, BAN, BA, B`).
  - `"A"` at index `1` appears in `5` substrings (`ANANA, ANAN, ANA, AN, A`).  
- Compute **Kevin’s and Stuart’s scores** in a **single loop**.  
