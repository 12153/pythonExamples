def permutations(s, k):
      if k <= 1:
            return s

      l = []
      for i in permutations(s, 1):
            for j in permutations(s, k - 1):
                  l.append(i+j)

      return l

if __name__ == "__main__":
      print(*permutations("ab", 4))
      print(*permutations("abc", 3))