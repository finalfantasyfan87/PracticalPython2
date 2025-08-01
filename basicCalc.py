
def perform_basic_calculation():
    while True:
        try:
            answer = input("Let's perform a basic calculation. Press 'q' to exit. Press the enter key to continue.: ")
            if answer == 'q':
                print("Goodbye.")
                break
            first_number = int(input("Enter the first number: "))
            second_number = int(input("Enter the second number: "))

            if first_number < 0 or first_number is None:
                print("First number must be greater than 0.")
            if second_number < 0 or second_number is None:
                print("Second number must be greater than 0.")
            operation = input("Which operation would you to perform(+,-,*,/). Press 'q' to quit."
                              "Press the enter key to continue.: ")

            match operation:
                case "+":
                    print(first_number + second_number)
                case "-":
                    print(first_number - second_number)
                case "*":
                    print(first_number * second_number)
                case "/":
                    print(first_number / second_number)
                case "q":
                    print("Goodbye")
                    break
                case _:
                    print("Invalid operation")
        except ValueError:
            print("Provide a valid integer, please!")

perform_basic_calculation()
