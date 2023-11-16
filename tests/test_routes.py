import pytest
from application import application


@pytest.fixture
def client():
    application.config['TESTING'] = True
    with application.test_client() as client:
        yield client


def test_get_cards_valid_quantity(client):
    response = client.get('/cards/?quantity=5')
    assert response.status_code == 200
    assert len(response.json) == 5


def test_get_cards_zero_quantity(client):
    response = client.get('/cards/?quantity=0')
    assert response.status_code == 400


def test_get_cards_excessive_quantity(client):
    response = client.get('/cards/?quantity=53')
    assert response.status_code == 400


def test_get_cards_negative_quantity(client):
    response = client.get('/cards/?quantity=-1')
    assert response.status_code == 400


def test_get_cards_no_quantity(client):
    response = client.get('/cards/')
    assert response.status_code == 200
    assert len(response.json) == 1  # Default is 1 card


def test_get_card_valid_suit(client):
    for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
        response = client.get(f'/card/{suit}')
        assert response.status_code == 200
        assert response.json['suit'] == suit


def test_get_card_invalid_suit(client):
    response = client.get('/card/InvalidSuit')
    assert response.status_code == 404


def test_card_suit_and_value_integrity(client):
    response = client.get('/cards/?quantity=52')
    assert response.status_code == 200
    valid_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    valid_values = ['2', '3', '4', '5', '6', '7', '8',
                    '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    for card in response.json:
        assert card['suit'] in valid_suits
        assert card['value'] in valid_values
