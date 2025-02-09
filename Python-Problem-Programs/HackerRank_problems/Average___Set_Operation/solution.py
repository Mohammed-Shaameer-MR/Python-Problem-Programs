def average(array):
    h=set(array)
    avg=sum(h)/len(h)
    return avg
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)