text_file = open("readmeee.txt","r")
sentence =  text_file.read()
words = sentence.split()
yeld= ( "f", "c", "k", "r", "F", "C", "K", "R")
VOWELS=("a","e","i","o","u","A","E","I","O","U")
k=len(words)
for i in range (k):
  mess = word[i]
  messe = ""
  for letter in mess:
    if letter not in VOWELS:
      messe = messe + letter
  count1=0
  count2=0
  for f in range(8)
    if yeld[f] in messe:
    count1+=1
  else:
    count2+=1
  if count1 >= count2 :
    print ( word[i], "is a bad word")
  else:
    print ( word[i], "is an ok word")
text_file.close()
