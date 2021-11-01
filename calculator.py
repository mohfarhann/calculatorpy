def add(y, x):
    return y + x
#Pertambahan

def subtract(y, x):
    return y - x
#pengurangan

def multiply(y, x):
    return y * x
#perkalian


def devide(y, x):
    return y / x
 
print("Select Operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.devide")

while True:
    choice = input("Enter choice(1/2/3/4)")

    if choice in ('1','2','3','4'):
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number :"))
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        
        elif choice == '3':
            print(num1,"*", num2, "=", multiply(num1, num2))
        
        elif choice == '4':
            print(num1, ":", num2, "=", devide(num1, num2))

        next_calculator = input("Let's do next calculator? (yes/no)")
        if next_calculator == "no":
            break
            
    else :
        print("invalid input")
            
