from typing import List

from pylnd.abstraction import LNDClientAbstraction

class LNDClientBase(object):
    """
    Base class for any LND client implementation to inherit.

    """

    _implementor: LNDClientAbstraction

    def __init__(self, implementor):
        self._implementor = implementor

    def generate_seed(self,
                      aezeed_passphrase: str = None,
                      seed_entropy: str = None) -> object:
        response = self._implementor.generate_seed(aezeed_passphrase,
                                                   seed_entropy)

        return response

    def info(self) -> object:
        response = self._implementor.info()

        return response

    def wallet_init(self,
                    wallet_password: bytes,
                    cipher_seed_mnemonic: List[str] = None,
                    aezeed_passphrase: bytes = None,
                    recovery_window: int = 0,
                    channel_backups: object = None) -> object:
        response = self._implementor.wallet_init(wallet_password,
                                                 cipher_seed_mnemonic,
                                                 aezeed_passphrase,
                                                 recovery_window,
                                                 channel_backups)

        return response

    def wallet_unlock(self,
                      wallet_password: bytes,
                      recovery_window: int = 0,
                      channel_backups: object = None) -> object:
        response = self._implementor.wallet_init(wallet_password,
                                                 recovery_window,
                                                 channel_backups)

        if response is None:
            return False

        return True
