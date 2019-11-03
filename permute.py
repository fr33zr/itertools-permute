from itertools import permutations

input1 = input("Enter a word to receive all the possibilities!! > ")
input1 = [''.join(z) for z in permutations(input1)]

print (input1)
print (len(input1))
