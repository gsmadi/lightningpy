from typing import List, Tuple

from lnd.client.abstraction import LNDClientAbstraction

class LNDClientBase(object):
    """
    Base class for any LND client implementation to inherit.

    """

    _implementor: LNDClientAbstraction

    def __init__(self, implementor):
        self._implementor = implementor


    def address_new(self, address_type: str = None) -> object:
        response = self._implementor.address_new(address_type)

        return response

    def channel_close(self, funding_txid: str, output_index: int) -> object:
        response = self._implementor.channel_close(funding_txid, output_index)

        return response

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
        raise NotImplementedError()

    def channel_policy_update(self,
                              chan_point: dict,
                              time_lock_delta: int,
                              base_fee_msat: str,
                              fee_rate: float,
                              is_global: bool) -> object:
        raise NotImplementedError()

    def channels_balance(self) -> object:
        response = self._implementor.channels_balance()

        return response

    def channels_closed(self,
                        cooperative: bool,
                        local_force: bool,
                        remote_force: bool,
                        breach: bool,
                        funding_canceled: bool,
                        abandoned: bool) -> object:
        raise NotImplementedError()

    def channels_list(self,
                      active_only: bool,
                      inactive_only: bool,
                      public_only: bool,
                      private_only: bool) -> object:
        raise NotImplementedError()

    def channels_open(self) -> object:
        response = self._implementor.channels_open()

        return response

    def channels_pending(self) -> object:
        response = self._implementor.channels_pending()

        return response

    def fee_estimate(self, target_confirmations: int) -> object:
        response = self._implementor.fee_estimate(target_confirmations)

        return response

    def fee_report(self) -> object:
        response = self._implementor.fee_report()

        return response

    def generate_seed(self,
                      aezeed_passphrase: str = None,
                      seed_entropy: str = None) -> object:
        response = self._implementor.generate_seed(aezeed_passphrase,
                                                   seed_entropy)

        return response

    def graph_describe(self, include_unannounced: bool) -> object:
        response = self._implementor.graph_describe(include_unannounced)

        return response

    def graph_info(self) -> object:
        response = self._implementor.graph_info()

        return response

    def graph_channel_info(self, channel_id: str) -> object:
        response = self._implementor.graph_channel_info(channel_id)

        return response

    def graph_node_info(self, pub_key: str, include_channels: bool) -> object:
        response = self._implementor.graph_node_info()

        return response

    def graph_query_routes(self,
                           pub_key: str,
                           amount: str,
                           final_cltv_delta: int,
                           fee_fixed_limit: str,
                           fee_percent_limit: str,
                           ignored_nodes: list,
                           source_pub_key: str,
                           use_mission_control: bool) -> object:
        raise NotImplementedError()

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
        raise NotImplementedError()

    def invoice_lookup(self, r_hash_string: str, r_hash: str) -> object:
        raise NotImplementedError()

    def invoices_list(self,
                      pending_only: bool,
                      index_offset: str,
                      num_max_invoices: str,
                      reverse: bool) -> object:
        raise NotImplementedError()

    def invoices_subscribe(self, add_index: str, settle_index: str) -> object:
        raise NotImplementedError()

    def message_sign(self, msg: bytes) -> object:
        raise NotImplementedError()

    def message_verify(self, msg: bytes, signiture: str) -> object:
        raise NotImplementedError()

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
        raise NotImplementedError()

    def payment_route(self,
                      route: dict,
                      payment_hash: bytes,
                      payment_hash_string: str) -> object:
        raise NotImplementedError()

    def payments_list(self, include_incomplete: bool) -> object:
        response = self._implementor.payments_list(include_incomplete)

        return response

    def payments_delete_all(self) -> object:
        response = self._implementor.payments_delete_all()

        return response

    def peers_list(self) -> object:
        response = self._implementor.peers_list()

        return response

    def peer_disconnect(self, pub_key: str) -> object:
        response = self._implementor.peer_disconnect(pub_key)

        return response

    def peer_connect(self, perm: bool, address: Tuple[str, str]) -> object:
        response = self._implementor.peer_connect(perm, address)

        return response

    def transaction_send(self,
                         send_all: bool,
                         target_confirmations: int,
                         amount: str,
                         sat_per_byte: str,
                         address: str) -> object:
        raise NotImplementedError()

    def transactions_list(self) -> object:
        response = self._implementor.transactions_list()

        return response

    def unspent_list(self,
                     minimum_confirmations: int,
                     maximum_confirmations: int) -> object:
        response = self._implementor.unspent_list(minimum_confirmations,
                                                  maximum_confirmations)

        return response

    def wallet_balance(self) -> object:
        response = self._implementor.wallet_balance()

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
        response = self._implementor.wallet_unlock(wallet_password,
                                                   recovery_window,
                                                   channel_backups)

        return response
