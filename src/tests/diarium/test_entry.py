import pytest

from cottidie.diarium.models import Entry


@pytest.mark.django_db
def test_create_entry_on_post(user_with_notebook, client):
    assert Entry.objects.count() == 0
    client.force_login(user_with_notebook)
    response = client.post(
        '/diarium/scribe/',
        {'entry': 'some entry data'}
    )
    assert Entry.objects.count() == 1
    assert Entry.objects.first().text == 'some entry data'
    assert Entry.objects.first().notebook == user_with_notebook.diarium.default
    assert response.status_code == 302
    assert response.url == '/diarium/scribe/1/'


@pytest.mark.django_db
def test_redirect_from_unused_url(user_with_notebook, client):
    assert Entry.objects.count() == 0
    client.force_login(user_with_notebook)
    response = client.get(
        '/diarium/scribe/1/',
    )
    assert response.status_code == 302
    assert response.url == '/diarium/scribe/'


@pytest.mark.django_db
def test_load_entry_on_get(entry, client):
    client.force_login(entry.notebook.user)
    response = client.get(
        '/diarium/scribe/{entry.pk}/'.format(entry=entry),
    )
    assert response.status_code == 200
    assert entry.text in response.content.decode()
