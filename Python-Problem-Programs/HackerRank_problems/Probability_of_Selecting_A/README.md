# Probability of Selecting 'a'

## Problem Description

Given a list of lowercase English letters, we select `K` indices randomly. We need to compute the probability that at least one of the selected indices contains the letter `'a'`.

## Formula

Probability = (Favorable cases) / (Total cases)

## Input Format

1. The first line contains an integer `N`, the length of the list.
2. The second line contains `N` space-separated lowercase English letters.
3. The third line contains an integer `K`, the number of indices to be selected.

## Output Format

Output a single line containing the probability, rounded to 3 decimal places.

## Constraints

- 0 < N <= 10
- 0 < K <= N
- All letters in the list are lowercase English letters.

## Example

### Input
```
4
aacd
2
```

### Processing
- Possible selections of `K=2` indices from `{1, 2, 3, 4}`:  
  `(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)`
- Favorable cases where at least one `'a'` is present:  
  `{(1, 2), (1, 3), (1, 4), (2, 3), (2, 4)}` → 5 cases
- Total cases = 6
- Probability = `5/6 = 0.8333`

### Output
```
0.833
```

## Hints
- Use combinatorics to determine possible index selections.
- Count the number of selections containing at least one `'a'`.
- Ensure precision up to 3 decimal places.
