def checkPalindrome(n):
    rev = 0
    dup = n
    while n > 0:
        temp = n % 10
        rev = (rev * 10) + temp
        n = n // 10

    if dup == rev:
        return True
    else:
        return False

n = int(input("Enter the number: "))

if checkPalindrome(n):
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")
