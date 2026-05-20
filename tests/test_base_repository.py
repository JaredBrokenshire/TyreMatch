import pytest
from sqlalchemy.exc import IntegrityError

from database.models import TyreModel
from database.repositories.base_repository import BaseRepository


def test_create(database_session):
    repo = BaseRepository(database_session, TyreModel)

    # Can not create entity with required fields missing
    with pytest.raises(IntegrityError):
        repo.create()

    # Can create entity
    tyre_model = repo.create(manufacturer='Michelin', model_name='Test Tyre Model')

    assert tyre_model.manufacturer is not None
    assert tyre_model.manufacturer == 'Michelin'
    assert tyre_model.model_name is not None
    assert tyre_model.model_name == 'Test Tyre Model'

def test_get_by_id(database_session):
    repo = BaseRepository(database_session, TyreModel)

    # Can get by ID
    created = repo.create(manufacturer='Michelin', model_name='Test Tyre Model')
    found = repo.get_by_id(created.id)

    assert found.id is not None
    assert found.id == created.id
    assert found.manufacturer == 'Michelin'
    assert found.model_name == 'Test Tyre Model'


    # Can not get by invalid ID
    invalid_id = 999999

    found = repo.get_by_id(invalid_id)

    assert found is None

def test_get_all(database_session):
    repo = BaseRepository(database_session, TyreModel)

    repo.create(manufacturer='Michelin', model_name='Test Tyre Model')
    repo.create(manufacturer='Not Michelin', model_name='Different Model Name')

    results = repo.get_all()

    assert len(results) == 2
    assert any(tyre_model.manufacturer == "Michelin" for tyre_model in results)
    assert any(tyre_model.manufacturer == "Not Michelin" for tyre_model in results)
    assert any(tyre_model.model_name == "Test Tyre Model" for tyre_model in results)
    assert any(tyre_model.model_name == "Different Model Name" for tyre_model in results)

def test_delete(database_session):
    repo = BaseRepository(database_session, TyreModel)

    # Can delete model that exists
    tyre_model = repo.create(manufacturer='Delete Me', model_name='Delete Me')

    result = repo.delete(tyre_model.id)

    assert result is True
    assert repo.get_by_id(tyre_model.id) is None

    # Can't delete model that doesn't exist
    result = repo.delete(999999)

    assert result is False