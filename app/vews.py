import json

from flask import request
from app.models import User, Order, Offer
from app.utils import db, app


@app.route("/users", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        result = []
        for user in db.session.query(User).all():
            result.append(user.get_data())
        return app.response_class(json.dumps(result),
                                  mimetype='application/json',
                                  status=200)
    if request.method == 'POST':
        data = request.json
        db.session.add(
            User(
                **data
            )
        )
        return app.response_class(json.dumps("ok"),
                                  mimetype='application/json',
                                  status=200)


@app.route("/users/<int:uid>", methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(uid):
    if request.method == 'GET':
        result = []
        for user in db.session.query(User).filter(User.id == uid).all():
            result.append(user.get_data())
        return app.response_class(json.dumps(result),
                                  mimetype='application/json',
                                  status=200)
    if request.method == 'PUT':
        data = request.json
        user = db.session.query(User).filter(User.id == uid).one()
        # user = db.session.query(User).get(uid)
            # user = db.session.query(User).filter(User.id == uid).get(uid)
        user.id = data.get("id")
        user.first_name = data.get("first_name")
        user.last_name = data.get("last_name")
        user.age = data.get("age")
        user.email = data.get("email")
        user.role = data.get("role")
        user.phone = data.get("phone")
        db.session.commit()
        return app.response_class(json.dumps("ok"),
                                  mimetype='application/json',
                                  status=200)
    if request.method == 'DELETE':
        db.session.query(User).filter(User.id == uid).delete()
        db.session.commit()
        return app.response_class(json.dumps("ok"),
                                  mimetype='application/json',
                                  status=200)


@app.route("/orders", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        result = []
        for order in db.session.query(Order).all():
            result.append(order.get_data())
        return app.response_class(json.dumps(result),
                                  mimetype='application/json',
                                  status=200)
    if request.method == 'POST':
        data = request.json
        db.session.add(
            Order(
                **data
            )
        )
        return app.response_class(json.dumps("ok"),
                                  mimetype='application/json',
                                  status=200)


@app.route("/orders/<int:oid>", methods=['GET', 'PUT', 'DELETE'])
def get_orders_by_id(oid):
    if request.method == 'GET':
        result = []
        for order in db.session.query(Order).filter(Order.id == oid).all():
            result.append(order.get_data())
        return app.response_class(json.dumps(result),
                                  mimetype='application/json',
                                  status=200)
    if request.method == 'PUT':
        data = request.json
        order = db.session.query(Order).get(oid)
        order.id = data.get("id")
        order.name = data.get("name")
        order.description = data.get("description")
        order.start_date = data.get("start_date")
        order.end_date = data.get("end_date")
        order.address = data.get("address")
        order.price = data.get("price")
        order.customer_id = data.get("customer_id")
        order.executor_id = data.get("executor_id")
        db.session.commit()
        return app.response_class(json.dumps("ok"),
                                  mimetype='application/json',
                                  status=200)
    if request.method == 'DELETE':
        db.session.query(Order).filter(Order.id == oid).delete()
        db.session.commit()
        return app.response_class(json.dumps("ok"),
                                  mimetype='application/json',
                                  status=200)


@app.route("/offers", methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        result = []
        for offer in db.session.query(Offer).all():
            result.append(offer.get_data())
        return app.response_class(json.dumps(result),
                                  mimetype='application/json',
                                  status=200)
    if request.method == 'POST':
        data = request.json
        db.session.add(
            Offer(
                **data
            )
        )
        return app.response_class(json.dumps("ok"),
                                  mimetype='application/json',
                                  status=200)


@app.route("/offers/<int:oid>", methods=['GET', 'PUT', 'DELETE'])
def get_offers_by_id(oid):
    if request.method == 'GET':
        result = []
        for offer in db.session.query(Offer).filter(Offer.id == oid).all():
            result.append(offer.get_data())
        return app.response_class(json.dumps(result, ensure_ascii=False),
                                  mimetype='application/json', status=200)
    if request.method == 'PUT':
        data = request.json
        offer = db.session.query(Offer).get(oid)
        # offer = db.session.filter(Offer.id == oid).get(oid)
        offer.id = data.get("id")
        offer.order_id = data.get("order_id")
        offer.executor_id = data.get("executor_id")
        db.session.commit()
        return app.response_class(json.dumps("ok"),
                                  mimetype='application/json',
                                  status=200)
    if request.method == 'DELETE':
        db.session.query(Offer).filter(Offer.id == oid).delete()
        db.session.commit()
        return app.response_class(json.dumps("ok"),
                                  mimetype='application/json',
                                  status=200)


if __name__ == '__main__':
    app.run()



