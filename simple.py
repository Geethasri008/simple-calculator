while True:
  print("choose the operation you want to perform: ")
  print("Enter 1:Addition")
  print("Enter 2:Subtraction")
  print("Enter 3:Multiplication")
  print("Enter 4:Division")
  print("Enter 5:Square Root")
  print("Enter 6:Exit")
  i=int(input("Enter your choice: "))
  if (i==1):
    a=int(input("enter the first value: "))
    b=int(input("enter the first value: "))
    print(a,"+",b,"=",a+b)
  elif(i==2):
    a=int(input("enter the first value: "))
    b=int(input("enter the first value: "))
    print(a,"-",b,"=",a-b)
  elif(i==3):
    a=int(input("enter the first value: "))
    b=int(input("enter the first value: "))
    print(a,"*",b,"=",a*b)
  elif(i==4):
    a=int(input("enter the first value: "))
    b=int(input("enter the first value: "))
    print(a,"/",b,"=",a/b)
  elif(i==5):
    a=int(input("enter the first value: "))
    print("square Root of",a,"=",a**0.5)
  else:
    break