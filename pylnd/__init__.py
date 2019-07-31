from pylnd.abstraction import LNDClientAbstraction

class LNDClientBase(object):
    """
    Base class for any LND client implementation to inherit.

    """

    _implementor: LNDClientAbstraction

    def __init__(self, implementor):
        self._implementor = implementor

    def get_info(self) -> object:
        response = self._implementor.get_info()

        return response
