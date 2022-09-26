import pytest
from fastapi import HTTPException
import main

moc_users = [
    {
        "name=": "Test1",
        "email": "test1@something.com",
        "phone": "123 456-1234"
    },
    {
        "name=": "Test2",
        "email": "test2@nowhere.com",
        "phone": "987 456-9876"
    }
]


def test_get():
    main.users = moc_users
    users_return = main.get_users()
    assert users_return == moc_users


def test_put():
    u = main.User(name="NewName", email="new@email.com", phone="987 123-4567")
    users_return = main.update_user(0, u)
    assert users_return[0] == u


def test_put_bad_index():
    u = main.User(name="NewName", email="new@email.com", phone="987 123-4567")
    with pytest.raises(HTTPException):
        main.update_user(9999, u)


def test_put_bad_user():
    with pytest.raises(HTTPException):
        main.update_user(0, None)


def test_post():
    u = main.User(name="NewName", email="new@email.com", phone="987 123-4567")
    moc_users.append(u)
    users_return = main.create_user(u)
    assert users_return == moc_users


def test_post_bad_user():
    with pytest.raises(HTTPException):
        main.create_user(None)
