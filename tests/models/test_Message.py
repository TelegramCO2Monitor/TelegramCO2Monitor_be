import pytest
from src.models.Message import Message

msg = Message('Sticker', 100 , '101024' , 105)

def test_type_message():
    msg.type_message = 'text'
    assert msg.type_message == 'text'

def test_size():
    assert msg.size == 100

def test_timestamp():
    assert msg.timestamp == '101024'

def test_user_id():
    assert msg.user_id == 105