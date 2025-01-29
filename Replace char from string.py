#Replace character from a string

org= input("Enter the original string: ")
replace = input("Enter the character to replace: ")
replacement = input("Enter the replacement character: ")

# Finding index of replace
target =org.find(replace)

#Getting the replaced string
if target == -1:
    print(f"The character '{replace}' was not found in the string.")
else:
    string = ""
    for i in org:
        if i == replace:
            string += replacement  #Character gets replaced
        else:
            string += i  #Rest of the string
    print(f"Original string: {org}")
    print(f"Modified string: {string}")

