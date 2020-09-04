from flask import render_template, request, flash, url_for

from shop import app
from werkzeug.utils import redirect

from .models import Brand
from .. import db


@app.route('/add-brand', methods=['GET', 'POST'])
def add_brand():
    if request.method == 'POST':
        get_brand = request.form['brand']
        brand = Brand(name=get_brand)
        db.session.add(brand)
        db.session.commit()
        flash(f'The brand {get_brand} was added to your database', 'success')
        return redirect(url_for('add_brand'))
    return render_template('products/add_brand.html', brands='brands')
