# Simple Python Calculator
def calculator():
    print("=== Simple Python Calculator ===")
    print("Operations: +, -, *, /, ** (power), % (modulus)")
    print("Type 'quit' to exit\n")

    previous = 0
    run = True

    def perform_calc():
        nonlocal previous
        if previous == 0:
            equation = input("Enter equation: ")
        else:
            equation = input(f"{previous} ")

        if equation == 'quit':
            return False

        # Replace ^ with ** for power
        equation = equation.replace('^', '**')

        try:
            result = eval(equation)
            print("Result:", result)
            previous = result
        except ZeroDivisionError:
            print("Error: Division by zero!")
            previous = 0
        except Exception as e:
            print(f"Error: Invalid input! ({e})")
            previous = 0

        return True

    while run:
        run = perform_calc()
        print("-" * 40)

# Run the calculator
if __name__ == "__main__":
    calculator()
