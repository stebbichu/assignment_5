num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0
# We will promt the user for numbers until he inputs a negative number
while num_int >= 0:
    #if the number is higher it replaces the old number
    if num_int > max_int:
        max_int = num_int
    #user inputs another number,
    num_int = int(input())
    

print("The maximum is", max_int)    # Do not change this line
