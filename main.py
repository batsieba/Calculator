#Calculator
from art import logo
#Add
def add(a, b):
  return a + b

#Subtract
def subtruct(a,b):
  return a - b

#Multiply
def multiply(a, b):
  return a * b

#Divide
def divide(a, b):
  return a / b


#operation needed
operations = {
  "+": add,
  "-": subtruct,
  "*": multiply,
  "/": divide
}


def call_ops():
  for i in operations:
    print(i)

def calculator():
  print(logo)
  #input from user
  num1 = float(input("What's the first number?: "))
  #print the operations
  
  repeat = True
  
  #loop answer
  while(repeat):
    call_ops()
    symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    calculation = operations[symbol]
    answer = calculation(num1, num2)
    
    print(f"{num1} {symbol} {num2} = {answer}")
  
    ask = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
    if ask == "y":
      num1 = answer
    else:
      repeat = False
      calculator()


calculator()
      