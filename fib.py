def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

def fib(n):
    if n <= 1:
        return n

    z = fib(n - 1) + fib(n - 2)
    return z


if __name__ == "__main__":
    print(fib(5))