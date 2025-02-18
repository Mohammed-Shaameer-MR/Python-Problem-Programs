import sys

n=int(input())
names=input().split()
data=sys.stdin.read().splitlines()
print(f"{(sum(int(line.split()[names.index("MARKS")]) for line in data)/n):.2f}")
