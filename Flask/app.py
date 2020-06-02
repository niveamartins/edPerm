from flask import Flask
from controller.endpoints import blueprint
from extensions import jwt

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.secret_key = b'\xae\xf3\x8e\x03\xb8\x9c\x87&\xae\xc4\xf5+'

jwt.init_app(app)

app.register_blueprint(blueprint, url_prefix="/api")

if __name__ == "__main__":

    app.run(host="127.0.0.1", port=5000, threaded=True, debug=True)