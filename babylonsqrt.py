# Don't change these lines
number = int(input("Find the square root of integer: "))
guess = int(input("Initial guess: "))
tolerance = float(input("What tolerance: "))

# Implement the Babylonian square root algorithm
#let n be the number for which to find the square root
#let g be the initial guess
#let t be the tolerance
#let g' be our previous guess, initialized to 0
#while the absolute difference between g and g' is greater than t
#  g' = g
#  g = average of n/g and g
count = 0
previous = 0
while abs(previous - guess) > tolerance:
    previous = guess
    quotient = number/guess
    guess = (quotient+guess)/2
    count += 1


# Don't change these lines
print("Square root of", number, "is", round(guess, 4))
print("Took", count, "reps to get it to tolerance")
