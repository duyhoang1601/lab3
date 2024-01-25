# lab3b1
def are_anagrams(str1, str2):
    # Remove white space and punctuation from the strings
    clean_str1 = ''.join(char.lower() for char in str1 if char.isalnum())
    clean_str2 = ''.join(char.lower() for char in str2 if char.isalnum())

    # Check if the cleaned strings are anagrams
    return sorted(clean_str1) == sorted(clean_str2)

# Example usage
string1 = "parliament"
string2 = "partial men"
result = are_anagrams(string1, string2)

if result:
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
    
#lab3b2
def hex_to_decimal(hex_string):
    try:
        decimal_value = int(hex_string, 16)
        return decimal_value
    except ValueError:
        return None

# Read a string from the user
user_input = input("Enter a string: ")

# Check if all characters are hexadecimal digits
if all(char.isdigit() or char.lower() in 'abcdef' for char in user_input):
    # Convert the hexadecimal string to base-10
    result = hex_to_decimal(user_input)
    if result is not None:
        print(f"The base-10 value of '{user_input}' is: {result}")
    else:
        print("Error: Invalid hexadecimal string.")
else:
    print("Error: The input contains non-hexadecimal characters.")

