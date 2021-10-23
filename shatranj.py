
n= int(input("enter n::"))
m=int(input("enter m::"))


for i in range(n):
    if i%2!=0:
        for j in range(m):
            print("*#",end="")
    else:
        for j in range(m):
            print("#*",end="")
    print()