import fractions
from fractions import Fraction
input_0 = int(input("enter 1 to excute the program:"))
i = input_0
while i==1:
    input_01 = int(input("enter 1 to calculate fractions and 2 to convert mixed fraction into improper fraction:"))
    if input_01==1:
        input_1 = int(input("please enter 1st fraction numerator:"))
        input_2 = int(input("please enter 1st fraction denominator:"))
        input_3 = int(input("please enter 2st fraction numerator:"))
        input_4 = int(input("please enter 2st fraction denominator:"))
        input_5 = input("press + to add , - to subtract, * to multiply , / to divide: ")
        if input_5=="+":
            fr1 = Fraction(input_1,input_2)
            fr2 = Fraction(input_3,input_4)
            print(fr1+fr2)
        if input_5=="*":
            fr1 = Fraction(input_1,input_2)
            fr2 = Fraction(input_3,input_4)
            print(fr1*fr2)    
        if input_5=="-":
            fr1 = Fraction(input_1,input_2)
            fr2 = Fraction(input_3,input_4)
            print(fr1-fr2) 
        if input_5=="-":
            fr1 = Fraction(input_1,input_2)
            fr2 = Fraction(input_3,input_4)
            print(fr1-fr2) 
        if input_5=="/":
            fr1 = Fraction(input_1,input_2)
            fr2 = Fraction(input_3,input_4)
            print(fr1/fr2) 
        input_0 = int(input("enter 1 to excute the program:"))
        if input_0 > 1 or input_0==0:
            i = i + 1 
            break  
    elif input_01==2:
        def mixed_fraction_to_improper_fraction():
            a=int(input("enter numerator:"))   
            b = int(input("enter denominator:")) 
            c = int(input("enter mixed number:"))
            fr3 = Fraction(c*b+a, b)
            print(fr3)
        mixed_fraction_to_improper_fraction()   
        input_0 = int(input("enter 1 to excute the program:"))
        if input_0 > 1 or input_0==0:
            i = i + 1 
            break   

print("thank you")
