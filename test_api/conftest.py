import pytest


@pytest.fixture
def url_dog():
    return "https://dog.ceo/"


@pytest.fixture
def url_brewery():
    return "https://api.openbrewerydb.org/"


@pytest.fixture
def url_jsplhold():
    return "https://jsonplaceholder.typicode.com/"


def pytest_addoption(parser):
    parser.addoption('--url', default='https://ya.ru', help='This is request url')
    parser.addoption('--status_code', default=200, help='This is request status_code answer')
