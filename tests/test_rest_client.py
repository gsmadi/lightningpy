import pytest
import requests

from pylnd.rest import LND, LNDRESTClient

URL = 'localhost:8080'
CERT_PATH = 'tests/fake/tls.cert'
MACAROON_PATH = 'tests/fake/admin.macaroon'

class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}

@pytest.fixture
def lnd_rest_client(monkeypatch):
    lnd = LNDRESTClient(URL, CERT_PATH, MACAROON_PATH)

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    return lnd

def test_rest_client_initialize(lnd_rest_client):
    assert lnd_rest_client.url == URL
    assert lnd_rest_client.certificate_path == CERT_PATH
    assert lnd_rest_client.macaroon_path == MACAROON_PATH

def test_client_implements_rest(lnd_rest_client):
    assert isinstance(lnd_rest_client, LNDRESTClient)

def test_client_endpoint_method(lnd_rest_client):
    route = '/dummy'

    assert lnd_rest_client._endpoint(route) == f'{URL}{route}'

def test_client_get_request(lnd_rest_client):
    result = lnd_rest_client._get_request('/dummy')

    assert result.json().get('mock_key') == 'mock_response'

def test_lnd_get_info(lnd_rest_client):
    response = lnd_rest_client.get_info()

    assert isinstance(response, MockResponse)

def test_lnd_client_initialize():
    lnd = LND(URL, CERT_PATH, MACAROON_PATH)

    assert isinstance(lnd._implementor, LNDRESTClient)
