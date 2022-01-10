a = int(input("enter an integer"))
try:
    if(a<10):
        raise ValueError("value cannot be less than 10")
    else:
        print("value entered is --",a)
except ValueError as ve:
    print(ve)