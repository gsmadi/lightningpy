from pylnd.abstraction import LNDClientAbstraction

class LNDClientBase(object):
    """
    Base class for any LND client implementation to inherit.

    """

    _implementor: LNDClientAbstraction
    url: str
    certificate_path: str
    macaroon_path: str

    def __init__(self, url: str, certificate_path: str, macaroon_path: str):
        self.url = url
        self.certificate_path = certificate_path
        self.macaroon_path = macaroon_path
    
    def get_info(self) -> object:
        response = self._implementor.get_info()

        return response
