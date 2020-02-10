import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from anyway.core import config, utils
from webassets import Environment as AssetsEnvironment
from flask_babel import Babel, gettext
from flask_assets import Environment
from flask_cors import CORS
from flask_compress import Compress

_PROJECT_ROOT = os.path.join(os.path.dirname(__file__))

"""
initializes a Flask instance with default values
"""
app = Flask(
    "anyway",
    template_folder=os.path.join(config._PROJECT_ROOT, 'templates'),
    static_folder=os.path.join(config._PROJECT_ROOT, 'static'))
app.config.from_object(config)
app.config['BABEL_TRANSLATION_DIRECTORIES'] = os.path.join(config._PROJECT_ROOT, 'translations')
app.config['SECURITY_REGISTERABLE'] = False
app.config['SECURITY_USER_IDENTITY_ATTRIBUTES'] = 'username'
app.config['BABEL_DEFAULT_LOCALE'] = 'he'
app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': os.environ.get('FACEBOOK_KEY'),
        'secret': os.environ.get('FACEBOOK_SECRET')
    },
    'google': {
        'id': os.environ.get('GOOGLE_LOGIN_CLIENT_ID'),
        'secret': os.environ.get('GOOGLE_LOGIN_CLIENT_SECRET')
    }
}
app.config['RESTPLUS_MASK_SWAGGER'] = False

db = SQLAlchemy(app)

from anyway.apis.common.models import cbs_models, news_flash_models, schools_models, public_models, mobile_app_models

assets = Environment()
assets.init_app(app)
assets_env = AssetsEnvironment(os.path.join(config._PROJECT_ROOT, 'static'), '/static')

CORS(app, resources={r"/location-subscription": {"origins": "*"}, r"/report-problem": {"origins": "*"}})

# sg = SendGridAPIClient(app.config['SENDGRID_API_KEY'])

babel = Babel(app)

Compress(app)


from anyway.apis import api
api.init_app(app)
