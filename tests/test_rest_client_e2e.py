import os
import pytest

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from pylnd.rest import LND

URL = 'https://0.0.0.0:8080'
CERT_PATH = ('tests/fake/tls.cert', 'tests/fake/tls.key')
MACAROON_PATH = '/lnd/data/chain/bitcoin/simnet/macaroon.db'

TEST_ENV = os.environ.get('TEST_ENV', None)
if TEST_ENV == 'DOCKER':
    CERT_PATH = ('/lnd/tls.cert', '/lnd/tls.key')
    MACAROON_PATH = '/lnd/data/chain/bitcoin/simnet/macaroon.db'

@pytest.fixture(scope='module')
def state():
    return {}

@pytest.fixture
def lnd():
    lnd = LND(URL, CERT_PATH, MACAROON_PATH, ssl_verify=False)

    return lnd

@pytest.mark.e2e
def test_generate_seed(state, lnd):
    mnemonic = lnd.generate_seed().json()

    cipher_seed_mnemonic = mnemonic['cipher_seed_mnemonic']
    enciphered_seed = mnemonic['enciphered_seed']

    assert isinstance(cipher_seed_mnemonic, list)
    assert isinstance(enciphered_seed, str)

    state['cipher_seed_mnemonic'] = cipher_seed_mnemonic

@pytest.mark.e2e
def test_wallet_init(state, lnd):
    cipher_seed_mnemonic = state['cipher_seed_mnemonic']
    ret = lnd.wallet_init(b'test1234', cipher_seed_mnemonic=cipher_seed_mnemonic)

    assert ret.status_code == 200
