def give_bmi(height: list[int | float], weight: list[int | float])\
            -> list[int | float]:
    """arguments: 2 lists of integers or float of height, weight
    returns: a list of bmi values
    """
    try:
        if (len(height) != len(weight)):
            raise ValueError("The length of height and weight lists \
should be the same")
        for i in range(len(height)):
            if isinstance(height[i], (int, float)) is False:
                raise ValueError("Height should be an integer or float")
            if isinstance(weight[i], (int, float)) is False:
                raise ValueError("Weight should be an integer or float")
            if height[i] <= 0 or weight[i] <= 0:
                raise ValueError("Height and weight should be positive")
        return [weight[i] / height[i] ** 2 for i in range(len(height))]
    except ValueError as e:
        print("An error occurred: ", e)
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """arguments: a list of bmi values and an integer limit
    returns: a list of boolean values, True if bmi is above the limit
    """
    try:
        if not isinstance(bmi, list):
            raise ValueError("bmi should be a list")
        if not all(isinstance(i, (int, float)) for i in bmi):
            raise ValueError("All elements of bmi should be an integer \
or float")
        if not isinstance(limit, int):
            raise ValueError("Limit should be an integer")
        return [True if i > limit else False for i in bmi]
    except ValueError as e:
        print("An error occurred: ", e)
        return None
