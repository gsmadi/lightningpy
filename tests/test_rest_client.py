import pytest

from pylnd.rest import LND, LNDRESTClient

URL = 'localhost:8080'
CERT_PATH = 'tests/fake/tls.cert'
MACAROON_PATH = 'tests/fake/admin.macaroon'

@pytest.fixture
def lnd_rest_client():
    lnd = LND(URL, CERT_PATH, MACAROON_PATH)

    return lnd

def test_rest_client_initialize(lnd_rest_client):
    assert lnd_rest_client.url == URL
    assert lnd_rest_client.certificate_path == CERT_PATH
    assert lnd_rest_client.macaroon_path == MACAROON_PATH

def test_client_implements_rest(lnd_rest_client):
    assert isinstance(lnd_rest_client._implementor, LNDRESTClient)