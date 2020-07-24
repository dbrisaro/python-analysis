#!/usr/bin/env python3

def merge(L1, L2):          # apareo
    i = 0
    j = 0
    l1 = len(L1)
    l2 = len(L2)
    L = [0] * (l1+l2)
    for k in range(l1+l2):
        if (j>=l2 or (i<l1 and L1[i]<L2[j])):
            L[k] = L1[i]
            i = i+1
        else:
            L[k] = L2[j]
            j = j+1
    return L

def main():
    L1 = [-63, -62, -57, -51, -26, -22, -21, 4, 16, 35, 35, 38, 43, 56, 63, 65, 66, 74, 93, 99]
    L2 = [-72, -41, -20, -19, -8, 8, 20, 35, 58, 80]
    L = merge(L1,L2)
    print(L)

if __name__ == "__main__":
    main()
