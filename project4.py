def AscII_trans( text):
 global number 
 number= [ord(n) for n in text]
 l = len(number)
 for i in range(l):
  e= e +number[i]
 k= int(e)
 if (k <= 3 and k >1) :
  print("thats a  prime a number")
 if ( k % 2 == 0 or k % 3 == 0 ):
  print("thats not a prime number")
 i = 5
 while(i * i <= k) : 
  if (k % i == 0 or k % (i + 2) == 0) : 
   print ("thats not a prime number")
   i = i + 6

