import pytest
import httpx


DOMAIN = 'http://127.0.0.1:8000'
dummy_note_data = {
  'title': 'string',
  'author_id': 1,
  'description': 'string',
  'status': 'UNCOMPLETED',
  'created_at': '2024-03-19T18:32:56.632Z'
}


def test_can_create_note():
    response = httpx.post(DOMAIN + '/notes/create', json=dummy_note_data)
    note = response.json()
    assert note['title'] == 'string'


def test_can_not_create_note():
    data = dummy_note_data
    data['author_id'] = 0
    with pytest.raises(httpx.HTTPError):
        response = httpx.post(DOMAIN + '/notes/create', json=data)
        response.raise_for_status()


def test_note_limit_works():
    httpx.post(DOMAIN + '/notes/create', json=dummy_note_data)
    httpx.post(DOMAIN + '/notes/create', json=dummy_note_data)
    respone = httpx.get(DOMAIN + '/notes/list', params={'limit': 1})
    assert len(respone.json()) == 1
