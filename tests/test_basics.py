def test_send_ok(client):
    prefix = '/api'
    response = client.get(prefix + '/')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == 'OK'


def test_hello_world_endpoint(client):
    prefix = '/api'
    response = client.get(prefix + '/greeting')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == '"Hello, World!"\n'

