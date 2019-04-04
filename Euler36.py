# 585 = 1001001001 is palindrome in base 10 and 2
# Find the sum of all numbers, less than one million, which are double-base palindromes in 10 and 2
# No leading zeroes

def is_palindrome (s):
    return s == ''.join(reversed(s))

count = 0
total = 0
for i in range (1000000):
    dec_string = str(i)
    if (is_palindrome(dec_string)):
        binary_string = "{0:b}".format(i)
        if (is_palindrome(binary_string)):
            print ((i, binary_string))
            count += 1
            total += i
print (count)
print (total)
