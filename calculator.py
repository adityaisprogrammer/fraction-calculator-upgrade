input1 = float(input("Enter first number:"))
input2 = float(input("Enter second number:"))
input3 = input("what do you want to do add , subtract , divide and multiply:")

if input3.lower()=="add":
 
        print(input1+input2)    
    
elif input3.lower()=="subtract":

        print(input1-input2)
elif input3.lower()=="divide":

        print(input1/input2)
elif input3.lower()=="multiply":
 
  
    
        print(input1*input2)
else:
    print("this calculator could only add, subtract, divide, multiply")

print("thank you")