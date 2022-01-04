__author__ = 'Mike'

import os, sys

from flask import Flask, render_template, session, send_from_directory,\
    redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# from werkzeug.contrib.cache import SimpleCache
# from flask_marshmallow import Marshmallow

# from config import basedir

app = Flask(__name__
            # , static_url_path='/static'
            # , static_url_path=''
            # , static_folder='/app/static'
            )
# app.config.from_object('config')

db = SQLAlchemy(app)
# marsh = Marshmallow(app)

################################################################################
# Import Models                                                                #
################################################################################
# from app.models.User import User
# from app.models.Post import Post
################################################################################

################################################################################
# Setup login Manager                                                          #
################################################################################
# from flask_login import LoginManager
# from flask_login import login_required
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'base.login'
################################################################################

################################################################################
# Register all the blueprints                                                  #
################################################################################

from app.views import base_views

app.register_blueprint(base_views.base)

# from api.v1 import apiv1
# app.register_blueprint(apiv1, url_prefix='/api/v1')

################################################################################




################################################################################
# Other assorted global nonsense                                               #
################################################################################
def nl2br(value):
     return value.replace('\n','<br>\n')

app.jinja_env.filters['nl2br'] = nl2br


