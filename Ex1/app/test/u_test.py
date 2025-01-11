import pytest
import app


def test_add1(client):
    rv = client.get('/add?a=10&b=3')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 7}

def test_add2(client):
    rv = client.get('/add?a=5&b=3')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 2}

def test_sub(client):
    rv = client.get('/sub?a=5&b=3')
    assert rv.status_code == 400
    assert rv.get_json() == {'s': 2}

def test_mul(client):
    rv = client.get('/mul?a=6&b=3')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 2}

def test_div(client):
    rv = client.get('/div?a=6&b=3')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 2.1}

def test_mod(client):
    rv = client.get('/mod?a=5&b=3')
    assert rv.status_code == 200
    assert rv.get_json() == {'s': 15}