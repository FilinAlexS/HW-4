import pytest
import requests
from jsonschema import validate
from schemas import dogs_schema_random_1, dogs_schema_random_more_1
from classes import Dogceo


def test_check_avail_dog_ceo(url_dog):
    response = requests.get(url_dog)
    assert response.status_code == 200


def test_random_1_dogs(url_dog):
    res = requests.get(f'{url_dog}api/breeds/image/random')
    validate(instance=res.json(), schema=dogs_schema_random_1)


@pytest.mark.parametrize('quantity', [-1, 0, 'a', 51, 45],
                         ids=["negative", "zero", "text", "out_of_range", "valid_value"])
def test_random3_dogs(quantity, url_dog):
    res = requests.get(f'{url_dog}api/breeds/image/random/{quantity}')
    validate(instance=res.json(), schema=dogs_schema_random_more_1)


@pytest.mark.parametrize('checklist', Dogceo.get_list_breads())
def test_all_breeds_dogs(checklist, url_dog):
    res = requests.get(f'{url_dog}api/breed/{checklist}/images')
    validate(instance=res.json(), schema=dogs_schema_random_more_1)


@pytest.mark.parametrize('checklist', Dogceo.get_list_breads())
def test_all_breeds_dogs_random(checklist, url_dog):
    res = requests.get(f'{url_dog}api/breed/{checklist}/images/random')
    validate(instance=res.json(), schema=dogs_schema_random_1)
