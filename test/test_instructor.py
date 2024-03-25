import os
import pytest
import pytest_lazyfixture 

def test_instructor(self):
    response = self. responses
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
    assert b'Instructores encontrados' in response.data
    assert b'Clase actualizada' in response.data
    assert b'Clase eliminada' in response.data

def test_index(self):
    response = self. responses
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
    assert b'Instructores encontrados' in response.data
    assert b'Clase actualizada' in response.data
    assert b'Clase eliminada' in response.data

def test_create_class(self):
    response = self. responses
    assert response.status_code == 201
    assert b'Clase creada' in response.data
    