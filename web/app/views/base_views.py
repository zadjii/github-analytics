################### These ALL need to be imported EVRYWHERE ###################
import os
from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for,
    request,
    flash,
    g,
    jsonify,
    abort,
    make_response,
    Flask,
    send_from_directory,
)
from flask_login import login_user, logout_user, current_user, login_required

# from werkzeug import secure_filename
# from flask_wtf.file import FileField

from app import app

# from app import login_manager
# from ..forms import LoginForm, PostForm
# from ..models.User import User
# from ..models.Post import Post
# from .. import db
# from datetime import datetime, date, time, timedelta
# from werkzeug.security import generate_password_hash, \
#     check_password_hash
# from sqlalchemy import or_
################################################################################
base = Blueprint("base", __name__)
################################################################################

# @base.before_request
# def before_request():
#     g.user = current_user

# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(int(id))

# @login_manager.unauthorized_handler
# def unauthorized():
#     return redirect(url_for('base.login'))
################################################################################

################################################################################
################################################################################
@base.route("/")
@base.route("/index")
@base.route("/homepage")
def homepage():
    return render_template("index.html.tmpl")


################################################################################
@base.route("/graph")
def graph():
    return render_template("graph.html.tmpl")


################################################################################
@base.route("/table")
def table():
    return render_template("table.html.tmpl")


################################################################################
