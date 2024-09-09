


from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Dummy user data
users = {
    'user1': {'password': 'pbkdf2:sha256:150000$abc123', 'id': 1}
}

@app.route('/authenticate', methods=['POST'])
def authenticate_user():
    username = request.json.get('username')
    password = request.json.get('password')
    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        s = Serializer(app.config['SECRET_KEY'], 600)
        token = s.dumps({'user_id': user['id']}).decode('utf-8')
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)


