from django.test import TestCase
import pytest
from django.urls import reverse
from django.urls import reverse_lazy
# Create your tests here.

@pytest.mark.parametrize('url', 'index')
@pytest.mark.django_db
def test_status(client, url):
    response = client.get(reverse(url))
    assert response.status_code == 200


@pytest.mark.parametrize('url', 'logged')
@pytest.mark.django_db
def test_status(client, url):
    response = client.get(reverse(url))
    assert response.status_code == 200


@pytest.mark.parametrize('url', 'offer')
@pytest.mark.django_db
def test_status(client, url):
    response = client.get(reverse(url))
    assert response.status_code == 200


@pytest.mark.parametrize('url', 'signUp')
@pytest.mark.django_db
def test_status(client, url):
    response = client.get(reverse(url))
    assert response.status_code == 200

