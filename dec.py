
def dec(n):
    p = n // 2
    r = str(n % 2)

    if p == 0:
        return r
    return dec(p) + r

    
if __name__ == "__main__":
    print(dec(233))
