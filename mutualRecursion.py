def f(n):
      if n == 0:
            return n

      print(n, "f")
      return z(n - 1)

def z(n):
      if n == 0:
            return n

      print(n, "z")
      return f(n-1)

f(50)