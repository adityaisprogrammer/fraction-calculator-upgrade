#this program is beta version 
#first two input are used for first fraction first input is numerator and denominator is 2nd input and 3rd and 4th input is used for 2nd fraction 
#this can take only two fractions
from fractions import Fraction
input_1 = int(input("please enter 1st number numerator:"))
input_2 = int(input("please enter 1st number denominator:"))
input_3 = int(input("please enter 2st number numerator:"))
input_4 = int(input("please enter 2st number denominator:"))
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