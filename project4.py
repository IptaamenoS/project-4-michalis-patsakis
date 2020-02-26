def AscII_trans( text)
 global number 
 number= [ord(n) for n in text]
Print (" Δώστε λέξη")
text=input()
AscII_trans(text)
for i in number:
  If( i > 0 and i < 8 and i != 4 and i != 6)
    print(i + 'inai protos')
