import os
import pytest
import time

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from lnd.client.rest import LND

URL = 'https://0.0.0.0:8080'
CERT_PATH = ('tests/fake/tls.cer', 'tests/fake/tls.key')
MACAROON_PATH = '/lnd/data/chain/bitcoin/simnet/admin.macaroon'

TEST_ENV = os.environ.get('TEST_ENV', None)
if TEST_ENV == 'DOCKER':
    CERT_PATH = ('/lnd/tls.cert', '/lnd/tls.key')
    MACAROON_PATH = '/lnd/data/chain/bitcoin/simnet/admin.macaroon'

@pytest.fixture(scope='module')
def state():
    return {}

@pytest.fixture
def lnd():
    lnd = LND(URL, CERT_PATH, MACAROON_PATH, ssl_verify=False)

    return lnd

@pytest.mark.int
def test_generate_seed(state, lnd):
    mnemonic = lnd.generate_seed().json()

    cipher_seed_mnemonic = mnemonic['cipher_seed_mnemonic']
    enciphered_seed = mnemonic['enciphered_seed']

    assert isinstance(cipher_seed_mnemonic, list)
    assert isinstance(enciphered_seed, str)

    state['cipher_seed_mnemonic'] = cipher_seed_mnemonic

@pytest.mark.int
def test_wallet_init(state, lnd):
    cipher_seed_mnemonic = state['cipher_seed_mnemonic']
    ret = lnd.wallet_init(b'test1234', cipher_seed_mnemonic=cipher_seed_mnemonic)

    assert ret.status_code == 200

    time.sleep(10)

# @pytest.mark.int
# def test_wallet_unlock(state, lnd):
#     ret = lnd.wallet_unlock(b'test1234')

#     assert ret.status_code == 200

@pytest.mark.int
def test_info(state, lnd):
    ret = lnd.info()
    print(ret.json())
    assert ret.status_code == 200

@pytest.mark.int
def test_address_new(state, lnd):
    ret = lnd.address_new()
    print(ret.json())
    assert ret.status_code == 200

@pytest.mark.int
def test_channels_balance(state, lnd):
    ret = lnd.channels_balance()
    print(ret.json())
    assert ret.status_code == 200
