import sys


def main():
    try:
        if len(sys.argv) < 2:
            exit(1)
        if len(sys.argv) > 2:
            raise Exception("AssertionError: more than one argument provided")
        number = int(sys.argv[1])
        if number % 2 == 0:
            print("I am Even")
        else:
            print("I am Odd")
    except ValueError:
        print("AssertionError: argument is not an integer")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
