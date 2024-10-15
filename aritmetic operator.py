def arithmetic_arranger(problems: object, show_answers: object = False) -> object:
    """
       :rtype: object
    """

    def solver(problems):
        results = []
        for problem in problems:
            if '-' in problem:
                operands = problem.split('-')
                result = int(operands[0]) - int(operands[1])
                results.append(result)
            else:
                operands = problem.split('+')
                result = int(operands[0]) + int(operands[1])
                results.append(result)
        return results

    def formatting(problems, results):
        formatted_problems = []
        line1 = ''
        line2 = ''
        line3 = ''
        line4 = ''

        for i, problem in enumerate(problems):
            operand1, operator, operand2 = problem.split()
            operand1_len = len(operand1)
            operand2_len = len(operand2)
            max_length = max(operand1_len, operand2_len)

            if '-' in problem:
                result = results[i]
            else:
                result = results[i]

            # Formatting for each line
            line1 += operand1.rjust(2 + max_length) + '    '
            line2 += operator + operand2.rjust(max_length + 1) + '    '
            line3 += '-' * (max_length + 2) + '    '
            line4 += str(result).rjust(max_length + 2) + '    '

            # Formatting for each problem
            formatted_problem = f"{operand1.rjust(2 + max_length)}\n{operator} {operand2.rjust(max_length)}\n{'-' * (max_length + 2)}\n{str(result)}\n "
            formatted_problems.append(formatted_problem)

        # Remove trailing spaces
        line1 = line1.rstrip()
        line2 = line2.rstrip()
        line3 = line3.rstrip()
        line4 = line4.rstrip()

        if show_answers:
            return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
        else:
            return line1 + "\n" + line2 + "\n" + line3

    def error_checker(problems: object, re: object = 'None') -> object:
        if len(problems) > 5:
            return 'Error: Too many problems.'

        valid_problems = r'^\d+\s*[-+]\s*\d+$'
        invalid_problems = r'[\*/]'

        for problem in problems:
            operand1, operator, operand2 = problem.split()
            if len(operand1) > 4 or len(operand2) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            elif not (operand1.isdigit() and operand2.isdigit()):
                return 'Error: Numbers must only contain digits.'
            elif re.match(valid_problems, problem) and not re.search(invalid_problems, problem):
                continue
            else:
                return "Error: Operator must be '+' or '-'."

    error = error_checker(problems)
    if error:
        return error
    results = solver(problems)
    return formatting(problems, results)


print(arithmetic_arranger('problems', True))

import tkinter as tk


def calculate_monthly_payment():
    loan_amount = float(loan_amount_entry.get())
    interest_rate = float(interest_rate_entry.get()) / 100
    loan_duration_in_years = float(loan_duration_in_years_entry.get())

    number_of_payments = loan_duration_in_years * 12
    monthly_payment = loan_amount * ((1 + interest_rate) ** number_of_payments - 1) / (
            (1 + interest_rate) ** number_of_payments - (1 + interest_rate) ** -number_of_payments)

    result_label.config(text="The monthly payment will be: {:.2f}".format(monthly_payment))


root = tk.Tk()
root.title("Loan Calculator")

# Create labels and entries for user input
loan_amount_label = tk.Label(root, text="Enter the loan amount:")
loan_amount_label.pack()
loan_amount_entry = tk.Entry(root)
loan_amount_entry.pack()

interest_rate_label = tk.Label(root, text="Enter the interest rate (in %):")
interest_rate_label.pack()
interest_rate_entry = tk.Entry(root)
interest_rate_entry.pack()

loan_duration_in_years_label = tk.Label(root, text="Enter the loan duration in years:")
loan_duration_in_years_label.pack()
loan_duration_in_years_entry = tk.Entry(root)
loan_duration_in_years_entry.pack()

# Create a button to calculate the monthly payment
calculate_button = tk.Button(root, text="Calculate Monthly Payment", command=calculate_monthly_payment)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()


def log_in():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    try:
        with open("test_file.txt", "r") as file:
            for line in file:
                if line.strip() == 'Username:{0}, Password:{1}'.format(username, password):
                    print("Greetings,", username, "you are now logged in")
                    return True, username, password
    except FileNotFoundError:
        print("User data file not found.")

    print("Sorry, username and password incorrect. Please re-enter for validation.")
    return False, '', ''


def new_user():
    succes = False
    while not succes:
        new_user = input("Please enter your new username: ")
        new_pass = input("Please enter your new password: ")

        exists = False
        try:
            with open("test_file.txt", "r") as file:
                for line in file:
                    if line.split(',')[0] == 'Username:' + new_user:
                        print('Invalid username: {0} already exists'.format(new_user))
                        exists = True
        except FileNotFoundError:
            # If the file does not exist, we can assume no users exist
            exists = False

        if not exists:
            with open("test_file.txt", "a") as file:
                file.write('Username:{0}, Password:{1}\n'.format(new_user, new_pass))
            succes = True
    print('You made a new user with username: {0} and password: {1}'.format(new_user, new_pass))


def main():
    command = ""
    logged_in = False
    username = password = ""

    while command != 'quit':
        command = input('Please type a command: ')
        if command == 'log in':
            logged_in, username, password = log_in()
        elif command == 'log out':
            logged_in = False
            username = password = ''
            print("You have been logged out.")
        elif command == 'new user':
            if not logged_in:
                new_user()
            else:
                print('First log out to make a new user.')


if __name__ == "__main__":
    main()
