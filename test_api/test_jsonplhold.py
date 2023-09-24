import pytest
import requests
from jsonschema import validate
from schemas import jsonplhold_schema_for_1_post, jsonplhold_schema_for_post_query, jsonplhold_schema_for_patch_query


def test_check_avail_jsonplhold(url_jsplhold):
    response = requests.get(url_jsplhold)
    assert response.status_code == 200


@pytest.mark.parametrize('items', [1, 10, 23, 51, 87])
def test_get_post(items, url_jsplhold):
    res = requests.get(f'{url_jsplhold}posts/{items}')
    validate(instance=res.json(), schema=jsonplhold_schema_for_1_post)


@pytest.mark.parametrize('json', [{'title': 'foo', 'body': 'bar', 'userId': 1}, {'title': 'car', 'body': 'testa', 'userId': 2}])
def test_postquery_posts(json, url_jsplhold):
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    res = requests.post(url=f'{url_jsplhold}posts',
                        headers=headers,
                        json=json)
    validate(instance=res.json(), schema=jsonplhold_schema_for_post_query)


@pytest.mark.parametrize('json', [{'id': 1, 'title': 'foo', 'body': 'bar', 'userId': 1},
                                  {'id': 1, 'title': 'car', 'body': 'testa', 'userId': 2}])
def test_putquery_posts(json, url_jsplhold):
    res = requests.put(url=f'{url_jsplhold}posts/1', data=json)
    validate(instance=res.json(), schema=jsonplhold_schema_for_post_query)


def test_patch_user(url_jsplhold):
    res = requests.patch(url=f'{url_jsplhold}todos/31', json={"completed": True})
    validate(instance=res.json(), schema=jsonplhold_schema_for_patch_query)

''' С начала сделал так, чтоб todos проверялся до изменения и сравнивался с изменениями после, но т.к.
на тестовом сервере изменения не сохраняются использовал xfail, но это не сходится с заданием - 
Тесты должны успешно проходить. Пришлось переделать

@pytest.mark.xfail(strict=True)  # reason='The data on the test bench does not change'
def test_patch_user(url_jsonplhold):
    res_get = requests.get(url=f'{url_jsonplhold}todos/31')
    res_patch = requests.patch(url=f'{url_jsonplhold}todos/31', data={"completed": True})
    res_get_after_patch = requests.get(url=f'{url_jsonplhold}todos/31')
    assert res_get.json() != res_patch.json() and res_get.json() != res_get_after_patch.json()
'''