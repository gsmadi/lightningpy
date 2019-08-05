import abc
from typing import Dict, List
import json

class LNDClientAbstraction(metaclass=abc.ABCMeta):
    """
    Abstraction class that defines all methods available for a LND
        client that an Implementation class must implement.

    """

    @abc.abstractmethod
    def generate_seed(self,
                      aezeed_passphrase: str = None,
                      seed_entropy: str = None) -> object:
        pass

    @abc.abstractmethod
    def info(self) -> object:
        pass

    @abc.abstractmethod
    def wallet_init(self,
                    wallet_password: bytes,
                    cipher_seed_mnemonic: List[str],
                    aezeed_passphrase: bytes = None,
                    recovery_window: int = 0,
                    channel_backups: object = None) -> bool:
        pass

    @abc.abstractmethod
    def wallet_unlock(self,
                      wallet_password: bytes,
                      recovery_window: int = 0,
                      channel_backups: object = None) -> bool:
        pass
