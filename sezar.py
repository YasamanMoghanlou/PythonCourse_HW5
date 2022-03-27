#sezar program

message = input("Enter a message: ")
key = int(input("enter key: "))
sezarcode = " "

for letter in message:        
    sezarcode += chr(ord(letter) + key) 
    
        
print(sezarcode)