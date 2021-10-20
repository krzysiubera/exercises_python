from complex_number import ComplexNumber


# for example, valid expression is 23.43+48.32j / 32.49-43j - note position of whitespaces
user_input = input("Enter your expression involving complex numbers >> ")
try:
    first_num_as_str, op, second_num_as_str = user_input.split()
except ValueError:
    # it means that unpacking of values went wrong - invalid position of whitespaces
    print("Invalid position of whitespaces")
else:
    first_num = ComplexNumber.from_string(first_num_as_str)
    second_num = ComplexNumber.from_string(second_num_as_str)

    if op == '+':
        result = first_num + second_num
    elif op == '-':
        result = first_num - second_num
    elif op == '*':
        result = first_num * second_num
    elif op == '/':
        result = first_num / second_num
    else:
        raise RuntimeError("Invalid operator provided")

    print(f"The result of {first_num} {op} {second_num} == {result}")


