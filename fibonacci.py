#printing fibonacci number until 'n' using python
n=int(input("enter the value of 'n': "))
a=0
b=1
sum=0
count=1
print("fibonacci:",end = " ")
while(count<=n):
  print(sum,end=" ")
  count +=1
  a=b
  b=sum
  sum=a+b
