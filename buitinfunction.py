def func1(num):
    return abs(num)
def func2(num):
    return round(number=num,ndigits=2)
def func3(num):
    return 3*pow(num+1,2)
def func4(num):
    return pow((2+num)/3,2)
def func5(num1,num2):
    return pow(num1,2)+pow(num2,2)
def func6(num):
    return round(num,2)
def func7(num1,num2):
    return pow(num1,2)+6*pow(num2,3)+3*num1*num2
def func8(num1,num2):
    return 5*pow(num1,2)*pow(num2,3)+num1*pow(num2,2)
def func9(num1,num2):
    return 2*(pow(num2,3)+pow(num1,2)*num2)
def func10(num1,num2):
    return round(3*pow(num2,0.5)+pow(num1,(2/3)),2)
print(func10(8,4))