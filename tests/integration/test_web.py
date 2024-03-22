import asyncio
import pytest
import httpx

from src.core.database import init_models
from tests.unit.conftest import make_user


asyncio.run(init_models())


def test_can_create_user(domain):
    response = httpx.post(domain + '/users/create', json=make_user().__dict__)
    httpx.post(domain + '/users/create', json=make_user().__dict__)
    assert response.status_code == 200


def test_can_edit_user(domain):
    response = httpx.patch(domain + '/users/update/1', json=make_user().__dict__)
    assert response.status_code == 200


def test_can_get_user_list(domain):
    response = httpx.get(domain + '/users/list')
    assert isinstance(response.json(), list)


def test_can_delete_user(domain):
    response = httpx.delete(domain + '/users/delete/1')
    assert response.status_code == 200


def test_can_create_note(dummy_note_dict, domain):
    response = httpx.post(domain + '/notes/create', json=dummy_note_dict)
    assert response.status_code == 200


def test_can_not_create_note_invalid_author_id(dummy_note_dict, domain):
    data = dummy_note_dict
    data['author_id'] = 0
    with pytest.raises(httpx.HTTPError):
        response = httpx.post(domain + '/notes/create', json=data)
        response.raise_for_status()


def test_note_limit_works(dummy_note_dict, domain):
    httpx.post(domain + '/notes/create', json=dummy_note_dict)
    httpx.post(domain + '/notes/create', json=dummy_note_dict)
    respone = httpx.get(domain + '/notes/list', params={'limit': 1})
    assert len(respone.json()) <= 1


def test_can_edit_note(dummy_note_dict, domain):
    pass
