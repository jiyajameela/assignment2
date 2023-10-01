###############1
#having the value of length from the user
zander_length = int(input("enter the length of the zander in centimeters: "))
size_limit = 100
if zander_length >= size_limit :
    print("congrats! the zander is of appropriate size , you may keep the fish")
else:
#calculate how many centimeters is zander below  the size limit
 centimeters_below_limit = size_limit - zander_length
 print ( f'the zander is {centimeters_below_limit} centimeters below the limit and please release the fish back into the lake now.')

###############2
# Get the cabin class from the user
cabin_class = input("Enter the cabin class (LUX, A, B, or C): ")

# Check the cabin class and help them according to their needs
if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("Above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Error: Invalid cabin class.")

#############3
# DEFINING THE normal hemoglobin ranges with a dictionary
normal_ranges = {
    'F': {'low': 117, 'high': 155},
    'M': {'low': 134, 'high': 167}
}

# Get biological gender and hemoglobin value from the user
gender = input("Enter biological gender (F for female, M for male): ").upper()

if gender not in normal_ranges:
    print("Invalid input for gender. Please enter 'F' for female or 'M' for male.")
else:
    # Get hemoglobin value from the user
    hemoglobin_value = float(input("Enter hemoglobin value (g/l): "))

    # give them a proper update after checking the hemoglobin values
    if normal_ranges[gender]['low'] <= hemoglobin_value <= normal_ranges[gender]['high']:
        print("Hemoglobin level is normal.")
    elif hemoglobin_value < normal_ranges[gender]['low']:
        print("Hemoglobin level is low.")
    else:
        print("Hemoglobin level is high.")

 ##############4
 # Get the year from the user
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#############5

# Initialize a variable to start the loop
number = 1

# Use a while loop for the numbers from the range of  1 to 1000
while number <= 1000:
    # Check if the number is divisible by 3
    if number % 3 == 0:
        # Print the number if divisible by 3
        print(number)
    # Move to the next number
    number += 1

############6
# Infinite loop to keep converting until a negative value is entered
while True:
    # Get input from the user
    inches = float(input("Enter inches (or a negative value to end): "))

    # Check if the input is negative, if so, end the program
    if inches < 0:
        print("Program HAS BEEN ended.")
        break

    # Convert inches to centimeters
    centimeters = inches * 2.54

    # Print the result
    print(f"{inches} inches is equal to {centimeters} centimeters.")

###########7

import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Game loop
while True:
    # Get user's guess
    user_guess = int(input("Enter your guess (between 1 and 10): "))

    # Compare the user's guess with the random number
    if user_guess < random_number:
        print("Too low! Try again.")
    elif user_guess > random_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! The number was {random_number}. You guessed it!")
        break




