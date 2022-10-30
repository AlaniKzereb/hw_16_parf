import json

from flask import Flask

from app import db
from app.Models import Offer, Order, User



def load_data(path):
    """ преобразовывает строку JSON в объект Python """
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


def load_offers(path):
    offers = load_data(path)

    for offer in offers:
        db.session.add(
            Offer(
                **offer
                )
            )

        db.session.commit()


def load_orders(path):
    orders = load_data(path)

    for order in orders:
        db.session.add(
            Order(
                **order
            )
        )
        db.session.commit()


def load_users(path):
    users = load_data(path)

    for user in users:
        db.session.add(
            User(
                **user
            )
        )
        db.session.commit()


def create_app():
    """создание подключения"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 4}
    app.config['SQLALCHEMY_EHO'] = True

    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()

        db.create_all()
        offer = load_offers('/Users/User/PycharmProjects/hw_16_parf/data/offers.json')
        order = load_orders('/Users/User/PycharmProjects/hw_16_parf/data/orders.json')
        user = load_users('/Users/User/PycharmProjects/hw_16_parf/data/users.json')

    return app

app = create_app()