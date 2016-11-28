import pytest


@pytest.mark.django_db
@pytest.mark.parametrize('url,verb,expected_response', [
    ('/admin/', 'GET', 200),
])
def test_urls(logged_in_superuser_client, url, verb, expected_response):
    if verb == 'GET':
        response = logged_in_superuser_client.get(url)

    assert response.status_code == expected_response
