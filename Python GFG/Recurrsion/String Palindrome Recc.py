def reccPal(S):
    if len(S) <= 1:
        return True
    else:
        if S[0] == S[-1]:
            return reccPal(S[1:-1])
        else:
            return False


Say = str(input("Enter any String : "))
Say = Say.lower()
print("Converting it to LoweCase : ", Say)
if reccPal(Say) == True:
    print("Yes !! Its is a Palindrome")
else:
    print("Nope !! Not a Palindrome")
