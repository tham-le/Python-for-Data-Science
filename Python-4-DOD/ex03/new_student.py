import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''generate a random id'''
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    '''info of a student'''

    name: string
    surname: string
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.login = self.name.lower()[0] + self.surname.lower()

#  https://docs.python.org/3/library/dataclasses.html
