def sumOf(n):
      if n == 1: return 1
      return n + sumOf(n - 1)

# def sumOf(n):
#       total = 0
#       for i in range(n + 1):
#             total += i
#       return total

def sum(n):
      return (n * (n + 1))//2

if __name__ == "__main__":
      print(sumOf(5))
      print(sumOf(10))
      print(sumOf(15))


