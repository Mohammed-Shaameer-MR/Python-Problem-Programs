import sys

#Getting the sets
a={int(x) for x in sys.stdin.readline().split()}

n=int(input())
subsets=[{int(i) for i in lines.split()} for lines in sys.stdin.read().splitlines()]

result=all(a>subsets[i] for i in range(len(subsets)))

print(result)
    
