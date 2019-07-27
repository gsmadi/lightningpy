import abc
from typing import Dict, List
import json

class LNDClientAbstraction(metaclass=abc.ABCMeta):
    """
    Abstraction class that defines all methods available for a LND
        client that an Implementation class must implement.

    """
    
    @abc.abstractmethod
    def get_info(self) -> object:
        pass
