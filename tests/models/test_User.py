import pytest
from src.models.User import User

user = User('francesco', True , '333333333' , 'francescosave.ricci@gmail.com', '101024', 1500, True)

def test_type_message():
    assert user.name == 'francesco'

def test_isAdmin():
    assert user.isAdmin == True

def test_email():
    assert user.email == 'francescosave.ricci@gmail.com'

def test_user_data_registration():
    assert user.data_registration == '101024'

def test_size_total():
    assert user.size_total == 1500

def test_isActive():
    assert user.isActive == True
