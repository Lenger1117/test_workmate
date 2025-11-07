import pytest
from reporters.average_rating import generate_average_rating_report

def test_average_rating_basic():
    data = [
        {'name': 'model1', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'},
        {'name': 'model2', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'model3', 'brand': 'apple', 'price': '899', 'rating': '4.7'},
    ]
    result = generate_average_rating_report(data)
    expected = [('apple', (4.9 + 4.7) / 2), ('samsung', 4.8)]
    assert result == expected

def test_empty_data():
    assert generate_average_rating_report([]) == []

def test_case_insensitive_brand():
    data = [
        {'name': 'model1', 'brand': 'Apple', 'price': '100', 'rating': '5.0'},
        {'name': 'model2', 'brand': 'apple', 'price': '200', 'rating': '4.0'},
    ]
    result = generate_average_rating_report(data)
    assert len(result) == 1
    assert result[0][0] == 'apple'
    assert abs(result[0][1] - 4.5) < 0.001