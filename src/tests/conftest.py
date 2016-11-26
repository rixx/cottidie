import pytest


@pytest.fixture
def superuser(django_user_model):
    return django_user_model.objects.create(
        is_superuser=True,
        is_staff=True,
        username='test_superuser',
    )


@pytest.fixture
def normal_user(django_user_model):
    return django_user_model.objects.create(
        username='test_user1',
    )


@pytest.fixture
def logged_in_superuser_client(superuser, client):
    client.force_login(superuser)
    return client


@pytest.fixture
def logged_in_client(normal_user, client):
    client.force_login(normal_user)
    return client
