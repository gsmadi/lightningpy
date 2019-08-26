from typing import List, Tuple

from lnd.client.abstraction import LNDClientAbstraction

class LNDClientBase(object):
    """
    Base class for any LND client implementation to inherit.

    """

    _implementor: LNDClientAbstraction

    def __init__(self, implementor):
        self._implementor = implementor


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

    def generate_seed(self,
                      aezeed_passphrase: str = None,
                      seed_entropy: str = None) -> object:
        response = self._implementor.generate_seed(aezeed_passphrase,
                                                   seed_entropy)

        return response

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

    def info(self) -> object:
        response = self._implementor.info()

        return response

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
        response = self._implementor.wallet_unlock(wallet_password,
                                                   recovery_window,
                                                   channel_backups)

        return response
