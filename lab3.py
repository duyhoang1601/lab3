# bài 1a
string = 5  

for i in range(1, string + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    
# bài 1b 
max_number = int(input("Enter a positive integer: "))
sum_numbers = 0
for number in range(1, max_number + 1):
    sum_numbers += number
print(f"The sum of all numbers from 1 to {max_number} is: {sum_numbers}")
