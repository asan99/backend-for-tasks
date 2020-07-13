"""9) Напиши калькулятор используя функции и используйте Try Except во время
деления, деление на ноль нельзя"""

def calculator():
    try:
        x = input(' "+", "-", "/", "*" ')
        if x == "+" or x == "-" or x == "/" or x == "*":
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            try:
                if x == "+":
                    print(a + b)
                elif x == "-":
                    print(a - b)
                elif x == "/":
                    print(a / b)         
                elif x == "*":
                    print(a * b) 
            except ZeroDivisionError:
                print("На ноль делить нельзя!!!!!!!!")  
                calculator() 
        else:
            print("Такого оператора нет!")     
            calculator()     
    except Exception:
        print("Нельзя ввести строку!") 
        calculator()            
calculator()    