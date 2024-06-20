from S1E9 import Character


class Baratheon(Character):
    '''Representing the Baratheon family.'''

    def __init__(self, first_name, is_alive=True):
        '''Initialise a Baratheon character.'''
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        '''Return a readable representation of the character.'''
        return super().__str__()

    def __repr__(self):
        '''Return a unambiguous representation of the character.'''
        repr = tuple([y for x, y in self.__dict__.items() if
                      x not in ["is_alive", "first_name"]])
        return "Vector: " + str(repr)

    def die(self):
        '''Kill the character'''
        if self.is_alive is False:
            print(f'{self.first_name} of House {self.family_name}\
 already is dead')
        self.is_alive = False


class Lannister(Character):
    '''Class for Lannister characters'''

    def __init__(self, first_name, is_alive=True):
        ''''Initialise a Lannister characters'''
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'green'
        self.hairs = 'light'

    def __str__(self):
        '''Return a readable representation of the character.'''
        return super().__str__()

    def __repr__(self):
        '''Return a unambiguous representation of the character.'''
        repr = tuple([y for x, y in self.__dict__.items() if
                      x not in ["is_alive", "first_name"]])
        return "Vector: " + str(repr)

    def die(self):
        '''Kill the character'''
        if self.is_alive is False:
            print(f'{self.first_name} of House {self.family_name} \
 is already is dead')
        self.is_alive = False

    @classmethod
    def create_lannister(self, first_name, is_alive=True):
        '''Create a Lannister character'''
        return Lannister(first_name, is_alive)
        # return cls(first_name, is_alive) better but flakes8 doesn't like it
