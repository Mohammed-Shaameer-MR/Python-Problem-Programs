

n = int(input("Enter a no: "))

div = 0
if n<=1:
    print("Its not a Prime no")
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            div += 1         
    if div == 2:
        print("Its a Prime no")
    else:
        print("Its not a Prime no")