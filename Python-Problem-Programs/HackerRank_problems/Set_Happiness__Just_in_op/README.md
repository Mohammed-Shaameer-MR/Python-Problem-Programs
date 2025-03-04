# Happiness Score Calculation  

### Problem Statement  
You are given an array of **n** integers and two disjoint sets, **A** and **B**, each containing **m** integers. Your happiness starts at **0**, and:  
- You **gain** `+1` happiness for each integer in **A**.  
- You **lose** `-1` happiness for each integer in **B**.  
- Integers not present in **A** or **B** do **not** affect happiness.  

At the end, you must **output your final happiness score**.  

### Input Format  
1. The first line contains **two integers** `n` and `m`, separated by a space.  
2. The second line contains **n integers**, representing the elements of the array.  
3. The third line contains **m integers**, representing set **A** (liked integers).  
4. The fourth line contains **m integers**, representing set **B** (disliked integers).  

### Constraints  
- `1 ≤ n ≤ 10⁵`  
- `1 ≤ m ≤ 10⁵`  
- `1 < any integer in the input < 10⁹`  

### Output Format  
- Print a **single integer**, the final happiness score.  

### Example  

#### Input
```
3 2  
1 5 3  
1 3  
5 7  
```

#### Processing  
- **Array**: `[1, 5, 3]`  
- **Set A** (Liked): `{1, 3}`  
- **Set B** (Disliked): `{5, 7}`  

Calculation:  
- `1` is in **A** → `+1` happiness  
- `5` is in **B** → `-1` happiness  
- `3` is in **A** → `+1` happiness  
- `7` is **not** in the array → No change  

Final happiness score: **`1`**  

#### **Output**  
```
1  
```

### Hints  
- Use **sets** for quick lookups (`O(1)` time complexity).  
- Iterate through the array and update happiness accordingly.  
- Avoid using nested loops to handle large constraints efficiently.  
