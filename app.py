from flask import Flask, jsonify, request
from flask_jwt_oidc import JwtManager


app = Flask(__name__)



app.config["OIDC_CLIENT_SECRETS"]={

        "web": {
            "issuer": "http://100.130.101.108:30162/auth/realms/fs",
            "auth_uri": "http://100.130.101.108:30162/auth/realms/fs/protocol/openid-connect/auth",
            "client_id": "test",
            "client_secret": "UUep9zGpZL2FaiLYc8uADKCdD87ZxMVJ",

            }
        }
jwt = JwtManager(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test-auth')
@jwt.requires_auth
def keycloaktest():
    user = jwt.get_user_info()
    return jsonify(message="requires auth route", user=user)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
