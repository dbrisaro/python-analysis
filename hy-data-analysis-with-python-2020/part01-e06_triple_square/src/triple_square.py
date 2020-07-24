#!/usr/bin/env python3

# Write two functions: triple and square. Function triple multiplies its parameter by three.
# Function square raises its parameter to the power of two. For example,
# we have equalities triple(5)==15 and square(5)==25.
# Now modify this for loop so that it stops iteration when the square of a value
# is larger than the triple of the value, without printing anything in the last iteration.

def triple(param):
    return param*3

def square(param):
    return param**2

def main():

    for i in range(1,11):
        sq = square(i)
        tr = triple(i)

        if sq <= tr:
             print(f'triple({i})=={tr} square({i})=={sq}')
        else:
            break

if __name__ == "__main__":
    main()
