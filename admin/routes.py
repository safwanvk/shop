from flask import Flask, render_template, request, flash, url_for

from shop import app, db, bcrypt
from werkzeug.utils import redirect

from .forms import RegistrationForm
from .models import User


@app.route('/')
def index():
    return render_template('admin/index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.name.data}Thank you for registering', 'success')
        return redirect(url_for('index'))
    return render_template('admin/register.html', form=form)
