def AscII_trans( text):
 global number 
 number= [ord(n) for n in text]
 l = len(number)
 for i in range(l):
  k= int(number[i])
  If( k > 0 and k < 8 and k != 4 and k != 6)
  print ( k + " είναι πρώτος αριθμός")
 else 
  print ( k + " δεν είναι πρώτος αριθμός")
Print(" Δώστε λέξη")
text=input()
