num0 = int(input("a coeficient: "))
num1 = int(input("b coeficient: "))
num2 = int(input("c coeficient: "))
answer = False
x = num0 * num2
print("Factors:")
if x > 0:
    for i in range(1, x + 1):
           if x % i == 0:
               j = int(x/i)
               print(i, ", ", j)
               if i + j == num1:
                   print("An answer is ",i,",",j,".")
                   answer = True
    for i in range(-x, 0):
           if x % i == 0:
               j = int(x/i)
               print(i, ", ", j)
               if i + j == num1:
                   print("An answer is ",i,",",j,".")
                   answer = True
elif x < 0:
    for i in range(x, 0):
           if x % i == 0:
               j = int(x/i)
               print(i, ", ", j)
               if i + j == num1:
                   print("An answer is ",i,",",j,".")
                   answer = True
    for i in range(-x, 0):
           if x % i == 0:
               j = int(x/i)
               print(i, ", ", j)
               if i + j == num1:
                   print("An answer is ",i,",",j,".")
                   answer = True

if answer:
    print("Answer was found.")
else:
    print("No answer.")