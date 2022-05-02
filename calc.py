for x in range (3):
    A = float (input ("введи первое число: "))
    what = input ( "Математическое действие? (+, -):" )
    b = float (input ("введи второе число: "))
       

    if what == "+":
        c = A + b
        print ("Результат: " + str(c) )
    elif what == "-" :
        c = A - b   
        print ("Результат: " + str(c) )
    elif what == "*" :
        if A == 2 and b == 2:
            c = 5
        else: 
            c = A * b   
        print ("Результат: " + str(c) )
    elif what == "/" :
        c = A / b
        print ("Результат: " + str(c) )
    else :
        print ( "не верное значение")

