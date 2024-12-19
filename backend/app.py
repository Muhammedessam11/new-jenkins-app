from flask import Flask
from app.routes import api_blueprint
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
db.init_app(app)
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
