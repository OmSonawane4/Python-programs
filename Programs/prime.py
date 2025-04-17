n = int(input("Enter a number- "))
if n == 0 or n == 1:
    print("Enter another number")
elif n > 1:
    for i in range(2,n):  for(i = 0; i<n;i++)
        if (n % i) == 0:
            print(n, "is not a prime no.")
            print(n, "appears", i, "times in" ,n//i)     
            break
else:
    print(n, "is a prime no")
