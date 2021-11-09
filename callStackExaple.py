def fourth():
    return "Code"

def third():
    return "Think" + fourth()

def second():
    return "We" + third()

def first():
    return "hello, " + second()


if __name__ == "__main__":
    print(first())