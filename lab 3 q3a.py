#Q3a
def get_middle_four_chars(str1):
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)

    # use string slicing to get result characters
    res = str1[mi - 2:mi + 2]
    print("Middle four chars are:", res)

get_middle_four_chars("Billdesctran")
get_middle_four_chars("HoSongHu")




