import numpy as np  # using numpy


def slice_me(family: list, start: int, end: int) -> list:
    """take a 2d array, print its shape
and returns a truncated version of the array based on the provided start
and end arguments.
    args: 2d array, start index, end index
    return: 2d array"""
    try:
        if (not isinstance(family, list) or
                not all(type(i) is list for i in family)):
            raise Exception("Input is not a 2D array")
        if (type(start) is not int or type(end) is not int):
            raise Exception("Start and end should be integers")
        if all(len(i) != len(family[0]) for i in family):
            raise Exception("Irregular 2D array")
        print(f"My shape is: ({np.array(family).shape})")
        print(f"My new shape is: ({np.array(family[start:end]).shape})")
        return family[start:end]

    except Exception as e:
        print("An error occurred:", e)
        return None

# def slice_me(family: list, start: int, end: int) -> list:
#     """take a 2d array, print its shape
# and returns a truncated version of the array based on the provided start
# and end arguments.
#     args: 2d array, start index, end index
#     return: 2d array"""
#     try:
#         if (not isinstance(family, list) or
#                 not all(type(i) is list for i in family)):
#             raise Exception("Input is not a 2D array")
#         if (type(start) is not int or type(end) is not int):
#             raise Exception("Start and end should be integers")
#         if all(len(i) != len(family[0]) for i in family):
#             raise Exception("Irregular 2D array")
#         h = len(family)
#         w = len(family[0])
#         print(f"My shape is: ({h}, {w})")
#         truncated = family[start:end]
#         print(f"My new shape is: ({len(truncated)}, {w})")
#         return truncated

#     except Exception as e:
#         print(e)
#         return None
