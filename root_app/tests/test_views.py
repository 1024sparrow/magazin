import pytest

#from django.shortcuts import get_object_or_404
#from django.contrib.auth.models import User

from django.test import TestCase
from root_app.models import Product, BasketedProduct


class TwoProductsTestCase(TestCase):
    def setUp(self):
        Product.objects.create(title='title_1')
        Product.objects.create(title='title_2')

    @pytest.mark.django_db
    def test_card_valid(self):
        #    

        response = self.client.get('/card/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/card/2/')
        self.assertEqual(response.status_code, 200)

    #@pytest.mark.django_db
    #def test_card_novalid(self):
    #    response = self.client.get('/card/3/')
    #    self.assertEqual(response.status_code, 200)


def create_test_user():
    u1 = User.objects.create_user(username='UserName', password='Password123', email='Test@gmail.com')
    return u1


def create_test_superuser():
    u1 = User.objects.create_user(username='admin', password='q1w2e3r4', email='Test@gmail.com')
    return u1


@pytest.mark.django_db
def test_index(client):
    response = client.get('/')
    assert response.status_code == 302 # redirect
    #u1 = create_test_user()


@pytest.mark.django_db
def test_admin(client):
    response = client.get('/admin/')
    assert response.status_code == 200 # ready
    

#@pytest.mark.django_db
#def test_login(client):
#    pass
    

#@pytest.mark.django_db
#def test_login(client):
#    pass
    

@pytest.mark.django_db
def test_catalogue(client):
    response = client.get('/catalogue/')
    assert response.status_code == 200 # ready
    

@pytest.mark.django_db
def test_basket(client):
    response = client.get('/basket/')
    assert response.status_code == 200 # ready


