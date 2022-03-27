#program for (BMM)
a = int (input ("please enter an integer: "))
b = int (input ("please enter an integer: "))

if a > b:
  smaller = b
else:
  smaller = a
  
for i in range(1, smaller+1):
  if((a % i == 0) and (b % i == 0)):
    BMM = i 
   
print(BMM)


    
    
     
    
    