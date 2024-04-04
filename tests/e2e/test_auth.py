import uuid
import httpx


def test_can_register_user(domain, user_json):
    user_json['email'] = str(uuid.uuid4()) + '@example.com'
    user_json['username'] = str(uuid.uuid4())
    response = httpx.post(domain + '/auth/register', json=user_json)
    assert response.status_code == 201


def test_can_login_and_logout(domain, user_json):
    with httpx.Client() as client:
        client.post(domain + '/auth/register', json=user_json)
        user_login_json = {
            'username': user_json['email'],
            'password': user_json['password'],
        }
        login_response = client.post(
            domain + '/auth/login', data=user_login_json
        )
        assert login_response.status_code == 204
        cookie = login_response.cookies

        logout_response = client.post(
            domain + '/auth/logout',
            headers={
                'Cookie': f'fastapiusersauth={cookie["fastapiusersauth"]}'
            }
        )
        assert logout_response.status_code == 204


def test_can_get_current_user(domain, user_json, pk: int = 1):
    with httpx.Client() as client:
        client.post(domain + '/auth/register', json=user_json)
        user_login_json = {
            'username': user_json['email'],
            'password': user_json['password'],
        }
        login_response = client.post(
            domain + '/auth/login', data=user_login_json
        )
        cookie = login_response.cookies
        current_user_response = client.get(
            domain + '/users/me',
            headers={
                'Cookie': f'fastapiusersauth={cookie["fastapiusersauth"]}'
            }
        )
        assert current_user_response.json()['username'] == 'super'


def test_cannot_get_user_list(domain):
    response = httpx.get(domain + '/users/list')
    assert response.status_code == 401
