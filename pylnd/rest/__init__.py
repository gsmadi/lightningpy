import base64
import codecs
import json
from typing import Dict, List
import requests

from pylnd.abstraction import LNDClientAbstraction
from pylnd import LNDClientBase
from pylnd.utils import encode_macaroon, read_file


class LNDRESTClient(LNDClientAbstraction):

    headers: Dict[str, any]
    url: str
    certificate_path: str
    macaroon_path: str
    ssl_verify: bool

    def __init__(self, url, certificate_path, macaroon_path, ssl_verify=False):
        self.url = url
        self.certificate_path = certificate_path
        self.macaroon_path = macaroon_path
        self.ssl_verify = ssl_verify

        macaroon = read_file(macaroon_path)
        encoded_macaroon = encode_macaroon(macaroon)
        self.headers = {'Grpc-Metadata-macaroon': encoded_macaroon}

    def generate_seed(self,
                      aezeed_passphrase: str = None,
                      seed_entropy: str = None) -> object:
        route = '/v1/genseed'
        params = {}

        if aezeed_passphrase:
            params['aezeed_passphrase'] = aezeed_passphrase

        if seed_entropy:
            params['seed_entropy'] = seed_entropy

        return self._get_request(route, params)

    def info(self) -> object:
        route = '/v1/getinfo'

        return self._get_request(route)

    def wallet_init(self,
                    wallet_password: bytes,
                    cipher_seed_mnemonic: List[str],
                    aezeed_passphrase: bytes = None,
                    recovery_window: int = 0,
                    channel_backups: object = None) -> bool:
        route = '/v1/unlockwallet'
        data = {
            'wallet_password': base64.b64encode(wallet_password).decode(),
            'cipher_seed_mnemonic': cipher_seed_mnemonic,
            'aezeed_passphrase': base64.b64encode(aezeed_passphrase).decode(),
            'recovery_window': recovery_window,
        }

        if channel_backups:
            data['channel_backups'] = channel_backups

        self._post_request(route, data)

        return True

    def wallet_unlock(self,
                      wallet_password: bytes,
                      recovery_window: int = 0,
                      channel_backups: object = None) -> bool:
        route = '/v1/unlockwallet'
        data = {
            'wallet_password': base64.b64encode(wallet_password).decode(),
            'recovery_window': recovery_window
        }

        if channel_backups:
            data['channel_backups'] = channel_backups

        self._post_request(route, data)

        return True

    def _endpoint(self, route) -> str:
        return f'{self.url}{route}'

    def _get_request(self, route, params: Dict[str, any] = None) -> object:
        if not params:
            params = {}

        response = requests.get(self._endpoint(route),
                                headers=self.headers,
                                cert=self.certificate_path,
                                verify=self.ssl_verify,
                                params=params)
        return response

    def _post_request(self, route, data) -> object:
        response = requests.post(self._endpoint(route),
                                 cert=self.certificate_path,
                                 verify=self.ssl_verify,
                                 data=json.dumps(data))
        return response


class LND(LNDClientBase):
    def __init__(self, url, certificate_path, macaroon_path, ssl_verify=False):
        implementor = LNDRESTClient(url, certificate_path,
                                    macaroon_path, ssl_verify=ssl_verify)
        super().__init__(implementor)
