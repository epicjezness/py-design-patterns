class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python.
    Some possible methods include: base class, decorator, metaclass.
    This example will use metaclass.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Override for __call__ dunder method.
        Possible changes to the value of the `__init__` argument do not affect the returned instance.
        """

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]
