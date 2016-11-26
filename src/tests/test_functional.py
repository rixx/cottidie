import pytest


@pytest.mark.parametrize('url,verb,expected_response', [
    ('/admin/login/', 'GET', 200),
])
def test_urls(client, url, verb, expected_response):
    print('running')
    if verb == 'GET':
        response = client.get(url)

    assert response.status_code == expected_response
