import pytest

from lnd.client import LNDClientBase
from lnd.client.abstraction import LNDClientAbstraction


def dummy_implementor(Cls):
    class NewCls(object):
        def __init__(self,*args,**kwargs):
            def fake_method(*args, **kwargs):
                pass

            for method in Cls.__dict__.get('__abstractmethods__'):
                setattr(NewCls, method, fake_method)

    return NewCls

@dummy_implementor
class DummyClientImplmentor(LNDClientAbstraction):
    pass

class DummyClient(LNDClientBase):
    pass

@pytest.fixture
def client():
    #pylint: disable=abstract-class-instantiated
    return DummyClient(DummyClientImplmentor()) 

def test_implements_address_new(client):
    _ = client.address_new()
    _ = client.address_new('type')

def test_implements_channel_close(client):
    _ = client.channel_close('id', 1)

def test_channels_balance(client):
    _ = client.channels_balance()

def test_channels_list(client):
    _ = client.channels_list()
    _ = client.channels_list(active_only=True)
    _ = client.channels_list(inactive_only=True)
    _ = client.channels_list(public_only=True)
    _ = client.channels_list(private_only=True)

def test_channels_open(client):
    _ = client.channels_open()

def test_channels_pending(client):
    _ = client.channels_pending()

def test_fee_estimate(client):
    _ = client.fee_estimate(target_confirmations=1)

def test_fee_report(client):
    _ = client.fee_report()

def test_generate_seed(client):
    _ = client.generate_seed()
    _ = client.generate_seed(aezeed_passphrase='dummy')
    _ = client.generate_seed(seed_entropy='dummy')

def test_graph_describe(client):
    _ = client.graph_describe(include_unannounced=True)

def test_graph_info(client):
    _ = client.graph_info()

def test_graph_channel_info(client):
    _ = client.graph_channel_info('id123')

def test_graph_node_info(client):
    _ = client.graph_node_info('pubkey', True)

def test_info(client):
    _ = client.info()

def test_payments_list(client):
    _ = client.payments_list(True)

def test_payments_delete_all(client):
    _ = client.payments_delete_all()

def test_peers_list(client):
    _ = client.peers_list()

def test_peer_disconnect(client):
    _ = client.peer_disconnect('pubkey')

def test_peer_connect(client):
    _ = client.peer_connect(True, address=('pubkey', 'host'))

def test_transactions_list(client):
    _ = client.transactions_list()

def test_unspent_list(client):
    _ = client.unspent_list(1, 6)

def test_wallet_balance(client):
    _ = client.wallet_balance()

def test_wallet_init(client):
    _ = client.wallet_init(b'pass')
    _ = client.wallet_init(b'pass', cipher_seed_mnemonic=['a', 'b', 'c'],
                           aezeed_passphrase=b'aezeed', recovery_window=1)

def test_wallet_unlock(client):
    _ = client.wallet_unlock(b'pass')
    _ = client.wallet_unlock(b'pass', 1)