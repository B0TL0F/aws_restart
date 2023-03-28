A=int(input("A="))
for x in range(2,A):
    if A % x ==0:
        break
if x+1 == A:
    print(A," is a prime number")
else:
    print(A," is not a prime number")