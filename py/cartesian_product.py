# CS350 Spring 2018 Seth Lewis

"""
    Since elements of Python sets must be immutable,
    a Python set cannot contain Python sets.
    For example, a power set cannot be represented using Python sets.

    So we will simulate a set using lists.
    For example, [[1,2], [1,3]] represents the set {{1,2}, {1,3}}.
    This works, since lists do not have the immutability constraint.
"""

import random


def randomSet(n, up):
    """Build a random 'set' of integers.

    Be sure to guarantee the key property of a set: no duplicates.

    >>> randomSet(4, 10)
    [5, 3, 2, 8]

    Params: 
        n (int): # of integers in the set
        up (int): upperbound 
    Returns: (list) random 'set' of n integers between 0 and up, inclusive
    """

    # L = random.sample(range(up), n)
    L = []
    end_list = 0
    while end_list < n:  # repeats do not create shorter sets
        number = random.randint(0, up)
        if number not in L:  # equivalent to "if x != number for all x in L then true"
            end_list += 1
            L.append(number)

    '''
    for x in range(n):  # repeats will lead to shorter sets
        number = random.randint(0, up)
        if number not in L:
            L.append(number)
    '''

    return L


def cartesianProduct(A, B):
    """Build the Cartesian product of the two sets A and B.

    >>> cartesianProduct([1,2], [3, 4])
    [(1,3), (1,4), (2,3), (2,4)]
    
    Params: 
        A (list): set of integers, represented internally as a list
        B (list): set of integers, represented internally as a list
    Returns: (list) Cartesian product AxB, 
                    represented internally as a list of tuples
    """

    L = []
    for x in A:
        for y in B:
            L.append((x, y))
    # L = [(x, y) for x in A for y in B]  # just learned about one line function calls, used nested loops for clarity
    return L


def printSet(L):
    """Print a 'set', using standard set notation.
    To restore the correct interpretation, this function prints the 'set'
    in true set notation.
    Hint: you can print without adding a newline (see print documentation)

    >>> printSet([1,2,3,4])
    {1, 2, 3, 4}

    >>> printSet([(1,2), (1,3)]
    {(1,2), (1,3)}
    
    Params: A (list): set of integers
    """

    string = str(L)

    def replaceCharacter(s):  # could not figure out how to work on lists then discovered python has inner function
        if s == '':
            return ''
        if s[0] == '[':
            return '{' + replaceCharacter(s[1:])
        if s[0] == ']':
            return '}' + replaceCharacter(s[1:])
        return s[0] + replaceCharacter(s[1:])

    print(replaceCharacter(string))

    '''
    print(str(L).replace("[", "{").replace("]", "}"))
    '''

    return


# an example of a test call
A = randomSet(5, 100)
B = randomSet(5, 100)
print("The Cartesian product of ")
printSet(A)
print("and")
printSet(B)
print("is")
printSet(cartesianProduct(A, B))
