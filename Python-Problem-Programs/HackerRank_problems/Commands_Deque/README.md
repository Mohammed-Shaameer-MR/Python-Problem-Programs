## Deque Commands

## Problem Statement

Perform `append`, `pop`, `popleft`, and `appendleft` methods on an empty deque `d`.

## Input Format

1. The first line contains an integer `N`, representing the number of operations.
2. The next `N` lines contain space-separated names of methods and their values.

## Constraints

- $$\( 0 < N < 100 \)$$

## Output Format

Print the space-separated elements of deque `d`.

## Example

### **Input**
```
6
append 1
append 2
append 3
appendleft 4
pop
popleft
```

### Processing
- `append 1` → `d = [1]`
- `append 2` → `d = [1, 2]`
- `append 3` → `d = [1, 2, 3]`
- `appendleft 4` → `d = [4, 1, 2, 3]`
- `pop` → `d = [4, 1, 2]`
- `popleft` → `d = [1, 2]`

### **Output**
```
1 2
```

## Hints

- Use `collections.deque` in Python to efficiently perform operations.
- `append()` adds an element to the right end.
- `appendleft()` adds an element to the left end.
- `pop()` removes and returns an element from the right end.
- `popleft()` removes and returns an element from the left end.