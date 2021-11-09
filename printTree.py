def printTree(n, s):
      if n == 1:
            print("base case: ", n, s)
            return

      print(n, s)
      printTree(n - 1, "left")
      printTree(n - 1, "right")

if __name__ == '__main__':
      printTree(3, "top")