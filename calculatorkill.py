def sum():
            a = int(input("enter first number : "))
            b = int(input("enter second number : "))
            print(a+b)

def sub ():
            x = int(input("enter first number : "))
            y = int(input("enter second number : "))
                    
            if x > y :
                print(x - y)
            else:
                print("it Is minus value")
def mul():
            p = int(input("enter first number : "))
            q = int(input("enter second number : "))
            print (p*q)
def div ():
            m = int(input("enter first number : "))
            n  = int( input("enter second number : "))
n = int(input("enter choise 1:add\n enter choice 2:sub\n enter choice 3:mul\n enter choice 4:div\n"))

if n == 1:
    sum()
elif n== 2:
    sub()
elif n==3:
    mul()
elif n==4:
    div()
else:
    print("go to sleep")
    

                    
