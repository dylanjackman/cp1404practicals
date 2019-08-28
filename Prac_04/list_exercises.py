user_names = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
              'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_name = input("Please enter correct User Name: ")
if user_name not in user_names:
    print("Access Denied")
else:
    print("\nAccess Granted\n")
    numbers = []
    print("Please enter 5 numbers ")
    for i in range(1, 6):
        user_numbers = int(input("Number: "))
        numbers.append(user_numbers)
    print("The first number is {:2}".format(numbers[0]))
    print("The last number is {:2}".format(numbers[4]))
    print("The smallest number is {:2}".format(min(numbers)))
    print("The largest number is {:2}".format(max(numbers)))
    print("The average of the numbers is {:2}".format(sum(numbers) / 5))