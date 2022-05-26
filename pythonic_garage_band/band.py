class Band():
    pass


class Guitarist:
    def __init__(self, name):
        self.name = name

    # This obtains name from the init above.
    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    # This obtains name from the init above.
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

class Musician():
    pass


class Bassist():
    pass


class Drummer():
    pass


if __name__ == '__main__':
    guitarist1 = Guitarist('Joan Jett')
    print(guitarist1.name)