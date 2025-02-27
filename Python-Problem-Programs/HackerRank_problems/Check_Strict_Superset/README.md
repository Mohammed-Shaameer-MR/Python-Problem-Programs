# Strict Superset

### Problem Statement  
You are given a set **A** and **n** other sets. Your job is to find whether set **A** is a strict superset of each of the **n** sets.

A strict superset has at least one element that does not exist in its subset.

### Function Description  
Implement the function `check_strict_superset(A, n, other_sets)`, which:  
- Takes a set **A**, a number **n** representing the number of other sets, and a list of **n** sets (`other_sets`).  
- Returns `True` if **A** is a strict superset of each of the **n** sets, otherwise returns `False`.

### Input Format  
The input consists of multiple lines:  
1. The first line contains space-separated elements representing the set **A**.  
2. The second line contains an integer **n**, the number of other sets.  
3. The next **n** lines contain space-separated elements for each of the other sets.  

### Constraints  
- `0 < len(set(A)) < 501`  
- `0 < N < 21`  
- `0 < len(otherSets) < 101`

### Output Format  
- Print `True` if **A** is a strict superset of all the other sets. Otherwise, print `False`.

### Example  
#### Input
```
1234567 8 9 10 11 12 23 45 84 78
2
12345
100 11 12
```

#### Processing
- **Set A**: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 78, 84}
- **Set 1**: {1, 2, 3, 4, 5}
- **Set 2**: {100, 11, 12}

- **Set A** is a strict superset of **Set 1** but not of **Set 2** because **100** is not in **Set A**.

#### Output
```
False
```

### Hints  
- Use Python's set operations (`>`, `issuperset()`, etc.) to check if one set is a strict superset of another.  
- Remember that a strict superset means the set must contain all elements of the subset, and at least one element in the superset is not in the subset.
