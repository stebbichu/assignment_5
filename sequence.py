n = int(input("Enter the length of the sequence: ")) # Do not change this line
# Design an algorithm that generates the 
# first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, 

sum = 0                                     
first_num, sec_num, third_num = 1, 0, 0
#let's design a for loop to run the sequence
for i in range(n):
    #add the numbers to get the sum
    sum = first_num + sec_num + third_num
    #print the sum
    print(str(sum))
    #replace the old numbers
    if i == 0 or i == 1:
        sec_num = first_num
        first_num = sum
    else:
        third_num = sec_num
        sec_num = first_num
        first_num = sum
