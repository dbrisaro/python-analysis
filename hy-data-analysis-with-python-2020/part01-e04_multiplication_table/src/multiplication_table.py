#!/usr/bin/env python3


def main():
    for i in range(1,11):     # filas

        for j in range(1,10): # columnas

            print('{:4d}'.format(i*j), end="")

        print('{:4d}'.format(i*10))



if __name__ == "__main__":
    main()
