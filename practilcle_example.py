## Praticle example
# To find the year is leap year or not, In a confusing manner

year = int(input("Enter the year: "))

if (year%4==0):
    if (year%100==0):
        if(year%400==0):
            print(year,"is a leap year")
        else:
            print(year,"is no leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")