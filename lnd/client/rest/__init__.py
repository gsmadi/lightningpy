import base64
import codecs
import json
from typing import Dict, List, Tuple
import requests

from lnd.client.abstraction import LNDClientAbstraction
from lnd.client import LNDClientBase
from lnd.utils import encode_macaroon, read_file


class LNDRESTClientError(Exception):
    pass

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
        self.headers = {}

    def address_new(self, address_type: str) -> object:
        pass


    def channel_balance(self) -> object:
        pass


    def channel_close(self, funding_txid: str, output_index: int) -> object:
        pass

    def channel_open(self,
                     spend_unconfirmed: bool,
                     push_sat: str,
                     remote_csv_delay: int,
                     private: bool,
                     node_pubkey: bytes,
                     minimum_confirmations: int,
                     node_pubkey_string: str,
                     local_funding_amount: str,
                     sat_per_byte: str,
                     min_htlc_msat: str,
                     target_confirmations: int) -> object:
        pass

    def channels_closed(self,
                        cooperative: bool,
                        local_force: bool,
                        remote_force: bool,
                        breach: bool,
                        funding_canceled: bool,
                        abandoned: bool) -> object:
        pass

    def channels_list(self,
                      active_only: bool,
                      inactive_only: bool,
                      public_only: bool,
                      private_only: bool) -> object:
        pass

    def channels_open(self) -> object:
        pass

    def channels_pending(self) -> object:
        pass

    def fee_estimate(self, target_confirmations: int) -> object:
        pass

    def fee_report(self) -> object:
        pass

    def graph_describe(self, include_unannounced: bool) -> object:
        pass

    def graph_info(self) -> object:
        pass

    def graph_channel_info(self, channel_id: str) -> object:
        pass

    def graph_node_info(self, pub_key: str, include_channels: bool) -> object:
        pass

    def graph_query_routes(self,
                           pub_key: str,
                           amount: str,
                           final_cltv_delta: int,
                           fee_fixed_limit: str,
                           fee_percent_limit: str,
                           ignored_nodes: list,
                           source_pub_key: str,
                           use_mission_control: bool) -> object:
        pass

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

        self._init_macaroon()

        return self._get_request(route)

    def invoice_add(self,
                    amount_paid_must: str,
                    settle_date: str,
                    add_index: str,
                    description_hash: bytes,
                    r_preimage: bytes,
                    state: int,
                    cltv_expiry: str,
                    route_hints: list,
                    r_hash: bytes,
                    creation_date: str,
                    settle_index: str,
                    memo: str,
                    private: bool,
                    expiry: str,
                    fallback_address: str,
                    settled: bool,
                    amount_paid: str,
                    payment_request: str,
                    amount_paid_sat: str,
                    value: str) -> object:
        pass

    def invoice_lookup(self, r_hash_string: str, r_hash: str) -> object:
        pass

    def invoices_list(self,
                      pending_only: bool,
                      index_offset: str,
                      num_max_invoices: str,
                      reverse: bool) -> object:
        pass

    def invoices_subscribe(self, add_index: str, settle_index: str) -> object:
        pass

    def message_sign(self, msg: bytes) -> object:
        pass

    def message_verify(self, msg: bytes, signiture: str) -> object:
        pass

    def payment_send(self,
                     outgoing_channel_id: str,
                     dest: bytes,
                     fee_limit: dict,
                     payment_hash_string: str,
                     dest_string: str,
                     final_cltv_delta: int,
                     payment_hash: bytes,
                     payment_request: str,
                     cltv_limit: int,
                     amount: str) -> object:
        pass

    def payment_route(self,
                      route: dict,
                      payment_hash: bytes,
                      payment_hash_string: str) -> object:
        pass

    def payments_list(self, include_incomplete: bool) -> object:
        pass

    def payments_delete_all(self) -> object:
        pass

    def peers_list(self) -> object:
        pass

    def peer_disconnect(self, pub_key: str) -> object:
        pass

    def peer_connect(self, perm: bool, address: Tuple[str, str]) -> object:
        pass

    def transaction_send(self,
                         send_all: bool,
                         target_confirmations: int,
                         amount: str,
                         sat_per_byte: str,
                         address: str) -> object:
        pass

    def transactions_list(self) -> object:
        pass

    def unspent_list(self,
                     minimum_confirmations: int,
                     maximum_confirmations: int) -> object:
        pass

    def wallet_balance(self) -> object:
        pass

    def wallet_init(self,
                    wallet_password: bytes,
                    cipher_seed_mnemonic: List[str] = None,
                    aezeed_passphrase: bytes = None,
                    recovery_window: int = 0,
                    channel_backups: object = None) -> object:
        route = '/v1/initwallet'
        data = {
            'wallet_password': base64.b64encode(wallet_password).decode(),
            'cipher_seed_mnemonic': cipher_seed_mnemonic,
            'recovery_window': recovery_window,
        }

        if aezeed_passphrase:
            data['aezeed_passphrase'] = base64.b64encode(aezeed_passphrase).decode()

        if channel_backups:
            data['channel_backups'] = channel_backups

        response = self._post_request(route, data)

        return response

    def wallet_unlock(self,
                      wallet_password: bytes,
                      recovery_window: int = 0,
                      channel_backups: object = None) -> object:
        route = '/v1/unlockwallet'
        data = {
            'wallet_password': base64.b64encode(wallet_password).decode(),
            'recovery_window': recovery_window
        }
        if channel_backups:
            data['channel_backups'] = channel_backups

        response = self._post_request(route, data)

        return response

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

        self._handle_error(response)

        return response

    def _post_request(self, route, data) -> object:
        response = requests.post(self._endpoint(route),
                                 headers=self.headers,
                                 cert=self.certificate_path,
                                 verify=self.ssl_verify,
                                 data=json.dumps(data))

        self._handle_error(response)

        return response

    @staticmethod
    def _handle_error(response):
        error = response.json().get('error', None)
        if error:
            raise LNDRESTClientError(error)

    def _init_macaroon(self):
        try:
            macaroon = read_file(self.macaroon_path)
            encoded_macaroon = encode_macaroon(macaroon)
            self.headers.update({'Grpc-Metadata-macaroon': encoded_macaroon})
        except FileNotFoundError:
            raise LNDRESTClientError('Could not find macaroon file')


class LND(LNDClientBase):
    def __init__(self, url, certificate_path, macaroon_path, ssl_verify=False):
        implementor = LNDRESTClient(url, certificate_path,
                                    macaroon_path, ssl_verify=ssl_verify)
        super().__init__(implementor)
