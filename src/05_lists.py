# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
for fish in y: 
    x.append(fish)
print(x)
#when using a for loop the i is already iterating

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.pop(4)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE

x.insert(5,x[4]*11)
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))
# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for fish in x:
    print(x[fish-1]*1000)
