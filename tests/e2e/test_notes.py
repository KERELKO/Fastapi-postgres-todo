import httpx


def test_can_create_note(user_json, note_json, domain):
    with httpx.Client() as client:
        user_login_json = {
            'username': user_json['email'],
            'password': user_json['password'],
        }
        login_response = client.post(
            domain + '/auth/jwt/login', data=user_login_json
        )
        cookie = login_response.cookies
        response = client.post(
            domain + '/notes/create',
            headers={
                'Cookie': f'fastapiusersauth={cookie["fastapiusersauth"]}'
            },
            json=note_json
        )
    assert response.status_code == 200
