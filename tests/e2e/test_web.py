import asyncio
import pytest
import httpx

from src.database import init_models
from tests.unit.conftest import make_user


asyncio.run(init_models())


def test_can_create_user(domain):
    user_data = make_user()
    response = httpx.post(domain + '/users/create', json=user_data.__dict__)
    assert response.status_code == 200


def test_can_create_note(dummy_note_dict, domain):
    response = httpx.post(domain + '/notes/create', json=dummy_note_dict)
    assert response.status_code == 200


def test_can_not_create_note(dummy_note_dict, domain):
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
