import itertools

def strperm(string):
    #your code here
    return list(set(map("".join, itertools.permutations(string))))
