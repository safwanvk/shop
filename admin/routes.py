from flask import Flask, render_template, request, flash, url_for

from shop import app, db
from werkzeug.utils import redirect

from .forms import RegistrationForm


@app.route('/')
def index():
    return "Home Page"


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = User(form.username.data, form.email.data,
        #             form.password.data)
        # db.session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form)
