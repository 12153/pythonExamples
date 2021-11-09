def printUp(n, k):
    if n == k:
        return

    print(n)
    printUp(n + 1, k)

def printDown(n, k):
    if n == k:
        return

    printDown(n + 1, k)
    print(n)

if __name__ == "__main__":
    printUp(0, 10)
    printDown(0, 10)