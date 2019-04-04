# Euler problem 42

import csv

import math 
def is_triangular(num):
    x = math.sqrt(2 * num)
    return 2 * num == int(x) * int(x + 1)

count = 0

with open('p042_words.txt') as csvfile:
    reader = csv.reader(csvfile)
    for word in (x for row in reader for x in row):
        num_value = sum(ord(ch) - ord('A') + 1 for ch in word)
        if (is_triangular(num_value)):
            count = count + 1

print(count)

print (sum(ord(ch) - ord('A') + 1 for ch in 'SKY'))

print (is_triangular(55))
