import pytest
from src.models.HistoryEmissions import HistoryEmissions

history = HistoryEmissions('101024', 15000 , 'C')

def test_type_timestamp():
    assert history.timestamp == '101024'

def test_emission_day():
    assert history.emission_day == 15000

def test_type_history():
    assert history.type_history == 'C'