#Q4a
str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)
res = "".join([item for item in str1 if item.isdigit()])
print(res)

#Q4b
import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)

#Q4c
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = []
for s in str_list:
    if s:
        res_list.append(s)
print(res_list)

#Q4d
str1 = "Emma-is-a-data-scientist"
print("Original String is:", str1)

sub_strings = str1.split("-")

print("Displaying each substring")
for sub in sub_strings:
    print(sub)
