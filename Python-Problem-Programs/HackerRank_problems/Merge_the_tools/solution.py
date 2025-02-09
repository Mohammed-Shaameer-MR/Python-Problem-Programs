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