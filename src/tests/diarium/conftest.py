import pytest
from cottidie.diarium.models import DiariumProfile, Entry, Notebook


@pytest.fixture
def notebook(normal_user):
    return Notebook.objects.create(
        user=normal_user,
        title='TestNotebook'
    )


@pytest.fixture
def user_with_notebook(notebook):
    DiariumProfile.objects.create(
        user=notebook.user,
        default=notebook,
    )
    return notebook.user


@pytest.fixture
def entry(user_with_notebook):
    return Entry.objects.create(
        notebook=user_with_notebook.diarium.default,
        text='Test entry in a notebook, does not conform to quill synatax.'
    )
