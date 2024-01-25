# bài 2a
# Define a list of numbers
numbers = [75, 150, 145]

# Display numbers from the list using a loop
for number in numbers:
    # Check if the number is divisible by five
    if number % 5 == 0:
        # If the number is greater than 500, stop the loop
        if number > 500:
            print(f"Stopping the loop at {number} because it is greater than 500.")
            break
        # If the number is greater than 150, skip it and move to the next number
        elif number > 150:
            print(f"Skipping {number} as it is greater than 150.")
            continue
        # Display the number
        else:
            print(number)
            
#bài 2b
tr =  input("string:")

numberOfLetters = 0
numberOfDigits = 0
numberOfOthers = 0
for i in range (len(str)):
    if('0' <= str[i] and str[i] <= '9') : numberOfDigits +=1
    elif(('a' <= str[i] and str[i] <= 'z') or ('A' <=str[i] and str[i] <= 'Z')): numberOfLetters +=1
    else: numberOfOthers +=1
    
print(numberOfLetters)
print(numberOfDigits)
print(numberOfOthers)


#bài 2c
# Define a list
my_list = [10, 20, 30, 40, 50]

# Print the list in reverse order using a loop
for i in range(len(my_list) - 10, -10, -10):
    print(my_list[i])

