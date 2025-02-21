# Word_Order

You are given `n` words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond to the first appearance of each word in the input.  

## Input Format  
1. The first line contains the integer `n`.  
2. The next `n` lines each contain a word.  

## Constraints  
-**1 <= n <= 10^5**  
- The sum of the lengths of all words does not exceed \( 10^6 \).  
- All words consist of lowercase English letters only.  

## Output Format  
Output **two lines**:  
1. The number of distinct words.  
2. The number of occurrences of each distinct word, in order of their first appearance.  

## Example  

### Input:
4
bcdef
abcdefg
bcde
bcdef

### Processing:  
- `bcdef` appears first.  
- `abcdefg` is a new word.  
- `bcde` is also new.  
- `bcdef` appears again.  

The distinct words in order:  
- `bcdef` (2 times)  
- `abcdefg` (1 time)  
- `bcde` (1 time)  

### Output:
3
2 1 1