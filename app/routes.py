# app/routes.py
import random
from flask import jsonify, request


def generate_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8',
              '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    return [{'suit': suit, 'value': value} for suit in suits for value in values]


def init_routes(app):
    @app.route('/cards/', methods=['GET'])
    def get_cards():
        quantity = request.args.get('quantity', default=1, type=int)
        if quantity < 1 or quantity > 52:
            return jsonify({'error': 'Quantity must be between 1 and 52'}), 400
        deck = generate_deck()
        random.shuffle(deck)
        return jsonify(deck[:quantity])

    @app.route('/card/<suit>', methods=['GET'])
    def get_card(suit):
        deck = generate_deck()
        suit_cards = [card for card in deck if card['suit'].lower()
                      == suit.lower()]
        if not suit_cards:
            return jsonify({'error': 'No cards of suit ' + suit}), 404
        card = random.choice(suit_cards)
        return jsonify(card)
