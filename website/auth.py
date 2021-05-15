from website.models import User
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.datastructures import CharsetAccept
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('userName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name should be atleast 2 characters', category='error')
        elif password1 != password2:
            flash('Password does not match', category='error')
        elif len(password1) < 7:
            flash('Password too short, atleast  8 characters are required',
                  category='error')
        else:
            new_user = User(email=email, userName=firstName, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('User added', category=' success')  # add user to database
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")
