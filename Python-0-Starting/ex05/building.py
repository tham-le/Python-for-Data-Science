import sys


def count_chars(string):
    """
    Counts the number of upper-case characters, lower-case characters,
    punctuation characters, digits and spaces in a string.
    Return a dictionary of the counts.
    """
    upper = lower = digit = space = punct = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        elif char.isspace() or char in "\n\t\r\f\v":
            space += 1
        else:
            punct += 1

    return {"upper letters": upper,
            "lower letters": lower,
            "punctuation marks": punct,
            "spaces": space,
            "digits": digit}


def main():
    """takes a single string argument and displays the sums of its
    upper-case characters,  lower-case characters
    punctuation characters, digits and spaces."""
    try:
        string = ""
        if len(sys.argv) == 1:
            try:
                string = input("What is the text to count?\n")
                string += "\n"
            except EOFError:
                pass
        elif len(sys.argv) == 2:
            string = sys.argv[1]
        else:
            raise Exception("AssertionError: Only one argument is allowed")

        counts = count_chars(string)
        print("The text contains", len(string), "characters")
        for key, value in counts.items():
            print(f"{value} {key}")

    except Exception as e:
        print("Catch error: ", e)


if __name__ == "__main__":
    main()

# https://www.reddit.com/r/learnpython/comments/13l5xn3/
# why_does_ctrl_d_not_raise_eoferror_and_shortens/
