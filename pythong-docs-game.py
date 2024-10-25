import textwrap

def main():
    while True:
        user_input_chosen_menu = input("Type the number of menu you wanna visit: ")
        print(textwrap.indent("1. Built-in functions", "> "))
        print(textwrap.indent("2. Programming keywoards / Glossary", "> "))
        if(user_input_chosen_menu == "1"):
            built_in_functions_menu()
        if(user_input_chosen_menu == "2"):
            glossary_menu()
        
        
def glossary_menu():
    return
def built_in_functions_menu():
    print("###")
    user_input_chosen_function = input("Write a built-in function you wanna explore (or enter to go back to main menu): ")
    if (user_input_chosen_function == ""):
        return
    if user_input_chosen_function.upper() in ["1", "ABS"]:
        abs_tutorial()
    if user_input_chosen_function.upper() in ["2", "AITER"]:
        aiter_tutorial()
    if user_input_chosen_function.upper() in ["3", "ALL"]:
        all_tutorial()
    if user_input_chosen_function.upper() in ["4", "ANEXT"]:
        anext_tutorial()


def anext_tutorial():
    print_tutorial_intro("anext tutorial(async_iterator, default)")
    pythonExplanation = """
    When awaited, return the next item from the given asynchronous iterator, or default if given and the iterator is exhausted.
    This is the async variant of the next() builtin, and behaves similarly.
    This calls the __anext__() method of async_iterator, returning an awaitable. Awaiting this returns the next value of the iterator. 
    If default is given, it is returned if the iterator is exhausted, otherwise StopAsyncIteration is raised.
          """
    print(textwrap.indent(pythonExplanation, ">"))
    print_my_explanation()
    print_out_of_scope()
def all_tutorial():
    print_tutorial_intro("all tutorial")
    print("Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:")
    function_definition = """\
        def all(iterable):
            for element in iterable:
                if not element:
                    return False
            return True
        """
    print(textwrap.indent(function_definition, ">"))
    print_my_explanation()
    print("The all fucntion checks if all items are iretable, so if there is a 0 or empty string it will return false")
    print("Examples: ")
    print(textwrap.indent("All elements are Falsy: *myList = [0, "", None, [], {}]* and will return false", "> "))
    print(textwrap.indent("All elements are Truthy: *myList = [1, 2, 5, 8, 9, 10]* and will return true", "> "))
    input("Press enter to continue.")
def aiter_tutorial():
    print_tutorial_intro('aiter tutorial')
    print("Return an asynchronous iterator for an asynchronous iterable. Equivalent to calling x.__aiter__().")
    print("Note: Unlike iter(), aiter() has no 2-argument variant.")
    print_my_explanation()
    print_out_of_scope()
def print_out_of_scope():
    print("Out of scope of the project")
def print_tutorial_intro(name):
    print(f"####--{name}--####")
    print("Python docs explanation:")
def print_my_explanation():
    print("---")
    print("My Explanation:")
def abs_tutorial():
    print_tutorial_intro('abs tutorial')
    print("Return the absolute value of a number. The argument may be an integer, a floating-point number, or an object implementing __abs__().")
    print("If the argument is a complex number, its magnitude is returned.")
    print_my_explanation()
    print("It removes any negative sign and returns the positive version of the number.")
    print()
    print(f"Examples: abs(-10.50) becomes: 10.50")

    while True:
        user_input = input("To test it, give a number to return the absolute value (or press Enter to exit): ")
        if user_input == "":
            print("Exiting the tutorial.")
            break

        try:
            # Check if input is a valid float or int
            if user_input.count(".") == 1 and user_input.replace(".", "").replace("-", "").isdigit():
                parsed_user_input = float(user_input)
            else:
                parsed_user_input = int(user_input)
            absolute_value = abs(parsed_user_input)

            # Check if the original input is already absolute
            if absolute_value == parsed_user_input:
                print(f"{user_input} stays: {absolute_value}")
            else:
                print(f"{user_input} becomes: {absolute_value}")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

main()