from collections import namedtuple

from flask import Flask, request, jsonify


app = Flask(__name__)


Login = namedtuple('Login', ['username', 'password'])

LOGIN_TOKENS = {
    Login('clara', 'password'): '12345',
    Login('karl', 'p@ssworD'): '67890',
}


@app.route('/get_token/', methods=['POST'])
def get_token():
    token = LOGIN_TOKENS.get(_login(**request.json))

    if token is not None:
        return jsonify(token=token), 200

    return jsonify(error='Invalid Login'), 401


@app.route('/check_token/', methods=['POST'])
def check_token():
    token = request.json.get('token')

    if token in LOGIN_TOKENS.values():
        return jsonify(status='success'), 200

    return jsonify(error='Invalid token'), 401


def _login(username=None, password=None, **kwargs):
    return Login(username, password)


if __name__ == '__main__':
    app.run(debug=True)
