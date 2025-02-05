'''
Consider the following: A string, s, of length n, where s = C₀C₁...Cₙ₋₁. An integer, k, where k is a factor of n.

We can split s into substrings, where each substring tᵢ consists of a contiguous block of k characters in s. Then, use each tᵢ to create a string uᵢ such that:

The characters in uᵢ form a subsequence of tᵢ.

Any repeated occurrence of a character is removed such that each character in uᵢ appears exactly once. In other words, if a character at some index j in tᵢ has appeared at a previous index < j, it is not included in uᵢ.


Given s and k, print n/k lines, where each line i contains string uᵢ.

For example, given s = "AAABCADDE" and k = 3, there are three substrings of length 3: "AAA", "BCA", and "DDE". The first substring consists of only the character 'A', so u₁ = "A". The second substring contains all distinct characters, so u₂ = "BCA". The third substring has two unique characters, so u₃ = "DE".

The order of characters in each subsequence is important, as it maintains the order in which they first appear.

Function Description

Complete the merge_the_tools function.

merge_the_tools has the following parameters:

string s: the input string

int k: the size of each substring


Prints: Each uᵢ on a new line. There will be n/k lines in total. The function does not return anything.

Input Format

The first line contains a single string, s.
The second line contains an integer, k, representing the length of each substring.

Constraints

1 ≤ n ≤ 10⁴, where n is the length of s.

1 ≤ k ≤ n.

It is guaranteed that n is a multiple of k.


Sample Input

AABCAAADA
3

Sample Output

AB
CA
AD

Explanation

We split s into n/k = 9/3 = 3 equal parts of length k = 3. Then, we remove duplicate characters while maintaining their first occurrence in each substring:

1. t₀ = "AAB", after removing duplicates → u₀ = "AB"


2. t₁ = "CAA", after removing duplicates → u₁ = "CA"


3. t₂ = "ADA", after removing duplicates → u₂ = "AD"



Each uᵢ is printed on a new line.
'''

#Code:-

import textwrap

def merge_the_tools(string, k):
    #parts=[string[i:i+k] for i in range(0,len(string),k)]  #Logical method
    parts=textwrap.wrap(string,k)  #Library function method
    for i in range(len(parts)):
        parts[i]="".join(dict.fromkeys(parts[i]))
        print(f"{parts[i]}")

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)