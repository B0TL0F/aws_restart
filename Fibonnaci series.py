A=int(input("A="))
a = 0
b = 1
s = 0

for x in range(A):
    print(s,end=" ")
    s = a+b
    b = a
    a = s