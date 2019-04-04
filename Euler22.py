total = 0

with open("p022_names.txt") as f:
    names = [ i.strip('"') for i in f.read().split(',') ]
    names.sort()
   
    for index, name in enumerate(names):
        total += (index + 1) * sum ( ord(i) - ord('A') + 1 for i in name ) 

print (total)

