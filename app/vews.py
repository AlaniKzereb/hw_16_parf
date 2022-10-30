import json

from flask import request


from app.Models import User, Order, Offer
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
        try:
            user = db.session.filter(User.id == uid).get(uid)
            user.id = data.get("id")
            user.first_name = data.get("first_name")
            user.last_name = data.get("last_name")
            user.age = data.get("age")
            user.email = data.get("email")
            user.role = data.get("role")
            user.phone = data.get("phone")

            db.session.commit()

        except Exception as e:
            print(e)



        return app.response_class(json.dumps("ok"),
                                  mimetype='application/json',
                                  status=200)
    if request.method == 'DELETE':

        try:
            db.session.query(User).filter(User.id == uid).delete()
            db.session.commit()

        except Exception as e:
            print(e)



        return app.response_class(json.dumps("ok"),
                                  mimetype='application/json',
                                  status=200)



@app.route("/orders", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        result = []
        for user in db.session.query(Order).all():

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

@app.route("/orders/<int:oid>", methods=['GET', 'PUT', 'DELETE'])
def get_orders_by_id(oid):
    if request.method == 'GET':
        result = []
        for user in db.session.query(Order).filter(Order.id == oid).all():

            result.append(user.get_data())

        return app.response_class(json.dumps(result),
                                  mimetype='application/json',
                                  status=200)


    if request.method == 'PUT':

        data = request.json
        try:
            order = db.session.filter(Order.id == oid).get(oid)
            order.id = data.get("id")
            order.name = data.get("first_name")
            order.description = data.get("last_name")
            order.start_date = data.get("age")
            order.end_date = data.get("email")
            order.address = data.get("role")
            order.price = data.get("phone")
            order.customer_id = data.get("customer_id")
            order.executor_id = data.get("executor_id")

            db.session.commit()

        except Exception as e:
            print(e)



        return app.response_class(json.dumps("ok"),
                                  mimetype='application/json',
                                  status=200)
    if request.method == 'DELETE':

        try:
            db.session.query(Order).filter(User.id == oid).delete()
            db.session.commit()

        except Exception as e:
            print(e)



        return app.response_class(json.dumps("ok"),
                                  mimetype='application/json',
                                  status=200)



@app.route("/offers", methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        result = []
        for user in db.session.query(Offer).all():

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

@app.route("/offers/<int:oid>", methods=['GET', 'PUT'])
def get_offers_by_id(oid):
    if request.method == 'GET':
        result = []
        for user in db.session.query(Offer).filter(Offer.id == oid).all():

            result.append(user.get_data())

        return app.response_class(json.dumps(result, ensure_ascii=False),
                                  mimetype='application/json', status=200)

    if request.method == 'PUT':

        data = request.json
        try:
            order = db.session.filter(Order.id == oid).get(oid)
            order.id = data.get("id")
            order.name = data.get("first_name")
            order.description = data.get("last_name")
            order.start_date = data.get("age")
            order.end_date = data.get("email")
            order.address = data.get("role")
            order.price = data.get("phone")
            order.customer_id = data.get("customer_id")
            order.executor_id = data.get("executor_id")

            db.session.commit()

        except Exception as e:
            print(e)



        return app.response_class(json.dumps("ok"),
                                  mimetype='application/json',
                                  status=200)

    if request.method == 'DELETE':

        try:
            db.session.query(Order).filter(User.id == oid).delete()
            db.session.commit()

        except Exception as e:
            print(e)



        return app.response_class(json.dumps("ok"),
                                  mimetype='application/json',
                                  status=200)


if __name__ == '__main__':

    app.run()



