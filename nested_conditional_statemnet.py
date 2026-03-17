## Nested conditional statement is the condition in which you can place one or more if, else, and elif statement inside another if, elif, else statement.

num = int(input("Enter the number: "))

if num>=0:
    print("Number is positive")
    
    if num%2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number is negative")