#Python Calculator (improved version, the old version can be found in my repositories, the name of the old version - Calculator_in_Python_programming_language)

float_str="float"
int_str="int"
check=0
yes="yes"

def addition(num_1,num_2):
    res=num_1+num_2
    return res

def subtraction(num_1,num_2):
    res=num_1-num_2
    return res                      

def multiplication(num_1,num_2):
    res=num_1*num_2
    return res

def division(num_1,num_2):
    try:
        res=num_1/num_2
    except ZeroDivisionError:
        print("You can't divide by zero!!! The result will be 0.")
        res=0
    return res

def divisionOfTheWhole(num_1,num_2):
    try:
        res=num_1//num_2
    except ZeroDivisionError:
        print("You can't divide by zero!!! The result will be 0.")
        res=0
    return res

def remainderOfTheDivision(num_1,num_2):
    try:
        res=num_1%num_2
    except ZeroDivisionError:
        print("You can't divide by zero!!! The result will be 0.")
        res=0
    return res

def degree(num_1,num_2):
    res=pow(num_1,num_2)
    return res

def intComparison(str):
    if str==int_str.capitalize() or str==int_str.upper() or str==int_str:
        return True
    else:
        return False

def floatComparison(str):
    if str==float_str.capitalize() or str==float_str.upper() or str==float_str:
        return True
    else:
        return False

while True:
    intOrFloat=input("What type of data do you need? Int or float? (int mode is an integer, float mode is fractional) ")
    if intComparison(intOrFloat) or floatComparison(intOrFloat):
        break

if intComparison(intOrFloat):

    while check==0:
        try:
            num1=int(input("Enter a number: "))
            num2=int(input("Enter a number: "))
            check+=1
        except ValueError:
            print("It is necessary to enter a number!")
    
    while True:
        symb=input("Enter a character (+,-,*,/,//,%,^): ")
        if symb=="+" or symb=="-" or symb=="*" or symb=="/" or symb=="//" or symb=='%' or symb=="^":
            break
    
    res=0

    while True:

        if symb=="+":
            res=addition(num1,num2)
            print(res)
            cont=input("Do you want to continue? (resume - yes, don't continue - any other word) ")

            if cont==yes.capitalize() or cont==yes.upper() or cont==yes:
                num1=res
                check=0
                while check==0:
                    try:
                        num2=int(input("Enter a number: "))
                        check+=1
                    except ValueError:
                        print("It is necessary to enter a number!")
                continue

            else:
                break

        elif symb=="-":
            res=subtraction(num1,num2)
            print(res)
            cont=input("Do you want to continue? (resume - yes, don't continue - any other word) ")

            if cont==yes.capitalize() or cont==yes.upper() or cont==yes:
                num1=res
                check=0
                while check==0:
                    try:
                        num2=int(input("Enter a number: "))
                        check+=1
                    except ValueError:
                        print("It is necessary to enter a number!")
                continue

            else:
                break

        elif symb=="*":
            res=multiplication(num1,num2)
            print(res)
            cont=input("Do you want to continue? (resume - yes, don't continue - any other word) ")

            if cont==yes.capitalize() or cont==yes.upper() or cont==yes:
                num1=res
                check=0
                while check==0:
                    try:
                        num2=int(input("Enter a number: "))
                        check+=1
                    except ValueError:
                        print("It is necessary to enter a number!")
                continue

            else:
                break

        elif symb=="/":
            res=division(num1,num2)
            print(res)
            if res==0:
                print("The result is equal to zero, so it makes no sense to continue dividing further, because dividing 0 by any number will be zero.")
                break
            cont=input("Do you want continue? (resume - yes, don't continue - any other word) ")

            if cont==yes.capitalize() or cont==yes.upper() or cont==yes:
                num1=res
                check=0
                while check==0:
                    try:
                        num2=int(input("Enter a number: "))
                        check+=1
                    except ValueError:
                        print("It is necessary to enter a number!")
                continue
            else:
                break

        elif symb=="//":
            res=divisionOfTheWhole(num1,num2)
            print(res)
            if res==0:
                print("The result is equal to zero, so it makes no sense to continue dividing further, because dividing 0 by any number will be zero.")
                break
            cont=input("Do you want continue? (resume - yes, don't continue - any other word) ")

            if cont==yes.capitalize() or cont==yes.upper() or cont==yes:
                num1==res
                check=0
                while check==0:
                    try:
                        num2=int(input("Enter a number: "))
                        check+=1
                    except ValueError:
                        print("It is so necessary to enter a number!")
                continue

            else:
                break

        elif symb=="%":
            res=remainderOfTheDivision(num1,num2)
            print(res)
            if res==0:
                print("The result is equal to zero, so it makes no sense to continue dividing further, because dividing 0 by any number will be zero.")
                break
            cont=input("Do you want continue? (resume - yes, don't continue - any other word) ")

            if cont==yes.capitalize() or cont==yes.upper() or cont==yes:
                num1=res
                check=0
                while check==0:
                    try:
                        num2=int(input("Enter a number: "))
                        check+=1
                    except ValueError:
                        print("It is necessary to enter a number!")
                continue

            else:
                break

        elif symb=="^":
            res=degree(num1,num2)
            print(res)
            cont=input("Do you want continue? (resume - yes, don't continue - any other word) ")

            if cont==yes.capitalize() or cont==yes.upper() or cont==yes:
                num1=res
                check=0
                while check==0:
                    try:
                        num2=int(input("Enter a number: "))
                        check+=1
                    except ValueError:
                        print("It is necessary to enter a number!")
                continue

            else:
                break

if floatComparison(intOrFloat):

    while check==0:

        try:
            num1=float(input("Enter a number: "))
            num2=float(input("Enter a number: "))
            check+=1
        except ValueError:
            print("It is necessary to enter a number!")
        
    while True:
        symb=input("Enter a character (+,-,*,/,//,%,^): ")
        if symb=="+" or symb=="-" or symb=="*" or symb=="/" or symb=="//" or symb=="%" or symb=="^":
            break

    res=0

    while True:
        if symb=="+":
            res=addition(num1,num2)
            print(res)
            cont=input("Do you want continue? (resume - yes, don't continue - any other word) ")

            if cont==yes.capitalize() or cont==yes.upper() or cont==yes:
                num1=res
                check=0
                while check==0:
                    try:
                        num2=float(input("Enter a number: "))
                        check+=1
                    except ValueError:
                        print("It is necessary to enter a number!")
                continue

            else:
                break

        elif symb=="-":
            res=subtraction(num1,num2)
            print(res)
            cont=input("Do you want continue? (resume - yes, don't continue - any other word) ")

            if cont==yes.capitalize() or cont==yes.upper() or cont==yes:
                num1=res
                check=0
                while check==0:
                    try:
                        num2=float(input("Enter a number: "))
                        check+=1
                    except ValueError:
                        print("It is necessary to enter a number!")
                continue

            else:
                break

        elif symb=="*":
            res=multiplication(num1,num2)
            print(res)
            cont=input("Do you want continue? (resume - yes, don't continue - any other word) ")

            if cont==yes.capitalize() or cont==yes.upper() or cont==yes:
                num1=res
                check=0
                while check==0:
                    try:
                        num2=float(input("Enter a number: "))
                        check+=1
                    except ValueError:
                        print("It is necessary to enter a number: ")
                continue

            else:
                break

        elif symb=="/":
            res=division(num1,num2)
            print(res)
            if res==0:
                print("The result is equal to zero, so it makes no sense to continue dividing further, because dividing 0 by any number will be zero.")
                break
            cont=input("Do you want to continue? (resume - yes, don't continue - any other word) ")

            if cont==yes.capitalize() or cont==yes.upper() or cont==yes:
                num1=res
                check=0
                while check==0:
                    try:
                        num2=float(input("Enter a number: "))
                        check+=1
                    except ValueError:
                        print("It is necessary to enter a number!")
                continue

            else:
                break

        elif symb=="//":
            res=divisionOfTheWhole(num1,num2)
            print(res)
            if res==0:
                print("The result is equal to zero, so it makes no sense to continue dividing further, because dividing 0 by any number will be zero.")
                break
            cont=input("Do you want continue? (resume - yes, not continue - any other word) ")

            if cont==yes.capitalize() or cont==yes.upper() or cont==yes:
                num1=res
                check=0
                while check==0:
                    try:
                        num2=float(input("Enter a number: "))
                        check+=1
                    except ValueError:
                        print("It is necessary to enter a number!")
                continue

            else:
                break

        elif symb=="%":
            res=remainderOfTheDivision(num1,num2)
            print(res)
            if res==0:
                print("The result is equal to zero, so it makes no sense to continue dividing further, because dividing 0 by any number will be zero.")
                break
            cont=input("Do you want continue? (resume - yes, not continue - any other word) ")

            if cont==yes.capitalize() or cont==yes.upper() or cont==yes:
                num1=res
                check=0
                while check==0:
                    try:
                        num2=float(input("Enter a number: "))
                        check+=1
                    except ValueError:
                        print("It is necessary to enter a number!")
                continue

            else:
                break

        elif symb=="^":
            res=degree(num1,num2)
            print(res)
            cont=input("Do you want continue? (resume - yes, not continue - any other word) ")

            if cont==yes.capitalize() or cont==yes.upper() or cont==yes:
                num1=res
                check=0
                while check==0:
                    try:
                        num2=float(input("Enter a number: "))
                        check+=1
                    except ValueError:
                        print("It is necessary to enter a number!")
                continue
            
            else:
                break
