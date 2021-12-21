n1 = int(input("Please enter the first number :-\n"))
n2 = int(input("Please enter the second number :-\n"))
HCF = 1
if n1 == n2:
    print(f"The HCF of these two numbers = {n1}")
if n1 == 0 or n2 == 0:  
    print(f"The HCF of {n1} and {n2} =", endsWith = " ")
    if n1 == 0:
        print(n2)
    else:
        print(n1)
elif n1>n2:
    for i in range(1,n2+1):
        if n1%i ==0 and n2%i == 0:
            HCF = i
    print(f"The HCF of {n1} and {n2} = {HCF}")
elif n1<n2:
    for i in range(1,n1+1):
        if n1%i == 0 and n2%i == 0:
            HCF = i
    print(f"The HCF of {n1} and {n2} = {HCF}")