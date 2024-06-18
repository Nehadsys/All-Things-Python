try:
    
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number again: "))
    
    takeInput = int(input("Please enter an operation: \n 1) Addition \n 2) Substraction \n 3) Multiplication \n 4) Division \n "))
    
    if takeInput == 1:
        print(num1+num2)
        
    elif takeInput == 2:
        print(num1-num2)
        
    elif takeInput == 3:
        print(num1*num2)
    
    elif takeInput == 4:
        print(num1/num2)
    
except ZeroDivisionError as e:
    print("Cannot divide by zero idiot")

except ValueError:
    print("You cannot put anything else other than integers!")
    
except Exception as e:
    print(e)
    print("Something occured!")
    

    
