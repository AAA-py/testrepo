## Adding a new file inside the child branch

print("Inside Child Branch")
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

def add (num1, num2):
   answer = num1 + num2
   print(f"{num1} + {num2} is equal to {answer}")

add(num1=x, num2=y)
