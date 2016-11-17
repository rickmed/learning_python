someVar = 'a string'

help("a string".join)  # help on a built-in method

'''
multi line comment
'''

print(dir(someVar))  # shows all object's attributes

print(someVar)

print(
    '''%c is my fav letter, %s is my fav string, %d is my fav number,
%.6f is my fav 3 decimal float'''
    % ('R', 'pizza', 20, 0.453))
