def strSub(st, curr="", index=0):
    n = len(st)

    if index == n:
        print(curr, " ")
        return

    strSub(st, curr, index + 1)
    strSub(st, curr + st[index], index + 1)


if __name__ == "__main__":
    say = str(input("Enter any Word : "))
    say = say.lower()
    print("Converting to lowercase")
    print(say)

    print("Subsets of the word ", "'", say, "'", " are ")
    print(strSub(say))
