#program to exercise number 34 from the book, 
#the program is tto take 20 floating numbers from user 
#and print sum, average, min, max


sum = 0 
avg = 0
a = float (input ("enter a value: "))
min = a
max = a

for i in range (19):
  a = float (input ("enter a value: "))
  sum += a
  if a > max:
    max = a 
  else:
    min = a

print ("the sum is: ") 
print (sum)
print ("average: ")
print (sum / 20)
print ("min: ")
print (min)
print ("max: ")
print (max)