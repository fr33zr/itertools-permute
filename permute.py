from itertools import permutations

#Define function
def permute():
        #Take user input
        inputPerm = input("What would you like me to permute? > ")
        #Concatenates the would be seperated listed letters, and turns them into words
        inputPerm = [''.join(z) for z in permutations(inputPerm)]
        #prints the output to the terminal
        print ("[*] Number of outcomes are printed below [*]")
        print (len(inputPerm))
        print (inputPerm)
permute()


