from flask import Flask

from core import api

from views import site

import os

app = Flask(__name__)

env = os.getenv('ENVIRONMENT', 'development')

if env == 'production':
    app.config.from_object('config.ProductionConfig')
elif env == 'development':
    app.config.from_object('config.DevelopmentConfig')

app.register_blueprint(site.bp)
app.register_blueprint(api.bp, url_prefix='/api')

@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    pass

if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG'))