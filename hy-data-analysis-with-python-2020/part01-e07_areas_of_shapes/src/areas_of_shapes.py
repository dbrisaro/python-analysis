#!/usr/bin/env python3

import math

# Create a program that can compute the areas of three shapes, triangles,
# rectangles and circles, when their dimensions are given.
# An endless loop should ask for which shape you want the area be calculated.
# An empty string as input will exit the loop. If the user gives a string
# that is none of the given shapes, the message “unknown shape!”
# should be printed. Then it will ask for dimensions for that particular shape.
# When all the necessary dimensions are given, it prints the area, and starts
# the loop all over again. Use format specifier f for the area.

def main():
    # enter you solution here
    condition = True

    while condition:
        shape = input('Choose a shape (triangle, rectangle, circle): ')

        if shape=='':
            condition = False

        elif shape=='triangle':
            base = float(input('Give base of the triangle: ' ))
            height = float(input('Give height of the triangle: '))
            area = base*height/2
            print('The area is', '{:6f}'.format(area))

        elif shape=='rectangle':
            base = float(input('Give base of the rectangle: ' ))
            height = float(input('Give height of the rectangle: '))
            area = base*height
            print('The area is', '{:6f}'.format(area))

        elif shape=='circle':
            r = float(input('Give radius of the circle: '))
            area = math.pi*r**2
            print('The area is', '{:6f}'.format(area))

        else:
            print(f'Unknown shape!')



if __name__ == "__main__":
    main()
