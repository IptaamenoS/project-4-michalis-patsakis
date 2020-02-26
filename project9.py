Print("Δώσε μου αριθμό")
n=int(input())
while (n>9):
  n*=3
  n+=1
  k=n
  count=0
  while(k>0):
    count=count+1
    k=k//10
    y=0
  for x inrange(count):
    k= n%10
    n= n//10
    y= y + k
  n=y

     
