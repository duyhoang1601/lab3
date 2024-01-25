str =  input("string:")

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