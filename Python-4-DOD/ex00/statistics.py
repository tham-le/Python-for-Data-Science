from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculate the mean, median, quartile, standard deviation,
 and variance of a list of numbers."""

    def mean(list_: Any) -> float:
        '''returns the mean of a list'''
        return sum(list_) / len(list_)

    def median(list_: Any) -> float:
        '''returns the median of a list'''
        list_ = sorted(list_)
        n = len(list_)
        if n % 2 == 0:
            return (list_[(n - 1) // 2] + list_[(n + 1) // 2]) / 2
        return list_[n // 2]

    def quartile(ls: list[int | float]) -> None:
        '''Calculate Quartile (25% and 75%)'''
        if len(ls) == 1:
            return [ls[0], ls[0]]
        s = sorted(ls)
        n = len(s)
        q1 = (s[(n - 1) // 4] + s[n // 4]) / 2
        q3 = (s[(n - 1) * 3 // 4] + s[n * 3 // 4]) / 2
        return q1, q3

    def std(list_: Any) -> float:  # ecart type
        '''returns the standard deviation of a list'''
        m = mean(list_)
        return (sum((x - m) ** 2 for x in list_) / len(list_)) ** 0.5

    def var(list_: Any) -> float:
        '''returns the variance of a list'''
        m = mean(list_)
        return sum((x - m) ** 2 for x in list_) / len(list_)

    if len(args) == 0:
        print("ERROR: no arguments given")
        return
    if len(kwargs) == 0:
        print("ERROR: no keyword arguments given")
        return

    op_dict = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": std,
        "var": var
    }

    num_list = [x for x in args if isinstance(x, (int, float))]
    for key, value in kwargs.items():
        if value in op_dict:
            print(f"{value}: {op_dict[value](num_list)}")
        else:
            print(f"ERROR: unknown keyword argument '{key}'")
