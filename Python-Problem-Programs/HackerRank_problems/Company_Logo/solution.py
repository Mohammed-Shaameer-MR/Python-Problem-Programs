from collections import Counter

if __name__ == '__main__':
    s = input()
    occs=Counter(s)

    sorted_occs=sorted(occs.items(),key=lambda x:(-x[1],x[0]))
    for i in sorted_occs[:3]:
        print(f"{i[0]} {i[1]}")
