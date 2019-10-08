import pytest
import requests

from lnd.client.rest import LND, LNDRESTClient, LNDRESTClientError

URL = 'localhost:8080'
CERT_PATH = 'tests/fake/tls.cer'
MACAROON_PATH = 'tests/fake/admin.macaroon'

class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


@pytest.fixture
def lnd_rest_client(monkeypatch):
    lnd = LNDRESTClient(URL, CERT_PATH, MACAROON_PATH, ssl_verify=False)

    def mock_get(*args, **kwargs):
        return MockResponse()

    def mock_post(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)
    monkeypatch.setattr(requests, 'post', mock_post)

    return lnd

def test_rest_client_initialize(lnd_rest_client):
    assert lnd_rest_client.url == URL
    assert lnd_rest_client.certificate_path == CERT_PATH
    assert lnd_rest_client.macaroon_path == MACAROON_PATH
    assert lnd_rest_client.ssl_verify == False

def test_client_implements_rest(lnd_rest_client):
    assert isinstance(lnd_rest_client, LNDRESTClient)

def test_client_endpoint_method(lnd_rest_client):
    route = '/dummy'

    assert lnd_rest_client._endpoint(route) == f'{URL}{route}'

def test_client_get_request(lnd_rest_client):
    result = lnd_rest_client._get_request('/dummy')

    assert result.json().get('mock_key') == 'mock_response'

def test_client_handle_error(lnd_rest_client):
    error_response = MockResponse()

    def json_error():
        return {"error": "mock_error"}

    setattr(error_response, 'json', json_error)

    with pytest.raises(LNDRESTClientError):
        lnd_rest_client._handle_error(error_response)

def test_client_post_request(lnd_rest_client):
    result = lnd_rest_client._post_request('/dummy', {'mock': 'param'})

    assert result.json().get('mock_key') == 'mock_response'

def test_info(lnd_rest_client):
    response = lnd_rest_client.info()
    print(response)
    assert isinstance(response, MockResponse)

def test_generate_seed(lnd_rest_client):
    response = lnd_rest_client.generate_seed()

    assert isinstance(response, MockResponse)

    response = lnd_rest_client.generate_seed(aezeed_passphrase='dummy',
                                             seed_entropy='dummy2')

    assert isinstance(response, MockResponse)

def test_address_new(lnd_rest_client):
    response = lnd_rest_client.address_new()

    assert isinstance(response, MockResponse)

    response = lnd_rest_client.address_new('type')

    assert isinstance(response, MockResponse)

def test_channels_balance(lnd_rest_client):
    response = lnd_rest_client.channels_balance()

    assert isinstance(response, MockResponse)

def test_channels_list(lnd_rest_client):
    response = lnd_rest_client.channels_list()

    assert isinstance(response, MockResponse)

def test_fee_estimate(lnd_rest_client):
    response = lnd_rest_client.fee_estimate(6)

    assert isinstance(response, MockResponse)

def test_fee_report(lnd_rest_client):
    response = lnd_rest_client.fee_report()

    assert isinstance(response, MockResponse)

def test_graph_describe(lnd_rest_client):
    response = lnd_rest_client.graph_describe()

    assert isinstance(response, MockResponse)

def test_graph_info(lnd_rest_client):
    response = lnd_rest_client.graph_info()

    assert isinstance(response, MockResponse)

def test_graph_channel_info(lnd_rest_client):
    response = lnd_rest_client.graph_channel_info('123')

    assert isinstance(response, MockResponse)

def test_graph_node_info(lnd_rest_client):
    response = lnd_rest_client.graph_node_info('123')

    assert isinstance(response, MockResponse)

def test_invoices_list(lnd_rest_client):
    response = lnd_rest_client.invoices_list(True, 1, True)

    assert isinstance(response, MockResponse)

def test_invoices_subsribe(lnd_rest_client):
    response = lnd_rest_client.invoices_subscribe('i', 'i')

    assert isinstance(response, MockResponse)

def test_payments_list(lnd_rest_client):
    response = lnd_rest_client.payments_list()

    assert isinstance(response, MockResponse)

def test_peers_list(lnd_rest_client):
    response = lnd_rest_client.peers_list()

    assert isinstance(response, MockResponse)

def test_transactions_list(lnd_rest_client):
    response = lnd_rest_client.transactions_list()

    assert isinstance(response, MockResponse)

def test_unspent_list(lnd_rest_client):
    response = lnd_rest_client.unspent_list(1, 7)

    assert isinstance(response, MockResponse)

def test_wallet_balance(lnd_rest_client):
    response = lnd_rest_client.wallet_balance()

    assert isinstance(response, MockResponse)

def test_lnd_wallet_init(lnd_rest_client):
    response = lnd_rest_client.wallet_init(b'password',
                                           ['str'],
                                           b'passphrase',
                                           2)

    assert isinstance(response, MockResponse)

def test_lnd_wallet_unlock(lnd_rest_client):
    response = lnd_rest_client.wallet_unlock(b'password', 2)

    assert isinstance(response, MockResponse)

def test_lnd_client_initialize():
    lnd = LND(URL, CERT_PATH, MACAROON_PATH)

    assert isinstance(lnd._implementor, LNDRESTClient)

# def test_client_init_macaroon(lnd_rest_client):
#     self._init_macaroon()
