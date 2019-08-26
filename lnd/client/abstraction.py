import abc
from typing import Dict, List, Tuple
import json

class LNDClientAbstraction(metaclass=abc.ABCMeta):
    """
    Abstraction class that defines all methods available for a LND
        client that an Implementation class must implement.

    """

    @abc.abstractmethod
    def address_new(self, address_type: str) -> object:
        pass

    @abc.abstractmethod
    def channel_balance(self) -> object:
        pass

    @abc.abstractmethod
    def channel_close(self, funding_txid: str, output_index: int) -> object:
        pass

    @abc.abstractmethod
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

    @abc.abstractmethod
    def channels_closed(self,
                        cooperative: bool,
                        local_force: bool,
                        remote_force: bool,
                        breach: bool,
                        funding_canceled: bool,
                        abandoned: bool) -> object:
        pass

    @abc.abstractmethod
    def channels_list(self,
                      active_only: bool,
                      inactive_only: bool,
                      public_only: bool,
                      private_only: bool) -> object:
        pass

    @abc.abstractmethod
    def channels_open(self) -> object:
        pass

    @abc.abstractmethod
    def channels_pending(self) -> object:
        pass

    @abc.abstractmethod
    def fee_estimate(self, target_confirmations: int) -> object:
        pass

    @abc.abstractmethod
    def fee_report(self) -> object:
        pass

    @abc.abstractmethod
    def generate_seed(self,
                      aezeed_passphrase: str = None,
                      seed_entropy: str = None) -> object:
        pass

    @abc.abstractmethod
    def graph_describe(self, include_unannounced: bool) -> object:
        pass

    @abc.abstractmethod
    def graph_info(self) -> object:
        pass

    @abc.abstractmethod
    def graph_channel_info(self, channel_id: str) -> object:
        pass

    @abc.abstractmethod
    def graph_node_info(self, pub_key: str, include_channels: bool) -> object:
        pass

    @abc.abstractmethod
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

    @abc.abstractmethod
    def info(self) -> object:
        pass

    @abc.abstractmethod
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

    @abc.abstractmethod
    def invoice_lookup(self, r_hash_string: str, r_hash: str) -> object:
        pass

    @abc.abstractmethod
    def invoices_list(self,
                      pending_only: bool,
                      index_offset: str,
                      num_max_invoices: str,
                      reverse: bool) -> object:
        pass

    @abc.abstractmethod
    def invoices_subscribe(self, add_index: str, settle_index: str) -> object:
        pass

    @abc.abstractmethod
    def message_sign(self, msg: bytes) -> object:
        pass

    @abc.abstractmethod
    def message_verify(self, msg: bytes, signiture: str) -> object:
        pass

    @abc.abstractmethod
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

    @abc.abstractmethod
    def payment_route(self,
                      route: dict,
                      payment_hash: bytes,
                      payment_hash_string: str) -> object:
        pass

    @abc.abstractmethod
    def payments_list(self, include_incomplete: bool) -> object:
        pass

    @abc.abstractmethod
    def payments_delete_all(self) -> object:
        pass

    @abc.abstractmethod
    def peers_list() -> object:
        pass

    @abc.abstractmethod
    def peer_disconnect(self, pub_key: str) -> object:
        pass

    @abc.abstractmethod
    def peer_connect(self, perm: bool, address: Tuple[str, str]) -> object:
        pass

    @abc.abstractmethod
    def transaction_send(self,
                         send_all: bool,
                         target_confirmations: int,
                         amount: str,
                         sat_per_byte: str,
                         address: str) -> object:
        pass

    @abc.abstractmethod
    def transactions_list(self) -> object:
        pass

    @abc.abstractmethod
    def unspent_list(self,
                     minimum_confirmations: int,
                     maximum_confirmations: int) -> object:
        pass

    @abc.abstractmethod
    def wallet_balance(self) -> object:
        pass

    @abc.abstractmethod
    def wallet_init(self,
                    wallet_password: bytes,
                    cipher_seed_mnemonic: List[str] = None,
                    aezeed_passphrase: bytes = None,
                    recovery_window: int = 0,
                    channel_backups: object = None) -> object:
        pass

    @abc.abstractmethod
    def wallet_unlock(self,
                      wallet_password: bytes,
                      recovery_window: int = 0,
                      channel_backups: object = None) -> object:
        pass
