import itertools
def permutations(elements):
    permutatedList = list(itertools.permutations(elements))
    print(permutatedList)
    print(len(permutatedList))
    for(x)

userInput = input("Enter space separated value:")
elements = userInput.split(" ")
permutations(elements)