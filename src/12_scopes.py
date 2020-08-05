# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def changeX():
    x = 99

changeX()

print(f'x local scope: {x}')
# This prints 12. What do we have to modify in changeX() to get it to print 99?
def changeX():
    global x
    x = 99


changeX()

print(f'x global scope: {x}')


# This nested function has a similar problem.
def outer():
    y = 120

    def inner():
        nonlocal y # ANSWER: declare y as a nonlocal variable
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".
    print(y)

outer()