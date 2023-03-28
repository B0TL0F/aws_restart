A=int(input("A="))
B=int(input("B="))
C=int(input("C="))

if (A>B) and (A>C):
    print("A is the greatest")
elif (B>A) and (B>C):
    print("B is the greatest")
elif (C>B) and (C>A):
    print("C is the greatest")