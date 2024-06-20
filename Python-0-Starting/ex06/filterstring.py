import sys
from ft_filter import ft_filter


def main():
    """accepts two arguments: a string(S), and an integer(N)
Output a list of words from S that have a length greater than N"""
    try:
        if len(sys.argv) != 3:
            raise Exception("AssertionError: two arguments are required")
        n = int(sys.argv[2])
        string = sys.argv[1]
        if isinstance(string, str) is False or isinstance(n, int) is False:
            raise Exception("AssertionError: type error")
        if n < 0:
            raise Exception("AssertionError: the second argument \
must be a positive integer")
        words = string.split()
        print(ft_filter(lambda x: len(x) > n, words))
    except ValueError:
        print("AssertionError: the arguments are bad, \
use a string and an integer")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
