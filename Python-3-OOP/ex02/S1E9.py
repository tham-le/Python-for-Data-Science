from abc import ABC, abstractmethod


class Character(ABC):
    """abtract class for a character that have a name and alive(maybe)"""

    def __init__(self, first_name: str, is_alive=True) -> None:
        '''Initialise a character with a name and a health stage as alive'''
        super().__init__()
        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self) -> str:
        '''return the name of the character'''
        return self.first_name

    @abstractmethod
    def die(self):
        '''kill the character'''
        pass


class Stark(Character):
    '''GOT character of the House Stark'''

    def die(self):
        '''kill the character'''
        if self.is_alive is False:
            print(f'{self.first_name} is already dead')
            return
        self.is_alive = False
