class calculator:
    '''calculations of vector with a scalar'''

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''dot product of two vectors'''
        if len(V1) != len(V2):
            print("Error: Vectors must have the same size")
            return
        print("Dot product is: ", sum(list(map(lambda x, y: x * y, V1, V2))))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''addition of two vectors'''
        if len(V1) != len(V2):
            print("Error: Vectors must have the same size")
            return
        print("Add Vector is: ", list(map(lambda x, y: float(x + y), V1, V2)))
        # list(map(sum, zip(V1, V2))) #this is better but can not do float

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''subtraction of two vectors'''
        if len(V1) != len(V2):
            print("Error: Vectors must have the same size")
            return
        print("Sous Vector is: ", list(map(lambda x, y: float(x - y), V1, V2)))
