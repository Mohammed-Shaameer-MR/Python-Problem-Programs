import os

def solve(s):
    x=s.strip().split(' ')
    for i in range(len(x)):
        if x[i] and x[i][0].isalpha():
            x[i]=x[i].capitalize()
    return ' '.join(x)
    
    
    
if __name__ == '__main__':
    # This code uses the OUTPUT_PATH provided by HackerRank to write the output to the correct file location so no open(output.text,'w') gets used.

    fptr = open(os.environ['OUTPUT_PATH'], 'w') #

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()