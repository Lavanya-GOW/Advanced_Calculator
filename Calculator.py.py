import math
while True:
 
 print("What you want to do?:")
 print("\n1. Basic Operations(+,-,,/,*,//[integer division],%[MODULOUS])")
 print("\n2. Scientific Operations(log, sin, tan, cos,square root, !)")
 print("[Note: Trignometric functions takes number as radians, not degree]")

 Want = int(input("\nEnter what you wanna do(1 or 2):"))

 if Want == 1:
  print()

  f = int(input("\nEnter the first number:"))

  opt = input("\nEnter an operator among(+,-,*,/,//,%, **)")

  s = int(input("\nenter the second number:"))


  if opt == "+":
   print(f+s)
  elif opt == "-":
   print(f-s)
  elif opt == "*":
   print(f*s)
  elif opt == "/":
   if s==0:
    print("Not Defined")
   else:
    print(f/s)
  elif opt == "":
   print(f**s)
  elif opt == "//":
   if s == 0:
    print("Not Defined")
   else:
    print(f//s)
  elif opt == "%":
   print(f%s)


  
  else:
   print("Choose operator among the options")

 elif Want == 2:
  
  
  
  num = float(input("\nEnter a number"))

  p = str(input("\nEnter an operator among (log, sin, cos, tan, sqrt,!)"))

  if p == "sqrt":
   if num < 0:
    print("Square root of negative number isn't defined")
   else:
    print(f"{math.sqrt(num):.3f}")

  elif p == "log":
   if num <= 0:
    print("Logarithms isn't defined for non postitive integers")
   else:           
    print(f"{math.log10(num):.3f}")

  elif p == "sin":
   print(f"{math.sin(num):.3f}")

  elif p == "cos":
   print(f"{math.cos(num):.3f}")

  elif p == "tan":
   print(f"{math.tan(num):.3f}")
   
  elif p == "!":
   if  num < 0:
    print("Factorial not defined for negative integers")
   elif num != int(num):
    print("Factorial only defined for integers")
   else:
    print(math.factorial(int(num)))
  else:
   print("Choose an operator amomg the options")
   
 else:
  print("Choose either 1 or 2")


 again = input("\nDo you wanna use calculator again?[Yes/No]:")
 if again.lower() == "no":
  break