#while loop syntax:
i = 0
while (i == 0):
    print(i)
    i = i + 1

#print 1 to 5 using while loop:
i=0
while i<6:
    print(i)
    i=i+1

#write a loop statement to print series 10,20,30,40,.....,200 using while loop:
i=0
while i<=200:
    print(i)
    i=i+10

#write a program to print first 10 natural numbers in reverse order using while loop:
i=10
while i>0:
    print(i)
    i=i-1

#write a program factorial using while loop:
i=5
fact=1
while i>0:
    fact=fact*i
    i = i-1
print(fact)

a = [1,2,3,4,5,6]
b=[]
m=0
while m<len(a):
        b.append(a[m])
        print("".join.(b))
        m=m+1


a = "i live in"
m = 0
while m< len(a):
    print(a[m])
    m=m+1

a = "i live in"
m = 0
while m< len(a):
    print(a[m])
    m=m+2


a = [1,2,3,4,5,6,7,8]
m = 0
while m< len(a):
    if a[m] % 2==0:
        print(a[m])
    m=m+1