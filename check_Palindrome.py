def Palindrome(str_,rev_str):
    str_=str(str_)
    rev = str(str_[::-1])
    if rev == rev_str:
        print(f"{str_} and {rev_str} are palindrome of each other")
    else:
        print(f"{str_} and {rev_str} are not palindrome of each other")
    return ""
print("------Enter the string in the input section------")
str_=input("Enter the frist string to check: ")
rev_str=input("Enter the second string to check: ")
print(Palindrome(str_,rev_str))
print("THANKYOU FOR USING THE PROGRAM !!!")
