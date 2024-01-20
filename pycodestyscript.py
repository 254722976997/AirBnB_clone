# This is a beautiful Python script that adheres to PEP 8 style conventions.

def greet(name):
    """This function greets the person passed in as a parameter."""
    greeting = f"Hello, {name}!"
    print(greeting)

def add_numbers(a, b):
    """This function adds two numbers and returns the result."""
    result = a + b
    return result

if __name__ == "__main__":
    # Example usage of the functions
    person_name = "John"
    greet(person_name)

    num1 = 10
    num2 = 20
    sum_result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {sum_result}")

