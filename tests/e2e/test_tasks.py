import httpx


def test_can_create_task(user_json, task_json, domain):
    with httpx.Client() as client:
        user_login_json = {
            'username': user_json['email'],
            'password': user_json['password'],
        }
        login_response = client.post(
            domain + '/auth/login', data=user_login_json
        )
        cookie = login_response.cookies
        response = client.post(
            domain + '/tasks/create',
            headers={
                'Cookie': f'fastapiusersauth={cookie["fastapiusersauth"]}'
            },
            json=task_json
        )
    assert response.status_code == 200
