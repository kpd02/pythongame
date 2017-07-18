def TwoNums(num1, num2):          #defining the function for divisble
    return num2 % num1 == 0

def fizzbuzz(newnumber):        #function for fizzbuzz: trying to get it to return all of the moduluses
    if newnumber % 15 == 0:
        return "fizzbuzz"
    elif newnumber % 5 == 0:
        return "buzz"
    elif newnumber % 3 == 0:
        return "fizz"
    else:
        return "nooo"

while True:
    user_input = input("if you want to stop, type STOP. If not, press any key ")
    if user_input == "STOP":
        break
    else:
        numberinput = input("Type a Number! ") #getting user input
        number = int(numberinput) #need to create a new var. to convert

        callfizzbuzz = fizzbuzz(number)
        print(callfizzbuzz)

        print("lets see if the second number is divisible by the first number")

        number1 = input("pick a first number ")  #getting user input for first num
        first = int(number1)

        number2 = input("pick a second number ") #user input for second number
        second = int(number2)

        quotient = TwoNums(first, second)   #calling the function?
        print(quotient)
