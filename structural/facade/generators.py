from random import choice, randint


class AgeGenerator(object):
    """
    Class for generating ages.
    """

    @staticmethod
    def generate_age() -> int:
        """
        Method for generating age.
        """
        _min = 1
        _max = 100

        return randint(_min, _max)


class NameGenerator(object):
    """
    Class for generating names.
    """

    @staticmethod
    def generate_first_name() -> str:
        """
        Method for generating first name.
        """

        first_names = [
            'Aaron',
            'James',
            'John',
            'Matthew',
            'Charles'
        ]

        return choice(first_names)

    @staticmethod
    def generate_last_name() -> str:
        """
        Method for generating first name.
        """

        last_names = [
            'Michaels',
            'Johnson',
            'Anderson',
            'Carter',
            'Parker'
        ]

        return choice(last_names)
