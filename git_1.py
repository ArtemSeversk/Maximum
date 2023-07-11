def Palindrome(string):
    foo = str(string)
    if foo[::-1].startswith(foo):
        return True
    else:
        return False
print(Palindrome('рассвет'))