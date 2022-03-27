#Program for x^3-x2+2 with Newoton Raphson with 10 times repetition


x = 16
count = 1
h = (x * x * x - x * x + 2) / (3 * x * x - 2 * x )

while count <= 10: 
    h = (x * x * x - x * x + 2) / (3 * x * x - 2 * x ) 
    x -= h
    count += 1 

print(x)