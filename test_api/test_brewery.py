import pytest
import requests
from jsonschema import validate
from schemas import brewery_schema_for_single, brewery_schema_for_meta
from classes import Brewery
import uuid


def test_check_avail_brewery(url_brewery):
    response = requests.get(url_brewery)
    assert response.status_code == 200


@pytest.mark.parametrize('item', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_schema_single_brewery(url_brewery, item):
    res = requests.get(f'{url_brewery}v1/breweries/{Brewery.get_brewery_id(item)}')
    validate(instance=res.json(), schema=brewery_schema_for_single)


@pytest.mark.parametrize('item', [0, 1, 2, 3, 4], ids=['1 in 5', '2 in 5', '3 in 5', '4 in 5', '5 in 5'])
@pytest.mark.parametrize('name', ['cooper', 'brewery', 'cafe'])
def test_by_name(url_brewery, name, item):
    query = {'by_name': name, 'per_page': 5}
    res = requests.get(f'{url_brewery}v1/breweries/', params=query)
    assert res.json()[item]['name'].casefold().__contains__(name)


def test_random_brewery(url_brewery):
    query = {'size': 3}
    res = requests.get(f'{url_brewery}v1/breweries/random', params=query)
    first = uuid.UUID(res.json()[0]['id'])
    second = uuid.UUID(res.json()[1]['id'])
    third = uuid.UUID(res.json()[2]['id'])
    assert first != second and first != third and second != third


@pytest.mark.parametrize('country', ['south_korea', 'united_states'])
def test_schema_meta(url_brewery, country):
    query = {'by_country': country}
    res = requests.get(f'{url_brewery}v1/breweries/meta', params=query)
    validate(instance=res.json(), schema=brewery_schema_for_meta)
