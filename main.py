import time
from parser.brace_checker import check_braces
from parser.if_checker import check_if_statements
from parser.for_checker import check_for_statements
from parser.while_checker import check_while_statements


def main():
    start_time = time.time()

    try:
        with open("sample.txt", "r") as file:
            code = file.read()
    except FileNotFoundError:
        print("Error: sample.txt not found.")
        return

    valid = True

    # Brace check
    if not check_braces(code):
        print("Braces do not match, exiting code.")
        valid = False
    else:
        print("Braces are balanced.")

    # If check
    if check_if_statements(code):
        print("'If' statements are correct.")
    else:
        print("'If' statements are incorrect, exiting code.")
        valid = False

    # For check
    if check_for_statements(code):
        print("'For' statements are correct.")
    else:
        print("'For' statements are incorrect, exiting code.")
        valid = False

    # While check
    if check_while_statements(code):
        print("'While' statements are correct.")
    else:
        print("'While' statements are incorrect, exiting code.")
        valid = False

    elapsed = (time.time() - start_time) * 1000
    print(f"Finished checks in {elapsed:.2f}ms")
    print("--------------------------------")

    if valid:
        print("Code is valid.")
    else:
        print("Code is invalid.")


if __name__ == "__main__":
    main()