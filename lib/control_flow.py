#!/usr/bin/env python3
def admin_login(username, password):
    if (username == 'admin' or username == 'ADMIN') and password == '12345':
        return "Access granted"
    else:
        return "Access denied"
admin_login('admin',12345)


def hows_the_weather(temperature):
    try:
        if temperature < 40:
            print("It's brisk out there")
        elif 40 <= temperature <= 65:
            print("It's a little chilly out there")
        elif temperature > 85:
            print("It's too dang hot out there")
    finally:
        print("It's perfect out there")

hows_the_weather(60)

def fizzbuzz(num):
    
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)
    

# Example usage:
fizzbuzz(4)


    

def calculator(operation, num1, num2):
    if operation in ('+', '-', '*', '/'):
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
          
        else:
            return "Invalid operation"
        
        return f"{num1} {operation} {num2} = {result}"

# Example usage:
operation = '$'
num1 = 5
num2 = 3
result_string = calculator(operation, num1, num2)
print(result_string)

def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float")
    finally:
        print("Isn't division fun?")
divide(6,3)

dog = "cuddly"

dict_map = {
    "hungry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "Playing tug-of-war.",
    "cuddly": "Snuggling.",
}