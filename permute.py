from itertools import permutations

input1 = input("Enter a word to receive all the possibilities!! > ")
input1 = [''.join(z) for z in permutations(input1)]

print (input1, "\n")
print ("[*] Number of outcomes are printed below [*]")
print (len(input1))
