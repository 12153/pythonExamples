def sum(n):
      if n == 0:
            print("base case has been reached, n =", n)
            return n

      print("n =", n)
      return sum(n - 1) + n

if __name__ == "__main__":
      print(sum(5))