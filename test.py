# O(n) is always proportional
def printList(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


# printList(9)

# O(1)
def sumNum(n):
    return n + n + n
print(sumNum(9))

# O(a+b)
def printList(n,m):
    for i in range(n):
            print(i)

    for j in range(m):
        print(j)
