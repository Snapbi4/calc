from re import A


what = input ( "Математическое действие? (+, -):" )

A = float (input ("введи первое число: "))
b = float (input ("введи второе число: "))

if what == "+":
    c = A + b
    print ("Результат: " + str(c) )
elif what == "-" :
    c = A - b   
    print ("Результат: " + str(c) )
elif what == "*" :
    c = A * b
    print ("Результат: " + str(c) )
elif what == "/" :
    c = A / b
    print ("Результат: " + str(c) )
else :
    print ( "не верное значение")

input ()
