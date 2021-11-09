def countFromNToK(n, k):
    if n == k:
        return

    print(n)
    countFromNToK(n+1, k)

if __name__ == "__main__":
    countFromNToK(0, 10)