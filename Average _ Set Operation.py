'''
Ms. Gabriel Williams, a botany professor at District College, asked her student Mickey to compute the average height of all distinct plants in her greenhouse. The goal is to determine the average by considering only the unique heights of the plants. The formula used for this calculation is:

Average = (Sum of Distinct Heights) / (Total Number of Distinct Heights)

To accomplish this, the function average needs to be implemented. This function takes a list of integers, arr, representing plant heights as input and returns the computed average as a floating-point value rounded to three decimal places.

The input format consists of two lines. The first line contains an integer, N, which denotes the number of elements in the list. The second line contains N space-separated integers representing the plant heights. The constraints specify that N is greater than zero but less than 100.

For example, given an input where N = 10 and the heights are 161 182 161 154 176 170 167 171 170 174, the distinct heights extracted from the list are {154, 161, 167, 170, 171, 174, 176, 182}. The sum of these distinct heights is 1355, and since there are 8 unique values, the computed average is 1355 / 8 = 169.375.

Thus, the expected output for this sample case is 169.375. The implementation should use Python's built-in set() function to extract unique values, followed by sum() and len() to compute the average efficiently.
'''

#Code:-

def average(array):
    h=set(array)
    avg=sum(h)/len(h)
    return avg
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)