n=int(input("enter a numbber:"))
rev=0
temp=n
while(temp>0):
    r=temp%10
    rev=(rev*10)+r
    temp=temp//10
print("Reverse of the given number is",rev)
if(n==rev):
    print("the number is a palindrome number")
else:
    print("the number is not a palindrome")