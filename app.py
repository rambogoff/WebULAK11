from flask import Flask, redirect, url_for, render_template, request, session, Response

import db
import json

app = Flask(__name__)


@app.route("/login", methods=['POST'])
def login():
    """

    :return:
    """
    post_data = request.form
    username = post_data['username']
    password = post_data['password']
    db_obj = db.DatabaseConnection()
    actual_password = db_obj.get_user_password(username)

    if actual_password is False:
        return Response(json.dumps({'error': 'User does not exist'}), status=400)

    if password != actual_password:
        return Response(json.dumps({'error': 'Password is wrong'}), status=400)

    return Response(json.dumps({'success': 'Login was successful'}), status=200)


@app.route('/get_hour_date')
def get_hour_date():
    dbObj = db.DatabaseConnection()
    response = dbObj.get_hour_report()

    ex_dict = [{"saha_id": row[0], "bbca0": row[1], "bbca1": row[2]} for row in response]
    return json.dumps(ex_dict, indent=3)


@app.route('/register')
def showregister():
    return render_template('register.html')


@app.route('/showSignIn')
def showSignIn():
    return render_template('signIn.html')


@app.route('/visualization')
def visualization():
    return render_template('visualization.html')


@app.route('/event')
def event():
    return render_template('Event.html')


@app.route("/signup", methods=['POST'])
def signup():
    """

    :return:
    """
    post_data = request.form
    username = post_data['username']
    password = post_data['password']
    user_type = post_data['user_type']
    db_obj = db.DatabaseConnection()
    status = db_obj.user_signup(username, password, user_type)
    return Response(json.dumps({'success': 'User registered successfully'}), status=201) if status else Response(
        json.dumps({'error': 'Something went wrong'}), status=400)


@app.route("/hourdata", methods=['POST'])
def hourdata():
    """
        :return:
    """
    post_data = request.json
    saha_id = post_data['saha_id']
    swm_id = post_data['swm_id']
    reset_cause = post_data['reset_cause']
    swm_date = post_data['swm_date']
    hour_date = post_data['hour_date']
    sum_reset_id = post_data['sum_reset_id']
    hour_reset_id = post_data['hour_reset_id']
    bbca0 = post_data['bbca0']
    bbca1 = post_data['bbca1']
    bbca2 = post_data['bbca2']

    db_obj = db.DatabaseConnection()
    status = db_obj.hour_report(saha_id, swm_id, reset_cause, swm_date, hour_date, sum_reset_id, hour_reset_id, bbca0,
                                bbca1, bbca2)
    return Response(json.dumps({'success': 'Registered successfully'}), status=201) if status else Response(
        json.dumps({'error': 'Something went wrong'}), status=400)


@app.route("/daydata", methods=['POST'])
def daydata():
    """
        :return:
    """
    post_data = request.json
    day_date = post_data['day_date']
    saha_id = post_data['saha_id']
    sum_reset_id = post_data['sum_reset_id']
    swm_did = post_data['swm_did']
    sum_ue = post_data['sum_ue']
    db_obj = db.DatabaseConnection()
    status = db_obj.day_report(day_date, saha_id, sum_reset_id, swm_did, sum_ue)
    return Response(json.dumps({'success': 'Registered successfully'}), status=201) if status else Response(
        json.dumps({'error': 'Something went wrong'}), status=400)


@app.route("/signup2")
def signup2():
    return render_template("signin2.html")


@app.route("/signin2")
def signin2():
    return render_template("signup2.html")


@app.route("/open")
def open():
    return render_template("open.html")


@app.route("/yuk")
def yuk():
    return render_template("yuk.html")


@app.route("/sahaday")
def sahaday():
    return render_template("sahaday.html")


@app.route("/help404")
def help404():
    return render_template("404.html")


@app.route('/')
@app.route('/home.html')
def main():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
