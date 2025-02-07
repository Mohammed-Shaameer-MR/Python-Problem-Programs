'''
You are given an array of 𝑛 integers and two disjoint sets, 𝐴 and 𝐵, each containing 𝑚 integers. You like all the integers in set 𝐴 and dislike all the integers in set 𝐵. 
Your initial happiness is 0. For each integer in the array, if it belongs to set 𝐴 you gain 1 happiness. If it belongs to set B, you lose 1 happiness. If it is in neither set, your happiness remains unchanged. At the end, you must output your final happiness score.

The constraints are as follows: 
->1 ≤ n ≤ 10^5
->1 ≤ n ≤ 10^5
->1< any integer in the input <10^9

The input consists of four lines. The first line contains two integers, 𝑛 and 𝑚, separated by a space. The second line contains 𝑛 integers representing the elements of the array. The third and fourth lines contain 𝑚 integers each, representing sets A and 𝐵, respectively. The output is a single integer representing your total happiness.

For example, if the input is:
3 2
1 5 3
1 3
5 7

The output will be:
1

In this case, you gain 1 happiness for elements 1 and 3 since they belong to set 𝐴.

You lose 1 happiness for element 5, which belongs to set 𝐵.

The element 7 is not in the array, so it does not affect happiness. The total happiness is calculated as 2−1=1

'''

#Code:-

import sys

#Get the data
n,m=(int(x) for x in input().strip().split(' '))
arr=[int(x) for x in sys.stdin.readline().split()]
like={int(x) for x in sys.stdin.readline().split()}
unlike={int(x) for x in sys.stdin.readline().split()}

#Happiness container
happy=0

#Checking for happiness
for i in arr:
    if i in like:
        happy+=1
    elif i in unlike:
        happy-=1
    else:
        continue

#Display Happiness
print(happy)