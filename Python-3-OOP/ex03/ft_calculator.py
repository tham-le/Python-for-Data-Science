class calculator:
    '''calculations of vector with a scalar'''

    def __init__(self, vec: list) -> None:
        '''initialize the vector'''
        self.values = vec

    def __str__(self) -> str:
        '''return the vector as a string'''
        return str(self.values)

    def __add__(self, object) -> None:
        '''addition of vector with a scalar'''
        self.values = [x + object for x in self.values]
        print(self.values)

    def __mul__(self, object) -> None:
        '''multiplication of vector with a scalar'''
        self.values = [x * object for x in self.values]
        print(self.values)

    def __sub__(self, object) -> None:
        '''subtraction of vector with a scalar'''
        self.values = [x - object for x in self.values]
        print(self.values)

    def __truediv__(self, object) -> None:
        '''division of vector with a scalar'''
        if object == 0:
            print("Division by zero")
            return
        self.values = [x / object for x in self.values]
        print(self.values)
