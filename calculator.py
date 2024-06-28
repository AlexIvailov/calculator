# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Деление на нула не е позволено.")
    return x / y

def main():
    print("Изберете операция:")
    print("1. Събиране")
    print("2. Изваждане")
    print("3. Умножение")
    print("4. Деление")

    while True:
        choice = input("Въведете избор (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Въведете първото число: "))
            num2 = float(input("Въведете второто число: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                try:
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                except ValueError as e:
                    print(e)
            break
        else:
            print("Невалиден избор. Моля, опитайте отново.")

if __name__ == "__main__":
    main()
