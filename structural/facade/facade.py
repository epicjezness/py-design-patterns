from .generators import AgeGenerator, NameGenerator


class PersonFacade(object):
    """
    Class for Person generation.
    Acts as a facade for generators.
    """

    @staticmethod
    def generate_person():
        first_name = NameGenerator.generate_first_name()
        last_name = NameGenerator.generate_last_name()
        age = AgeGenerator.generate_age()

        return f'{first_name} {last_name} - {age} years old.'
