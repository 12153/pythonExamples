def strRev(s):
    if s == "":
        return ""

    return strRev(s[1:]) + s[0]

if __name__ == "__main__":
    print(strRev("hello, WeThinkCode"))