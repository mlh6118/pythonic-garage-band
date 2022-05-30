class Band:
    # Define class attribute
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        # Call instances, but need 'Band' before it since instances is
        # defined outside the method.
        Band.instances.append(self)

    def name(self):
        return self.name

    # Self has is a parameter that has an attribute called members that was
    # put there by __init__.
    def play_solos(self):
        list_solos = []
        for member in self.members:
            list_solos.append(member.play_solo())
        return list_solos

    @classmethod
    def to_list(cls):
        return Band.instances


class Musician:
    pass


class Guitarist(Musician):
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

    @staticmethod
    def play_solo():
        return 'face melting guitar solo'


class Bassist(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return 'bass'

    @staticmethod
    def play_solo():
        return 'bom bom buh bom'


class Drummer(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return 'drums'

    @staticmethod
    def play_solo():
        return 'rattle boom crash'


if __name__ == '__main__':
    guitarist1 = Guitarist('Joan Jett')
    print(guitarist1.name)
