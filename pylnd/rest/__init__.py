import base64
import codecs
import json
import requests

from typing import Dict

from pylnd.abstraction import LNDClientAbstraction
from pylnd.utils import encode_macaroon
from pylnd import LNDClientBase
from pylnd.utils import encode_macaroon, read_file

url = 'https://localhost:8080'
cert_path = 'LND_DIR/tls.cert'


class LNDRESTClient(LNDClientAbstraction):
    
    headers: Dict[str, object]
    url: str
    certificate_path: str
    macaroon_path: str

    def __init__(self, url, certificate_path, macaroon_path):
        macaroon = read_file(certificate_path)
        encoded_macaroon = encode_macaroon(macaroon)
        self.headers = {'Grpc-Metadata-macaroon': encoded_macaroon}
    
    def get_info(self) -> object:
        route = '/v1/getinfo'

        return self._get_request(route)

    def _endpoint(self, route):
        return f'{self.url}{route}'

    def _get_request(self, route):
        r = requests.get(self._endpoint(route),
                         headers=self.headers,
                         verify=self.certificate_path)
        return r

class LND(LNDClientBase):
    def __init__(self, url, certificate_path, macaroon_path):
        super().__init__(url, certificate_path, macaroon_path)
        self._implementor = LNDRESTClient(url, certificate_path,
                                          macaroon_path)

