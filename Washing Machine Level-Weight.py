'''A washing machine works on the principle of Fuzzy System, the weight of clothes put 
inside it for washing is uncertain but based on weight measured by sensors and the water 
level chosen, it decides total time needed. 
For low level water, the time estimate is 25 minutes, where approximately weight is 
between 2000 grams or any nonzero positive number below that.
For medium level water, the time estimate is 35 minutes, where approximately weight is 
between 2001 grams and 4000 grams.
For high level water, the time estimate is 45 minutes, where approximately weight is 
above 4000 grams. Assume the capacity of machine is maximum 7000 grams. 
When the weight is zero, time needed is 
0
minutes. 
If the weight exceeds maximum weight limit, then, print “OVERLOADED”, and for all 
negative weights, the output is “INVALID INPUT”.
Sample Input-1: 2000, L
Sample Output-1: Time Estimated: 25 minutes
Input should be in the form of integer value. 
Output must have the following format: Time Estimated: NN Minutes
'''



k=input().strip() #Remove trailing whitespaces
parts=k.split(',') # Split the string based on ',' into list

#Check for list only having two parts
if len(parts)!=2:
    print("INVALID INPUT")
else:
    n=int(parts[0]) #Getting weight 
    waterLevel=parts[1].upper() # Getting the water level
    if n<0:
        print("INVALID INPUT")
    elif n==0:
        print("Time Estimated : 0 minutes")
    elif n>7000:
        print("OVERLOADED")
    else:
        if waterLevel=='L' and n<=2000:
            print("Time Estimated : 25 minutes")
        elif waterLevel =='M' and n>=2001 and n<=4000:
            print("Time Estimated : 35 minutes")
        elif waterLevel =='H' and n>=4001 and n<=7000:
            print("Time Estimated : 45 minutes")
        else:
            print("INVALID INPUT")