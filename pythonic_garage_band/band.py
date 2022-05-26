class Band():
    def __init__(self, name, members):
        self.name = name

    def name(self):
        return self.name


class Guitarist:
    def __init__(self, name):
        self.name = name

    # This obtains name from the init above.
    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    # This obtains name from the init above.
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return 'guitar'


class Musician():
    pass


class Bassist():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return 'bass'

class Drummer():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return 'drums'

if __name__ == '__main__':
    guitarist1 = Guitarist('Joan Jett')
    print(guitarist1.name)