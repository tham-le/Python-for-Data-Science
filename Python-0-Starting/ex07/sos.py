import sys


def main():
    """takes a string as an argument and encodes it into Morse Code"""
    try:
        if len(sys.argv) != 2:
            raise Exception("AssertionError: one argument is required")
        string = sys.argv[1]
        if isinstance(string, str) is False:
            raise Exception("AssertionError: type error")
        if string.isalnum() is False and string.isspace() is False:
            raise Exception("AssertionError: the argument must contain only \
alphanumeric characters")

        NESTED_MORSE = {" ": "/ ",
                        "A": ".-",
                        "E": ".",
                        "I": "..",
                        "M": "--",
                        "Q": "--.-",
                        "U": "..-",
                        "Y": "-.--",
                        "B": "-...",
                        "F": "..-.",
                        "J": ".---",
                        "N": "-.",
                        "R": ".-.",
                        "V": "...-",
                        "Z": "--..",
                        "C": "-.-.",
                        "G": "--.",
                        "K": "-.-",
                        "O": "---",
                        "S": "...",
                        "W": ".--",
                        "D": "-..",
                        "H": "....",
                        "L": ".-..",
                        "P": ".--.",
                        "T": "-",
                        "X": "-..-",
                        "A": ".-",
                        "0": "-----",
                        "3": "...--",
                        "6": "-....",
                        "9": "----.",
                        "1": ".----",
                        "4": "....-",
                        "7": "--...",
                        "2": "..---",
                        "5": ".....",
                        "8": "---.."}
        morse = " ".join([NESTED_MORSE.get(i.upper()) for i in string])
        print(morse)
    except ValueError:
        print("AssertionError: the argument is bad")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
